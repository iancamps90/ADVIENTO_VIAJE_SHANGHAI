import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, TextColor


def footer() -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.vstack(
                rx.text(
                    "Calendario de Adviento Shanghai 2025",
                    font_size=Size.MEDIUM.value,
                    margin_bottom=Size.ZERO.value,
                    class_name="chinese-text"
                ),
                rx.text(
                    "Creado con ",
                    rx.el.i(class_name="nes-icon is-small heart"),
                    " para nuestro viaje épico a Shanghai",
                    font_size=Size.MEDIUM.value,
                    color=TextColor.TERTIARY.value
                ),
                rx.text(
                    "Del 25 de diciembre de 2025 al 3 de enero de 2026 - ¡La aventura nos espera!",
                    font_size=Size.SMALL.value,
                    color=TextColor.QUATERNARY.value
                ),
                align_items="start",
                spacing="3"
            ),
            rx.spacer(),
            rx.image(
                src="gift.png",
                alt="Regalo del viaje a Shanghai",
                class_name="nes-avatar is-large lantern"
            ),
            width="100%"
        ),
        padding_bottom=Size.BIG.value,
        style=styles.max_width_style
    )
