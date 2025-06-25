import subprocess
import re
from .helper import explain_error

def start_watcher(path):
    print(f"[DevPulse] Watching for errors in: {path}")
    process = subprocess.Popen(f"python {path}", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    while True:
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        if output:
            print(output, end="")

        error_output = process.stderr.readline()
        if error_output:
            print(f"\n[DevPulse detected error]\n{error_output}")
            print("[DevPulse AI Explanation]:")
            print(explain_error(error_output))