import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import TextColor, Color
from adeviento_web.components.button import button
from adeviento_web.views.calendar import (
    _shanghai_days, _shanghai_day_name, _shanghai_day_message, _shanghai_day_url,
    _shanghai_day_motivation, _shanghai_day_recommendations, _shanghai_day_video, _shanghai_day_photo
)


def day_detail(day_number: int) -> rx.Component:
    """Vista detallada para cada día del calendario de Shanghai"""
    
    # Obtener el contenido del día (day_number - 1 porque el array es 0-indexed)
    day_index = day_number - 1
    
    if day_index < 0 or day_index >= len(_shanghai_days):
        return rx.vstack(
            rx.heading("Día no encontrado", size="6"),
            rx.text("Este día no existe en nuestro calendario de Shanghai."),
            rx.link(
                button("Volver al calendario", ""),
                href="/",
                external=False
            ),
            align="center",
            spacing="4",
            style=styles.max_width_style
        )
    
    day_name = _shanghai_day_name(day_index)
    day_message = _shanghai_day_message(day_index)
    day_motivation = _shanghai_day_motivation(day_index)
    day_recommendations = _shanghai_day_recommendations(day_index)
    day_video = _shanghai_day_video(day_index)
    day_photo = _shanghai_day_photo(day_index)
    
    return rx.vstack(
        # Header con el número del día
        rx.box(
            rx.heading(
                f"Día {day_number}",
                size="8",
                color=TextColor.ACCENT.value,
                class_name="chinese-text golden-glow"
            ),
            rx.text(
                "Calendario de Adviento Shanghai 2025",
                font_size=Size.MEDIUM.value,
                color=TextColor.TERTIARY.value
            ),
            align="center",
            padding=Size.BIG.value,
            background=f"linear-gradient(135deg, {Color.BACKGROUND.value}, {Color.SECONDARY.value})",
            border_radius="12px",
            border=f"2px solid {Color.SECONDARY.value}",
            width="100%"
        ),
        
        # Contenido principal del día
        rx.box(
            rx.vstack(
                rx.heading(
                    day_name,
                    size="6",
                    color=TextColor.SECONDARY.value,
                    text_align="center",
                    margin_bottom=Size.BIG.value
                ),
                
                # Foto del día
                rx.cond(
                    day_photo != "",
                    rx.image(
                        src=day_photo,
                        alt=f"Foto del día {day_number}",
                        width="100%",
                        max_width="400px",
                        border_radius="8px",
                        margin_bottom=Size.BIG.value
                    )
                ),
                
                rx.text(
                    day_message,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.SECONDARY.value,
                    text_align="center",
                    line_height="1.6",
                    margin_bottom=Size.BIG.value
                ),
                
                # Frase motivacional
                rx.cond(
                    day_motivation != "",
                    rx.box(
                        rx.text(
                            f'"{day_motivation}"',
                            font_style="italic",
                            font_size=Size.MEDIUM.value,
                            color=TextColor.ACCENT.value,
                            text_align="center",
                            padding=Size.BIG.value,
                            background=Color.BACKGROUND.value,
                            border_radius="8px",
                            border=f"2px solid {Color.SECONDARY.value}"
                        ),
                        width="100%",
                        margin_bottom=Size.BIG.value
                    )
                ),
                
                # Recomendaciones
                rx.cond(
                    day_recommendations != "",
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "📋 Recomendaciones del día:",
                                font_weight="bold",
                                color=TextColor.ACCENT.value,
                                font_size=Size.MEDIUM.value
                            ),
                            rx.text(
                                day_recommendations,
                                color=TextColor.SECONDARY.value,
                                white_space="pre-line",
                                text_align="left"
                            ),
                            align="start",
                            spacing="2"
                        ),
                        padding=Size.BIG.value,
                        background=Color.BACKGROUND.value,
                        border_radius="8px",
                        border=f"2px solid {Color.SECONDARY.value}",
                        width="100%",
                        margin_bottom=Size.BIG.value
                    )
                ),
                
                # Video de YouTube
                rx.cond(
                    day_video != "",
                    rx.box(
                        rx.vstack(
                            rx.text(
                                "🎥 Video del día:",
                                font_weight="bold",
                                color=TextColor.ACCENT.value,
                                font_size=Size.MEDIUM.value
                            ),
                            rx.el.iframe(
                                src=day_video,
                                width="100%",
                                height="200px",
                                border_radius="8px"
                            ),
                            align="center",
                            spacing="2"
                        ),
                        padding=Size.BIG.value,
                        background=Color.BACKGROUND.value,
                        border_radius="8px",
                        border=f"2px solid {Color.SECONDARY.value}",
                        width="100%",
                        margin_bottom=Size.BIG.value
                    )
                ),
                
                # Botones de acción
                rx.hstack(
                    rx.link(
                        button(
                            "Volver al calendario",
                            ""
                        ),
                        href="/",
                        external=False
                    ),
                    rx.link(
                        button(
                            "Ver día anterior",
                            ""
                        ),
                        href=f"/day/{day_number - 1}" if day_number > 1 else "/",
                        external=False
                    ),
                    rx.link(
                        button(
                            "Ver día siguiente",
                            ""
                        ),
                        href=f"/day/{day_number + 1}" if day_number < 25 else "/",
                        external=False
                    ),
                    spacing="3",
                    justify="center",
                    flex_wrap="wrap"
                ),
                
                align="center",
                spacing="3"
            ),
            padding=Size.VERY_BIG.value,
            background=f"linear-gradient(135deg, {Color.PRIMARY.value}, {Color.QUATERNARY.value})",
            border_radius="12px",
            border=f"2px solid {Color.ACCENT.value}",
            box_shadow=f"0 8px 16px {Color.QUATERNARY.value}",
            width="100%",
            class_name="chinese-card fade-in"
        ),
        
        # Información adicional
        rx.box(
            rx.vstack(
                rx.text(
                    "💡 Tip del día:",
                    font_weight="bold",
                    color=TextColor.ACCENT.value
                ),
                rx.text(
                    _get_day_tip(day_number),
                    color=TextColor.TERTIARY.value,
                    text_align="center"
                ),
                align="center",
                spacing="2"
            ),
            padding=Size.BIG.value,
            background=Color.BACKGROUND.value,
            border_radius="8px",
            border=f"1px solid {Color.SECONDARY.value}",
            width="100%"
        ),
        
        align="center",
        spacing="4",
        style=styles.max_width_style,
        padding=Size.BIG.value
    )


