from colored_print.core.utils import is_colors_allowed
from colored_print.core.colors import Color
import operator


def c_print(color: str, text: str) -> None:
    if is_colors_allowed() and hasattr(Color, color.upper()):
        _color = getattr(Color, color.upper())
    else:
        _color = '' 
    print('%s%s%s' % (_color, text, Color.END)) 
