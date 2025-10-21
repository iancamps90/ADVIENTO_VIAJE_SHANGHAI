import reflex as rx


def header_text(icon: str, text: str, dark=True) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                class_name=f"nes-icon is-medium {icon} golden-glow"
            ),
            rx.heading(
                text,
                size="6",
                color="#DC143C" if dark else "#666",
                class_name="chinese-text text-center",
                text_align="center"
            ),
            spacing="3",
            align="center",
            justify="center",
            width="100%"
        ),
        class_name="container text-center mb-4",
        width="100%"
    )
