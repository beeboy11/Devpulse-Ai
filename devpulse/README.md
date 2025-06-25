# DevPulse

DevPulse is a Python package and VS Code extension that provides instant, clear explanations for Python errors and terminal commands using Google Gemini models. Run your Python files and let DevPulse help you understand and fix issues faster.

---

## Features

- Explains Python errors in plain English right after your code runs.
- CLI tool: `devpulse run your_script.py` explains errors after execution.
- VS Code extension: Right-click any Python file and select "Run with DevPulse (Explain Errors)".
- Lets you set your own Gemini API key.
- Works with your existing Python projects and workflow.

---

## Installation

Install DevPulse from PyPI:

```
pip install devpulse
```

---

## Usage

### CLI

Run any Python script and get instant error explanations:

```
devpulse run your_script.py
```

You can also explain a specific error or command:

```
devpulse explain --text "NameError: name 'l' is not defined" --type error
devpulse explain --text "ls -la" --type command
```

### VS Code Extension

1. Install the DevPulse AI extension from the VS Code Marketplace.
2. Right-click any Python file in the Explorer.
3. Select "Run with DevPulse (Explain Errors)".
4. If an error occurs, DevPulse will print an explanation immediately after the error message.

---

## Configuration

1. Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Create a `.env` file in your project root:
    ```
    GOOGLE_API_KEY=your_gemini_api_key_here
    ```
3. You can also set your API key from the VS Code command palette:  
   Search for "DevPulse: Set Gemini API Key".

---

## Requirements

- Python 3.7 or higher
- Google Gemini API key

---

## License

MIT License

---

## Author

Abiodun (beeboyabiodun111@gmail.com)

---

## Contributing

Contributions and issues are welcome. See the [GitHub repository](https://github.com/beeboy11/devpulse) for details.