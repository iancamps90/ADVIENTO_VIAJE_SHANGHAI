import reflex as rx
import datetime
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, Color, TextColor
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button


def author() -> rx.Component:
    return rx.vstack(
        header_text(
            "like",
            "¡Hola! Somos 5 amigos"
        ),
        rx.flex(
            rx.image(
                src="/nosotros.png",
                width="128px",
                height="128px",
                bg=Color.PRIMARY.value,
                padding="2px",
                border=f"4px solid {Color.SECONDARY.value}",
                border_radius="50%",
                margin_right=Size.SMALL.value,
                margin_bottom=Size.SMALL.value
            ),
            rx.vstack(
                rx.el.span(
                    "Somos 5 amigos preparando la aventura más épica del año."
                ),
                rx.el.span(
                    "Todos listos para descubrir Shanghai y vivir una experiencia inolvidable juntos."
                ),
                rx.el.span(
                    "¡Cada día nos acerca más a la aventura de nuestras vidas!"
                ),
                _author_buttons(),
                width="100%",
                align_items="start"
            ),
            align_items="start",
            spacing="4",
            flex_direction=styles.FLEX_DIRECTION
        ),
        style=styles.max_width_style
    )


def _author_buttons() -> rx.Component:
    return rx.flex(
        button(
            "Ver Fotos del Viaje",
            constants.INSTAGRAM_URL
        ),
        button(
            "Seguir la Aventura",
            constants.TWITTER_URL
        ),
        button(
            "Código del Proyecto",
            constants.GITHUB_URL
        ),
        align_items="start",
        flex_direction=styles.FLEX_DIRECTION
    )


def _experience() -> int:
    return datetime.date.today().year - 2010
