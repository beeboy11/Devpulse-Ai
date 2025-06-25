import sys
import traceback

try:
    from devpulse.helper import explain_error
except ImportError:
    def explain_error(msg): return "[DevPulse unavailable]"

def excepthook(type, value, tb):

    traceback.print_exception(type, value, tb)
    if type not in (KeyboardInterrupt, SystemExit):
        last_line = "".join(traceback.format_exception_only(type, value)).strip()
        print("\n[DevPulse AI Explanation]:")
        print(explain_error(last_line))

sys.excepthook = excepthook