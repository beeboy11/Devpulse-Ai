# DevPulse AI VS Code Extension

DevPulse AI is a Visual Studio Code extension that provides clear, instant explanations for Python errors using Google Gemini models. With DevPulse, you can run your Python files and get immediate, human-friendly explanations for any errors that occur.

---

## Features

- Explains Python errors in plain English right after your code runs.
- Simple right-click menu: run any Python file with DevPulse from the Explorer.
- Lets you set your own Gemini API key from within VS Code.
- Works with your existing Python projects and workflow.

---

## Getting Started

### 1. Install the Extension

- Install from the VS Code Marketplace, or
- Download the `.vsix` file and install it via the Extensions sidebar.

### 2. Install the DevPulse Python Package

Open your terminal and run:
```
pip install devpulse
```

### 3. Set Up Your Gemini API Key

- Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
- You can set your key in a `.env` file in your project root:
  ```
  GOOGLE_API_KEY=your_gemini_api_key_here
  ```
- Or, use the command palette in VS Code:
  - Press `Ctrl+Shift+P`
  - Search for "DevPulse: Set Gemini API Key"
  - Enter your API key when prompted

---

## Usage

1. Right-click any Python file in the VS Code Explorer.
2. Select "Run with DevPulse (Explain Errors)".
3. Your code will run in a new terminal. If an error occurs, DevPulse will print an explanation immediately after the error message.

---

## Requirements

- Python 3.7 or higher
- The `devpulse` Python package
- A Google Gemini API key

---

## Configuration

- The Gemini model used by default is `gemini-2.0-flash`. You can change this in your `.env` file or in the Python package code.
- The `.env` file should be in your project root and contain your API key.

---

## Troubleshooting

- If you do not see explanations, make sure your `.env` file is present and contains a valid `GOOGLE_API_KEY`.
- Ensure the `devpulse` Python package is installed and available in your PATH.
- Reload VS Code after installing the extension.
- Make sure you are right-clicking a Python file in the Explorer.

---

## License

MIT License

---

## Author

BugHunter (beeboyabiodun111@gmail.com)

---

##