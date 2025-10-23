import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import TextColor, Color
from adeviento_web.components.button import button
from adeviento_web.components.photo_carousel import photo_carousel
from adeviento_web.components.special_effects import celebration_banner, progress_bar
from adeviento_web.views.calendar import (
    _shanghai_days, _shanghai_day_name, _shanghai_day_message, _shanghai_day_url,
    _shanghai_day_motivation, _shanghai_day_recommendations, _shanghai_day_video, _shanghai_day_photo,
    _is_day_available
)


def _parse_day_content(content: str) -> dict:
    """Parsea el contenido del día y lo separa en secciones"""
    sections = {
        'intro': '',
        'challenge': '',
        'preparations': '',
        'tip': '',
        'progress': '',
        'video': '',
        'extra': ''
    }
    
    lines = content.split('\n')
    current_section = 'intro'
    current_content = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if '🎯 **RETO DEL DÍA:**' in line or '**🎯 RETO DEL DÍA:**' in line:
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = 'challenge'
            current_content = [line.replace('**🎯 RETO DEL DÍA:**', '').replace('🎯 **RETO DEL DÍA:**', '').strip()]
        elif '🧳 **Preparativos' in line:
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = 'preparations'
            current_content = [line.replace('🧳 **Preparativos de maleta:**', '').strip()]
        elif '💡 **Tip del día:**' in line:
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = 'tip'
            current_content = [line.replace('💡 **Tip del día:**', '').strip()]
        elif '🏮 **Progreso del viaje:**' in line:
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = 'progress'
            current_content = [line.replace('🏮 **Progreso del viaje:**', '').strip()]
        elif '🎥 **Video del día:**' in line:
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = 'video'
            current_content = [line.replace('🎥 **Video del día:**', '').strip()]
        elif '🧧 **Extra para el grupo:**' in line:
            if current_content:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = 'extra'
            current_content = [line.replace('🧧 **Extra para el grupo:**', '').strip()]
        else:
            current_content.append(line)
    
    # Guardar la última sección
    if current_content:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections


