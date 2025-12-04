import reflex as rx
import datetime
from adeviento_web.styles.colors import TextColor, Color
from adeviento_web.styles.styles import Size

def get_shanghai_time() -> str:
    """Obtiene la hora actual en Shanghai (UTC+8)"""
    utc_now = datetime.datetime.utcnow()
    shanghai_time = utc_now + datetime.timedelta(hours=8)
    return shanghai_time.strftime("%H:%M")

def shanghai_info() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("🇨🇳 SHANGHAI", font_size="0.6em", font_weight="bold", color=TextColor.ACCENT.value),
            rx.text(get_shanghai_time(), font_size="1em", font_weight="bold", color="#FFF"),
            spacing="0",
            align="center"
        ),
        padding="8px",
        background="rgba(0,0,0,0.5)",
        border_radius="8px",
        border=f"1px solid {Color.SECONDARY.value}",
        display={
            "initial": "none",
            "sm": "block"
        }
    )

