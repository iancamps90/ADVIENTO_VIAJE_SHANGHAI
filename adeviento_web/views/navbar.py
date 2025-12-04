import reflex as rx
import adeviento_web.constants as constants
from adeviento_web.styles.styles import Size, Color
from adeviento_web.components.link_icon import link_icon


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="/culture_images/animalchino2025.jpg",
                alt="Año del Dragón 2025",
                width="5em",
                height="3em",
                border_radius="8px",
                object_fit="cover"
            ),
            rx.text(
                "Calendario de Adviento Shanghai 2025 🇨🇳🏮🎁❄️🎊",
                font_size="1rem",
                font_weight="bold",
                color="white"
            ),
            rx.spacer(),
            link_icon(
                "instagram",
                constants.INSTAGRAM_URL
            ),
            link_icon(
                "github",
                constants.GITHUB_URL
            ),
            align="center",
            width="100%"
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )
