import reflex as rx
import adeviento_web.constants as constants
from adeviento_web.styles.styles import Size


def github() -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.vstack(
                rx.el.span(
                    "Calendario"
                ),
                rx.el.span(
                    "de Shanghai"
                ),
                align_items="start",
                class_name="nes-balloon from-right is-dark",
                margin_bottom=Size.BIG.value
            ),
            rx.box(
                rx.el.span(
                    "2025",
                    class_name="is-error"
                ),
                class_name="nes-badge"
            )
        ),
        rx.box(
            class_name="nes-octocat animate"
        ),
        href=constants.GITHUB_REPO_URL,
        external=True,
        align_items="end",
        display="flex",
        margin_top=Size.ZERO.value
    )
