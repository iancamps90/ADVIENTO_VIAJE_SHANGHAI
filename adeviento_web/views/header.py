import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, TextColor
from adeviento_web.components.button import button


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Calendario de Adviento Shanghai 2025",
            size=rx.breakpoints(
                initial="6",
                xs="7", 
                sm="8",
                md="9",
                lg="9",
                xl="9"
            ),
            padding_bottom=Size.DEFAULT.value,
            class_name="chinese-text golden-glow"
        ),
        rx.box(
            # Contenedor con overlay para el texto
            rx.vstack(
                # Imagen de fondo que ocupa todo
                rx.image(
                    src="/nosotros.png",
                    alt="Grupo de amigos preparando el viaje a Shanghai.",
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    position="absolute",
                    top="0",
                    left="0",
                    z_index="1"
                ),
                # Overlay oscuro para legibilidad
                rx.box(
                    width="100%",
                    height="100%",
                    background="linear-gradient(135deg, rgba(0,0,0,0.7), rgba(0,0,0,0.5))",
                    position="absolute",
                    top="0",
                    left="0",
                    z_index="2"
                ),
                # Contenido de texto encima
                rx.vstack(
                    rx.text(
                        "¡Un calendario de adviento personalizado para nuestro viaje a Shanghai!",
                        font_size=rx.breakpoints(
                            initial="1.2em",
                            xs="1.3em", 
                            sm="1.4em",
                            md="1.5em",
                            lg="1.6em",
                            xl="1.6em"
                        ),
                        color="white",
                        font_weight="bold",
                        text_shadow="3px 3px 6px rgba(0,0,0,0.9)",
                        text_align="center"
                    ),
                    rx.text(
                        "Cada día una nueva sorpresa para calentar el viaje",
                        font_size=rx.breakpoints(
                            initial="1em",
                            xs="1.1em", 
                            sm="1.2em",
                            md="1.3em",
                            lg="1.4em",
                            xl="1.4em"
                    ),
                        color="white",
                        text_shadow="3px 3px 6px rgba(0,0,0,0.9)",
                        text_align="center"
                    ),
                    rx.text(
                        "¡Prepárate para la aventura más épica de fin de año!",
                        font_size=rx.breakpoints(
                            initial="1em",
                            xs="1.1em", 
                            sm="1.2em",
                            md="1.3em",
                            lg="1.4em",
                            xl="1.4em"
                        ),
                        color="white",
                        font_weight="bold",
                        text_shadow="3px 3px 6px rgba(0,0,0,0.9)",
                        text_align="center"
                    ),
                    rx.link(
                        "#ShanghaiNosEspera25",
                        href="https://instagram.com/iaancamps90",
                        external=True,
                        color="#FFD700",
                        text_shadow="4px 4px 8px rgba(0,0,0,1)",
                        font_weight="bold",
                        font_size=rx.breakpoints(
                            initial="1.3em",
                            xs="1.4em", 
                            sm="1.5em",
                            md="1.6em",
                            lg="1.7em",
                            xl="1.7em"
                        ),
                        text_align="center",
                        background="rgba(0,0,0,0.7)",
                        padding="0.5em 1em",
                        border_radius="25px",
                        border="2px solid #FFD700",
                        _hover={
                            "background": "rgba(255,215,0,0.2)",
                            "color": "#FFFFFF",
                            "transform": "scale(1.05)"
                        }
                    ),
                    align="center",
                    spacing="3",
                    justify="center",
                    height="100%",
                    width="100%",
                    position="relative",
                    z_index="3"
                ),
                position="relative",
                height="400px",
                width="100%",
                overflow="hidden"
            ),
            width="100%"
        ),
            padding_top=Size.VERY_BIG.value,
            style=styles.max_width_style,
            background_image="url('/culture_images/templo1.jpg')",
            background_size="cover",
            background_position="center",
            background_repeat="no-repeat",
            border_radius="12px",
            border=f"2px solid {TextColor.TERTIARY.value}"
        )
