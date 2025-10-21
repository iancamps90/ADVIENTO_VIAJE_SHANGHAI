import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, Color
from adeviento_web.components.header_text import header_text


def partners() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text(
                "star",
                "Información del Viaje",
                False
            ),
            rx.vstack(
                rx.text(
                    "Del 25 de diciembre de 2025 al 3 de enero de 2026",
                    font_size=Size.MEDIUM.value,
                    color=styles.TextColor.SECONDARY.value,
                    text_align="center"
                ),
                rx.text(
                    "Shanghai, China - La ciudad más poblada del mundo",
                    font_size=Size.MEDIUM.value,
                    color=styles.TextColor.SECONDARY.value,
                    text_align="center"
                ),
                rx.text(
                    "5 amigos - ¡La aventura más épica!",
                    font_size=Size.MEDIUM.value,
                    color=styles.TextColor.SECONDARY.value,
                    text_align="center"
                ),
                align="center",
                spacing="2"
            ),
            padding_y=Size.VERY_BIG.value,
            style=styles.max_width_style
        ),
        bg=Color.ACCENT.value,
        align="center",
        width="100%"
    )


def _partner_link(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width="100%",
            height="100%",
            alt=alt
        ),
        href=url,
        external=True
    )
