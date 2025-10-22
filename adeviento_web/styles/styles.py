import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH = "1000px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "4em"


STYLESHEETS = [
    "css/main.css",
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.SECONDARY.value,
    "background": f"linear-gradient(135deg, {Color.BACKGROUND.value} 0%, {Color.PRIMARY.value} 100%)",
    "min_height": "100vh",
    rx.heading: {
        "font_family": Font.DEFAULT.value,
        "color": TextColor.ACCENT.value,
        "text_shadow": f"2px 2px 4px {Color.QUATERNARY.value}"
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none",
            "transform": "scale(1.05)"
        }
    },
    rx.el.span: {
        "font_size": Size.MEDIUM.value
    },
    rx.button: {
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BUTTON.value,
        "color": f"{TextColor.SECONDARY.value} !important",
        "background": f"linear-gradient(45deg, {Color.ACCENT.value}, {Color.SECONDARY.value})",
        "border": f"2px solid {Color.SECONDARY.value}",
        "border_radius": "8px",
        "_hover": {
            "color": f"{TextColor.PRIMARY.value} !important",
            "transform": "translateY(-2px)",
            "box_shadow": f"0 4px 8px {Color.QUATERNARY.value}"
        }
    }
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)
