import reflex as rx
import datetime
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import TextColor, Color
from adeviento_web.components.button import button
from adeviento_web.views.calendar import (
    _shanghai_days, _shanghai_day_name, _shanghai_day_message, 
    _shanghai_day_motivation, _shanghai_day_recommendations, 
    _shanghai_day_video, _shanghai_day_photo, _is_day_available
)
from adeviento_web.services.whatsapp_service import whatsapp_service


def admin() -> rx.Component:
    """Panel de administración para envío manual de mensajes de WhatsApp"""
    
    today = datetime.date.today()
    current_day = today.day if today.month == 12 and today.year == 2025 else 1
    
    return rx.vstack(
        # Header del admin
        rx.box(
            rx.vstack(
                rx.heading(
                    "Panel de Administración",
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
                spacing="2"
            ),
            padding=Size.BIG.value,
            background=f"linear-gradient(135deg, {Color.BACKGROUND.value}, {Color.SECONDARY.value})",
            border_radius="12px",
            border=f"2px solid {Color.SECONDARY.value}",
            width="100%"
        ),
        
        # Información del día actual
        rx.box(
            rx.vstack(
                rx.text(
                    f"Día actual: {current_day} de diciembre de 2025",
                    font_weight="bold",
                    color=TextColor.ACCENT.value,
                    font_size=Size.MEDIUM.value
                ),
                rx.text(
                    f"Fecha: {today.strftime('%d/%m/%Y')}",
                    color=TextColor.SECONDARY.value
                ),
                align="center",
                spacing="2"
            ),
            padding=Size.BIG.value,
            background=Color.PRIMARY.value,
            border_radius="8px",
            border=f"1px solid {Color.SECONDARY.value}",
            width="100%"
        ),
        
        # Contenido del día actual
        rx.cond(
            current_day <= 25,
            rx.box(
                rx.vstack(
                    rx.text(
                        f"Contenido del Día {current_day}:",
                        font_weight="bold",
                        color=TextColor.ACCENT.value,
                        font_size=Size.MEDIUM.value
                    ),
                    rx.text(
                        _shanghai_day_name(current_day - 1),
                        color=TextColor.SECONDARY.value,
                        font_weight="bold"
                    ),
                    rx.text(
                        _shanghai_day_message(current_day - 1),
                        color=TextColor.SECONDARY.value,
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
            )
        ),
        
        # Botones de acción
        rx.box(
            rx.vstack(
                rx.text(
                    "Acciones disponibles:",
                    font_weight="bold",
                    color=TextColor.ACCENT.value,
                    font_size=Size.MEDIUM.value
                ),
                rx.vstack(
                    # Botones principales
                    rx.hstack(
                        rx.button(
                            "📱 Enviar a los 4 amigos",
                            background=Color.ACCENT.value,
                            color=TextColor.PRIMARY.value,
                            _hover={
                                "background": Color.QUATERNARY.value,
                                "transform": "scale(1.05)"
                            },
                            on_click=send_whatsapp_message
                        ),
                        rx.button(
                            "👁️ Previsualizar mensaje",
                            background=Color.SECONDARY.value,
                            color=TextColor.PRIMARY.value,
                            _hover={
                                "background": Color.TERTIARY.value,
                                "transform": "scale(1.05)"
                            },
                            on_click=preview_whatsapp_message
                        ),
                        spacing="3",
                        justify="center",
                        flex_wrap="wrap"
                    ),
                    
                    # Botones secundarios
                    rx.hstack(
                        rx.button(
                            "🧪 Enviar mensaje de prueba",
                            background=Color.TERTIARY.value,
                            color=TextColor.PRIMARY.value,
                            _hover={
                                "background": Color.SECONDARY.value,
                                "transform": "scale(1.05)"
                            },
                            on_click=send_test_message
                        ),
                        rx.link(
                            button(
                                "Ver página del día",
                                ""
                            ),
                            href=f"/day/{current_day}",
                            external=False
                        ),
                        rx.link(
                            button(
                                "Volver al calendario",
                                ""
                            ),
                            href="/",
                            external=False
                        ),
                        spacing="3",
                        justify="center",
                        flex_wrap="wrap"
                    ),
                    
                    spacing="3"
                ),
                align="center",
                spacing="3"
            ),
            padding=Size.BIG.value,
            background=Color.PRIMARY.value,
            border_radius="8px",
            border=f"2px solid {Color.ACCENT.value}",
            width="100%"
        ),
        
        # Información de configuración
        rx.box(
            rx.vstack(
                rx.text(
                    "📱 Configuración de WhatsApp:",
                    font_weight="bold",
                    color=TextColor.ACCENT.value,
                    font_size=Size.MEDIUM.value
                ),
                rx.text(
                    f"• {len(whatsapp_service.friends_numbers)} amigos configurados",
                    color=TextColor.SECONDARY.value,
                    font_size=Size.SMALL.value
                ),
                rx.text(
                    f"• Envío automático: {'Activado' if whatsapp_service.get_friends_status()['auto_send_enabled'] else 'Desactivado'}",
                    color=TextColor.SECONDARY.value,
                    font_size=Size.SMALL.value
                ),
                rx.text(
                    f"• Hora de envío: {whatsapp_service.get_friends_status()['auto_send_time']}",
                    color=TextColor.SECONDARY.value,
                    font_size=Size.SMALL.value
                ),
                rx.text(
                    "• Los mensajes incluyen: contenido del día, link directo y hashtags",
                    color=TextColor.SECONDARY.value,
                    font_size=Size.SMALL.value
                ),
                rx.text(
                    "• Para configurar números: edita adeviento_web/config/whatsapp_config.py",
                    color=TextColor.TERTIARY.value,
                    font_size=Size.SMALL.value,
                    font_style="italic"
                ),
                align="start",
                spacing="1"
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


def send_whatsapp_message():
    """Función para enviar mensaje de WhatsApp manualmente a los 4 amigos"""
    today = datetime.date.today()
    current_day = today.day if today.month == 12 and today.year == 2025 else 1
    
    try:
        # Usar el servicio de WhatsApp
        results = whatsapp_service.send_daily_message(current_day)
        
        # Contar éxitos y fallos
        success_count = sum(1 for success in results.values() if success)
        total_count = len(results)
        
        if success_count == total_count:
            return rx.window_alert(f"✅ ¡Mensaje del día {current_day} enviado a todos los {total_count} amigos!")
        elif success_count > 0:
            return rx.window_alert(f"⚠️ Mensaje enviado a {success_count} de {total_count} amigos. Revisa la configuración.")
        else:
            return rx.window_alert("❌ Error: No se pudo enviar el mensaje a ningún amigo. Revisa la configuración.")
            
    except Exception as e:
        return rx.window_alert(f"❌ Error al enviar mensaje: {str(e)}")


def send_test_message():
    """Función para enviar mensaje de prueba"""
    try:
        results = whatsapp_service.send_test_message()
        success_count = sum(1 for success in results.values() if success)
        total_count = len(results)
        
        if success_count == total_count:
            return rx.window_alert(f"✅ ¡Mensaje de prueba enviado a todos los {total_count} amigos!")
        else:
            return rx.window_alert(f"⚠️ Mensaje de prueba enviado a {success_count} de {total_count} amigos.")
            
    except Exception as e:
        return rx.window_alert(f"❌ Error al enviar mensaje de prueba: {str(e)}")


def preview_whatsapp_message():
    """Función para previsualizar el mensaje de WhatsApp"""
    today = datetime.date.today()
    current_day = today.day if today.month == 12 and today.year == 2025 else 1
    
    try:
        message = whatsapp_service.create_whatsapp_message(current_day)
        return rx.window_alert(f"📱 Previsualización del mensaje del día {current_day}:\n\n{message}")
    except Exception as e:
        return rx.window_alert(f"❌ Error al generar previsualización: {str(e)}")

