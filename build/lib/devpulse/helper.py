import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime
import time
from colorama import init, Fore, Style

init(autoreset=True)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print(
        f"{Fore.RED}[DevPulse] GOOGLE_API_KEY is not set!{Style.RESET_ALL}\n"
        f"Please create a .env file in your project root with:\n\n"
        f"{Fore.YELLOW}GOOGLE_API_KEY=your_gemini_api_key_here{Style.RESET_ALL}\n"
        f"You can get a Gemini API key from: {Fore.CYAN}https://aistudio.google.com/app/apikey{Style.RESET_ALL}\n"
        f"\nAvailable Gemini models:\n"
        f"  - gemini-2.0-pro\n"
        f"  - gemini-2.0-pro-vision\n"
        f"  - gemini-2.0-flash\n"
        f"  - gemini-1.5-pro-latest\n"
        f"  - gemini-1.5-flash-latest\n"
        f"\nSet your preferred model in the code if you want to change it."
    )
    raise ValueError("GOOGLE_API_KEY is not set. Please add it to your .env file.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # You can change this to any available model above
    temperature=0.2,
    max_output_tokens=512,
    top_p=0.7,
    top_k=20,
    max_retries=1,
    google_api_key=api_key,
)

error_prompt = ChatPromptTemplate.from_template(
    "In clear, natural, concise language, explain this programming error in about 2 sentences: {error_message}"
)
error_chain = error_prompt | llm

command_prompt = ChatPromptTemplate.from_template(
    "Explain what this terminal command does, clearly and simply in 1-2 sentences: {command}"
)
command_chain = command_prompt | llm

LEVEL_COLORS = {
    "INFO": Fore.CYAN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "SUCCESS": Fore.GREEN,
}

def explain_error(error_message: str) -> str:
    start = time.time()
    response = error_chain.invoke({"error_message": error_message})
    elapsed = time.time() - start
    return format_reply(response.content if hasattr(response, "content") else str(response), "WARNING", elapsed)

def explain_command(command: str) -> str:
    start = time.time()
    response = command_chain.invoke({"command": command})
    elapsed = time.time() - start
    return format_reply(response.content if hasattr(response, "content") else str(response), "INFO", elapsed)

def format_reply(reply: str, level: str = "INFO", response_time: float = 1.0) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    color = LEVEL_COLORS.get(level, Fore.WHITE)
    time_str = f"{Fore.MAGENTA}[{now}]{Style.RESET_ALL}"
    level_str = f"{color}[{level}]{Style.RESET_ALL}"
    ai_str = f"{Fore.GREEN}DevPulse AI{Style.RESET_ALL}"
    return f"{time_str} {level_str} {ai_str} ({response_time:.2f}s): {reply.strip()}"

def is_probable_error(line: str) -> bool:
    """
    Basic filter to check if a line likely contains an error.
    """
    keywords = ["error", "exception", "traceback", "not found", "undefined"]
    return any(keyword in line.lower() for keyword in keywords)
