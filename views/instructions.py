import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import TextColor
from adeviento_web.components.button import button


def instructions() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "¿Cómo funciona nuestro Shanghai Advent Journey? 🏮",
                class_name="title chinese-text",
                color=TextColor.ACCENT.value
            ),
            rx.el.span(
                "• Del 1 al 25 de diciembre descubrirás cada día una nueva sorpresa para calentar el viaje."
            ),
            rx.el.span(
                "• Cada día tendrás: frases motivacionales, recomendaciones de viaje, recordatorios importantes y tips útiles."
            ),
            rx.el.span(
                "• Haz clic en cada día del calendario para ver la sorpresa completa y compartirla con el grupo."
            ),
            button(
                "Compartir en WhatsApp",
                "https://wa.me/?text=Mira+la+sorpresa+del+día+1+https://shanghai-advent.vercel.app/day/1"
            ),
            rx.el.span(
                "• ¡Cada día nos acerca más a la aventura más épica del año en Shanghai!"
            ),
            rx.el.span(
                "• ¡No te pierdas ni un día! ¡Cada sorpresa está diseñada para hacer que el viaje sea aún más especial!"
            ),
            class_name="nes-container is-dark with-title chinese-card",
            align_items="start",
            width="100%"
        ),
        style=styles.max_width_style
    )
