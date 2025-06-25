const vscode = require("vscode");
const fs = require("fs");
const path = require("path");

function activate(context) {
    console.log("DevPulse AI extension is now active!");

    // Register runWithDevPulse command
    let runDisposable = vscode.commands.registerCommand("devpulse.runWithDevPulse", (uri) => {
        if (!uri || !uri.fsPath) {
            vscode.window.showErrorMessage("No file selected.");
            return;
        }
        const terminal = vscode.window.createTerminal("DevPulse Run");
        terminal.show();
        terminal.sendText(`devpulse run "${uri.fsPath}"`);
    });

    context.subscriptions.push(runDisposable);

    let setApiKeyDisposable = vscode.commands.registerCommand("devpulse.setApiKey", async function () {
        const apiKey = await vscode.window.showInputBox({
            prompt: "Enter your Gemini API Key",
            ignoreFocusOut: true,
            password: false,
            placeHolder: "GOOGLE_API_KEY=your_gemini_api_key_here"
        });

        if (!apiKey) {
            vscode.window.showWarningMessage("DevPulse: No API key entered.");
            return;
        }

        // Find the workspace root
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders || workspaceFolders.length === 0) {
            vscode.window.showErrorMessage("DevPulse: No workspace folder open.");
            return;
        }
        const envPath = path.join(workspaceFolders[0].uri.fsPath, ".env");

        // Write or update the .env file
        let content = "";
        if (fs.existsSync(envPath)) {
            content = fs.readFileSync(envPath, "utf8");
            // Remove any existing GOOGLE_API_KEY line
            content = content.replace(/^GOOGLE_API_KEY=.*$/m, "");
            content = content.trim() + "\n";
        }
        content += `GOOGLE_API_KEY=${apiKey}\n`;
        fs.writeFileSync(envPath, content, "utf8");

        vscode.window.showInformationMessage("DevPulse: API key saved to .env!");
    });

    context.subscriptions.push(setApiKeyDisposable);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
