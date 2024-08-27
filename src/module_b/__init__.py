import importhook
import inspect
import sys
from pathlib import Path

from src.module_b.functions import do_thing


WHITELIST = {"src.module_a"}


@importhook.on_import("src.module_b")
def on_module_b_import(module_b):
    stack = inspect.stack()

    this_frame_index = len(stack) - 1
    for frame in reversed(stack):
        if frame.filename == __file__:
            break
        this_frame_index -= 1

    current_index = this_frame_index + 1
    while True:
        if "frozen importlib" in stack[current_index].filename:
            current_index += 1
        else:
            break

    project_path = Path(sys.path[0])  # assumes entrypoint is always prepended
    caller_file = Path(stack[current_index].filename)
    caller_module = str(caller_file.relative_to(project_path)).replace("/", ".").replace(".py", "")
    print(f"caller: {caller_module}")

    if caller_module not in WHITELIST:
        raise ImportError(f"Module '{caller_module}' is not allowed to import '{module_b.__name__}'")

    print(module_b)
    print("module_b has been imported")