def _get_day_tip(day_number: int) -> str:
    """Obtiene un tip específico para cada día"""
    tips = {
        1: "¡Empieza a hacer una lista de todo lo que quieres hacer en Shanghai!",
        2: "Revisa el clima de Shanghai para saber qué ropa llevar.",
        3: "¡Descarga Duolingo y aprende algunas frases básicas en chino!",
        4: "Haz una copia de seguridad de todos tus documentos importantes.",
        5: "¡Investiga sobre la historia de Shanghai para apreciar más la ciudad!",
        6: "Crea una playlist especial para el viaje.",
        7: "¡Busca restaurantes locales auténticos en Shanghai!",
        8: "Planifica qué lugares quieres visitar cada día.",
        9: "¡Aprende sobre las tradiciones navideñas en China!",
        10: "Revisa que tu seguro de viaje esté al día.",
        11: "¡Practica cómo pedir comida en chino!",
        12: "Prepara tu cámara y asegúrate de tener suficiente espacio.",
        13: "¡Investiga sobre las mejores zonas para comprar en Shanghai!",
        14: "Descarga apps útiles como Google Translate y Maps.",
        15: "¡Ya estamos a mitad del camino! ¡Mantén la emoción!",
        16: "Prepara regalos pequeños para intercambiar con el grupo.",
        17: "¡Planifica cómo celebrar el Año Nuevo en Shanghai!",
        18: "¡Crea un hashtag especial para vuestras fotos del viaje!",
        19: "Escribe en un diario tus expectativas para el viaje.",
        20: "¡Última semana! ¡Revisa que tengas todo listo!",
        21: "¡Prepara tu mente para la aventura más épica!",
        22: "¡Solo quedan 3 días! ¡La emoción está al máximo!",
        23: "¡Última noche en casa! ¡Disfruta y descansa bien!",
        24: "¡HOY ES EL DÍA! ¡Que empiece la aventura!",
        25: "¡FELIZ NAVIDAD EN SHANGHAI! ¡Disfruta cada momento!"
    }
    return tips.get(day_number, "¡Disfruta cada momento de esta aventura épica!")