def _render_day_sections(content: str) -> rx.Component:
    """Renderiza el contenido del día en secciones visuales separadas"""
    sections = _parse_day_content(content)
    
    components = []
    
    # Introducción
    if sections['intro']:
        components.append(
            rx.box(
                rx.text(
                    sections['intro'],
                    font_size=rx.breakpoints(
                        initial="1em",
                        xs="1.1em", 
                        sm="1.2em",
                        md="1.3em",
                        lg="1.3em",
                        xl="1.3em"
                    ),
                    color="#FFFFFF",
                    text_align="center",
                    line_height="1.6",
                    text_shadow="2px 2px 4px rgba(0,0,0,0.8)"
                ),
                padding=Size.BIG.value,
                background="rgba(0,0,0,0.6)",
                border_radius="12px",
                border=f"2px solid {Color.SECONDARY.value}",
                width="100%",
                margin_bottom=Size.BIG.value
            )
        )
    
    # Reto del día
    if sections['challenge']:
        components.append(
            rx.box(
                rx.vstack(
                    rx.text(
                        "🎯 RETO DEL DÍA",
                        font_size=rx.breakpoints(
                            initial="1.2em",
                            xs="1.3em", 
                            sm="1.4em",
                            md="1.5em",
                            lg="1.5em",
                            xl="1.5em"
                        ),
                        font_weight="bold",
                        color="#FFD700",
                        text_shadow="2px 2px 4px rgba(0,0,0,0.8)"
                    ),
                    rx.text(
                        sections['challenge'],
                        font_size=rx.breakpoints(
                            initial="0.9em",
                            xs="1em", 
                            sm="1.1em",
                            md="1.2em",
                            lg="1.2em",
                            xl="1.2em"
                        ),
                        color="#FFFFFF",
                        text_align="center",
                        line_height="1.6",
                        text_shadow="1px 1px 2px rgba(0,0,0,0.8)"
                    ),
                    align="center",
                    spacing="2"
                ),
                padding=Size.BIG.value,
                background="rgba(220, 20, 60, 0.3)",
                border_radius="12px",
                border=f"2px solid #DC143C",
                width="100%",
                margin_bottom=Size.BIG.value
            )
        )
    
    # Preparativos de maleta
    if sections['preparations']:
        components.append(
            rx.box(
                rx.vstack(
                    rx.text(
                        "🧳 PREPARATIVOS DE MALETA",
                        font_size=rx.breakpoints(
                            initial="1.1em",
                            xs="1.2em", 
                            sm="1.3em",
                            md="1.4em",
                            lg="1.4em",
                            xl="1.4em"
                        ),
                        font_weight="bold",
                        color="#FFD700",
                        text_shadow="2px 2px 4px rgba(0,0,0,0.8)"
                    ),
                    rx.text(
                        sections['preparations'],
                        font_size=rx.breakpoints(
                            initial="0.9em",
                            xs="1em", 
                            sm="1.1em",
                            md="1.2em",
                            lg="1.2em",
                            xl="1.2em"
                        ),
                        color="#FFFFFF",
                        text_align="left",
                        line_height="1.6",
                        text_shadow="1px 1px 2px rgba(0,0,0,0.8)"
                    ),
                    align="center",
                    spacing="2"
                ),
                padding=Size.BIG.value,
                background="rgba(0,0,0,0.6)",
                border_radius="12px",
                border=f"2px solid {Color.SECONDARY.value}",
                width="100%",
                margin_bottom=Size.BIG.value
            )
        )
    
    # Progreso del viaje - ELIMINADO (redundante con barra de progreso)
    
    # Video del día
    if sections['video']:
        components.append(
            rx.box(
                rx.vstack(
                    rx.text(
                        "🎥 VIDEO DEL DÍA",
                        font_size=rx.breakpoints(
                            initial="1.1em",
                            xs="1.2em", 
                            sm="1.3em",
                            md="1.4em",
                            lg="1.4em",
                            xl="1.4em"
                        ),
                        font_weight="bold",
                        color="#FFD700",
                        text_shadow="2px 2px 4px rgba(0,0,0,0.8)"
                    ),
                    rx.text(
                        sections['video'],
                        font_size=rx.breakpoints(
                            initial="0.9em",
                            xs="1em", 
                            sm="1.1em",
                            md="1.2em",
                            lg="1.2em",
                            xl="1.2em"
                        ),
                        color="#FFFFFF",
                        text_align="center",
                        line_height="1.6",
                        text_shadow="1px 1px 2px rgba(0,0,0,0.8)"
                    ),
                    align="center",
                    spacing="2"
                ),
                padding=Size.BIG.value,
                background="rgba(0,0,0,0.6)",
                border_radius="12px",
                border=f"2px solid {Color.SECONDARY.value}",
                width="100%",
                margin_bottom=Size.BIG.value
            )
        )
    
    # Extra para el grupo
    if sections['extra']:
        components.append(
            rx.box(
                rx.vstack(
                    rx.text(
                        "🧧 EXTRA PARA EL GRUPO",
                        font_size=rx.breakpoints(
                            initial="1.1em",
                            xs="1.2em", 
                            sm="1.3em",
                            md="1.4em",
                            lg="1.4em",
                            xl="1.4em"
                        ),
                        font_weight="bold",
                        color="#FFD700",
                        text_shadow="2px 2px 4px rgba(0,0,0,0.8)"
                    ),
                    rx.text(
                        sections['extra'],
                        font_size=rx.breakpoints(
                            initial="0.9em",
                            xs="1em", 
                            sm="1.1em",
                            md="1.2em",
                            lg="1.2em",
                            xl="1.2em"
                        ),
                        color="#FFFFFF",
                        text_align="center",
                        line_height="1.6",
                        text_shadow="1px 1px 2px rgba(0,0,0,0.8)"
                    ),
                    align="center",
                    spacing="2"
                ),
                padding=Size.BIG.value,
                background="rgba(0,0,0,0.6)",
                border_radius="12px",
                border=f"2px solid {Color.SECONDARY.value}",
                width="100%",
                margin_bottom=Size.BIG.value
            )
        )
    
    return rx.vstack(*components, spacing="3", width="100%")


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
        # Banner de celebración para días especiales
        celebration_banner(day_number),
        
        # Barra de progreso
        progress_bar(day_number),
        
        # Header con el número del día
        rx.box(
            rx.heading(
                f"Día {day_number}",
                size=rx.breakpoints(
                    initial="6",
                    xs="7", 
                    sm="8",
                    md="8",
                    lg="8",
                    xl="8"
                ),
                color=TextColor.ACCENT.value,
                class_name="chinese-text golden-glow"
            ),
            rx.text(
                "Calendario de Adviento Shanghai 2025",
                font_size=rx.breakpoints(
                    initial="0.8em",
                    xs="0.9em", 
                    sm="1em",
                    md="1.1em",
                    lg="1.1em",
                    xl="1.1em"
                ),
                color="#FFFFFF",
                text_shadow="1px 1px 2px rgba(0,0,0,0.8)"
            ),
            align="center",
            padding=rx.breakpoints(
                initial="1em",
                xs="1.5em", 
                sm="2em",
                md="2em",
                lg="2em",
                xl="2em"
            ),
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
                    size=rx.breakpoints(
                        initial="4",
                        xs="5", 
                        sm="6",
                        md="6",
                        lg="6",
                        xl="6"
                    ),
                    color="#FFFFFF",
                    text_align="center",
                    margin_bottom=Size.BIG.value,
                    text_shadow="2px 2px 4px rgba(0,0,0,0.8)"
                ),
                
                # Carrusel de fotos del día
                rx.cond(
                    day_photo != "",
                    photo_carousel(
                        photos=_get_day_photos(day_number),
                        interval=7000  # Cambia cada 7 segundos
                    )
                ),
                
                # Contenido separado en secciones
                _render_day_sections(day_message),
                
                # Tip del día (movido más arriba)
                rx.box(
                    rx.vstack(
                        rx.text(
                            "💡 Tip del día:",
                            font_weight="bold",
                            color=TextColor.ACCENT.value
                        ),
                        rx.text(
                            _get_day_tip(day_number),
                            color="#FFFFFF",
                            text_align="center",
                            text_shadow="1px 1px 2px rgba(0,0,0,0.8)"
                        ),
                        align="center",
                        spacing="2"
                    ),
                    padding=Size.BIG.value,
                    background="rgba(0,0,0,0.8)",
                    border_radius="8px",
                    border=f"1px solid {Color.SECONDARY.value}",
                    width="100%",
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
                                color="#FFFFFF",
                                white_space="pre-line",
                                text_align="left",
                                text_shadow="1px 1px 2px rgba(0,0,0,0.8)"
                            ),
                            align="start",
                            spacing="2"
                        ),
                        padding=Size.BIG.value,
                        background="rgba(0,0,0,0.8)",
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
                                height=rx.breakpoints(
                                    initial="180px",
                                    xs="200px", 
                                    sm="220px",
                                    md="250px",
                                    lg="280px",
                                    xl="300px"
                                ),
                                border_radius="8px",
                                max_width="560px"
                            ),
                            align="center",
                            spacing="2"
                        ),
                        padding=Size.BIG.value,
                        background="rgba(0,0,0,0.8)",
                        border_radius="8px",
                        border=f"2px solid {Color.SECONDARY.value}",
                        width="100%",
                        margin_bottom=Size.BIG.value
                    )
                ),
                
                # Botones de acción
                rx.link(
                    button(
                        "🏮 Volver al calendario",
                        ""
                    ),
                    href="/",
                    external=False
                ),
                
                align="center",
                spacing="3"
            ),
            padding=rx.breakpoints(
                initial="1em",
                xs="1.5em", 
                sm="2em",
                md="2.5em",
                lg="3em",
                xl="3em"
            ),
            background=f"linear-gradient(135deg, {Color.PRIMARY.value}, {Color.QUATERNARY.value})",
            border_radius="12px",
            border=f"2px solid {Color.ACCENT.value}",
            box_shadow=f"0 8px 16px {Color.QUATERNARY.value}",
            width="100%",
            max_width=rx.breakpoints(
                initial="95%",
                xs="90%", 
                sm="85%",
                md="900px",
                lg="1000px",
                xl="1100px"
            ),
            class_name="chinese-card fade-in"
        ),
        
        align="center",
        spacing=rx.breakpoints(
            initial="2",
            xs="3", 
            sm="4",
            md="4",
            lg="4",
            xl="4"
        ),
        style=styles.max_width_style,
        padding=rx.breakpoints(
            initial="0.5em",
            xs="1em", 
            sm="1.5em",
            md="2em",
            lg="2em",
            xl="2em"
        )
    )


