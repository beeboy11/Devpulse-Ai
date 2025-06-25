import argparse
import sys
import traceback

from devpulse.helper import explain_error, explain_command

def main():
    parser = argparse.ArgumentParser(
        description="DevPulse AI - Error & Terminal Command Explainer"
    )
    subparsers = parser.add_subparsers(dest="mode", help="Mode of operation")

    # Explain subcommand
    explain_parser = subparsers.add_parser(
        "explain", help="Explain an error message or terminal command"
    )
    explain_parser.add_argument(
        "--text", type=str, required=True, help="Error message or command to explain"
    )
    explain_parser.add_argument(
        "--type",
        type=str,
        choices=["error", "command"],
        required=True,
        help="Type of input",
    )

    # Run subcommand
    run_parser = subparsers.add_parser(
        "run", help="Run a Python script and explain errors if they occur"
    )
    run_parser.add_argument(
        "script", type=str, help="Python script to run"
    )
    run_parser.add_argument(
        "script_args", nargs=argparse.REMAINDER, help="Arguments to pass to the script"
    )

    args = parser.parse_args()

    if not args.mode:
        parser.print_help()
        sys.exit(1)

    try:
        if args.mode == "explain":
            if args.type == "error":
                print(explain_error(args.text))
            elif args.type == "command":
                print(explain_command(args.text))
        elif args.mode == "run":
            sys.argv = [args.script] + args.script_args
            try:
                with open(args.script, "rb") as f:
                    code = compile(f.read(), args.script, 'exec')
                    exec(code, {"__name__": "__main__"})
            except Exception:
                tb = traceback.format_exc()
                print(tb, end="")  # Print the original traceback
                last_line = tb.strip().splitlines()[-1]
                print("\n[DevPulse AI Explanation]:")
                print(explain_error(last_line))
    except Exception as exc:
        print(f"An error occurred: {exc}")
        sys.exit(1)

if __name__ == "__main__":
    main()
