import sys


def is_colors_allowed() -> bool:
    system = sys.platform
    if system.lower().startswith(('win')):
        return False
    else:
        return True