def _get_day_photos(day_number: int) -> list[str]:
    """Obtiene múltiples fotos para el carrusel de cada día"""
    # Fotos base del calendario
    base_photos = [f"/calendar_enhanced/{day_number}.png"]
    
    # Fotos adicionales según el día - MÁS VARIEDAD
    extra_photos = {
        1: ["/calendar_enhanced/1.png", "/calendar_enhanced/2.png", "/calendar_enhanced/3.png", "/calendar_enhanced/4.png", "/calendar_enhanced/5.png"],
        2: ["/calendar_enhanced/2.png", "/calendar_enhanced/6.png", "/calendar_enhanced/7.png", "/calendar_enhanced/8.png", "/calendar_enhanced/9.png"],
        3: ["/calendar_enhanced/3.png", "/calendar_enhanced/10.png", "/calendar_enhanced/11.png", "/calendar_enhanced/12.png", "/calendar_enhanced/13.png"],
        4: ["/calendar_enhanced/4.png", "/calendar_enhanced/14.png", "/calendar_enhanced/15.png", "/calendar_enhanced/16.png", "/calendar_enhanced/17.png"],
        5: ["/calendar_enhanced/5.png", "/calendar_enhanced/18.png", "/calendar_enhanced/19.png", "/calendar_enhanced/20.png", "/calendar_enhanced/21.png"],
        6: ["/calendar_enhanced/6.png", "/calendar_enhanced/22.png", "/calendar_enhanced/23.png", "/calendar_enhanced/24.png", "/calendar_enhanced/25.png"],
        7: ["/calendar_enhanced/7.png", "/calendar_enhanced/1.png", "/calendar_enhanced/2.png", "/calendar_enhanced/3.png", "/calendar_enhanced/4.png"],
        8: ["/calendar_enhanced/8.png", "/calendar_enhanced/5.png", "/calendar_enhanced/6.png", "/calendar_enhanced/7.png", "/calendar_enhanced/8.png"],
        9: ["/calendar_enhanced/9.png", "/calendar_enhanced/9.png", "/calendar_enhanced/10.png", "/calendar_enhanced/11.png", "/calendar_enhanced/12.png"],
        10: ["/calendar_enhanced/10.png", "/calendar_enhanced/13.png", "/calendar_enhanced/14.png", "/calendar_enhanced/15.png", "/calendar_enhanced/16.png"],
        11: ["/calendar_enhanced/11.png", "/calendar_enhanced/17.png", "/calendar_enhanced/18.png", "/calendar_enhanced/19.png", "/calendar_enhanced/20.png"],
        12: ["/calendar_enhanced/12.png", "/calendar_enhanced/21.png", "/calendar_enhanced/22.png", "/calendar_enhanced/23.png", "/calendar_enhanced/24.png"],
        13: ["/calendar_enhanced/13.png", "/calendar_enhanced/25.png", "/calendar_enhanced/1.png", "/calendar_enhanced/2.png", "/calendar_enhanced/3.png"],
        14: ["/calendar_enhanced/14.png", "/calendar_enhanced/4.png", "/calendar_enhanced/5.png", "/calendar_enhanced/6.png", "/calendar_enhanced/7.png"],
        15: ["/calendar_enhanced/15.png", "/calendar_enhanced/8.png", "/calendar_enhanced/9.png", "/calendar_enhanced/10.png", "/calendar_enhanced/11.png"],
        16: ["/calendar_enhanced/16.png", "/calendar_enhanced/12.png", "/calendar_enhanced/13.png", "/calendar_enhanced/14.png", "/calendar_enhanced/15.png"],
        17: ["/calendar_enhanced/17.png", "/calendar_enhanced/16.png", "/calendar_enhanced/17.png", "/calendar_enhanced/18.png", "/calendar_enhanced/19.png"],
        18: ["/calendar_enhanced/18.png", "/calendar_enhanced/20.png", "/calendar_enhanced/21.png", "/calendar_enhanced/22.png", "/calendar_enhanced/23.png"],
        19: ["/calendar_enhanced/19.png", "/calendar_enhanced/24.png", "/calendar_enhanced/25.png", "/calendar_enhanced/1.png", "/calendar_enhanced/2.png"],
        20: ["/calendar_enhanced/20.png", "/calendar_enhanced/3.png", "/calendar_enhanced/4.png", "/calendar_enhanced/5.png", "/calendar_enhanced/6.png"],
        21: ["/calendar_enhanced/21.png", "/calendar_enhanced/7.png", "/calendar_enhanced/8.png", "/calendar_enhanced/9.png", "/calendar_enhanced/10.png"],
        22: ["/calendar_enhanced/22.png", "/calendar_enhanced/11.png", "/calendar_enhanced/12.png", "/calendar_enhanced/13.png", "/calendar_enhanced/14.png"],
        23: ["/calendar_enhanced/23.png", "/calendar_enhanced/15.png", "/calendar_enhanced/16.png", "/calendar_enhanced/17.png", "/calendar_enhanced/18.png"],
        24: ["/calendar_enhanced/24.png", "/calendar_enhanced/23.png", "/calendar_enhanced/24.png"],
        25: ["/calendar_enhanced/25.png", "/calendar_enhanced/1.png", "/calendar_enhanced/2.png"]
    }
    
    return extra_photos.get(day_number, base_photos)


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
