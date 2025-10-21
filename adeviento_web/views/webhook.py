import reflex as rx
from reflex import State
from adeviento_web.services.meta_whatsapp_service import meta_whatsapp_service
from adeviento_web.styles.styles import Size
import json
import datetime


class WebhookState(State):
    """Estado para manejar webhooks de WhatsApp"""
    
    def verify_webhook(self, mode: str, token: str, challenge: str) -> str:
        """Verifica el webhook de Meta"""
        result = meta_whatsapp_service.verify_webhook(mode, token, challenge)
        return result if result else "Verification failed"
    
    def process_webhook(self, data: dict) -> dict:
        """Procesa los mensajes del webhook"""
        return meta_whatsapp_service.process_webhook(data)
    
    def send_daily_message(self, day_number: int = None) -> dict:
        """Envía el mensaje del día"""
        return meta_whatsapp_service.send_daily_message(day_number)
    
    def send_test_message(self) -> dict:
        """Envía mensaje de prueba"""
        return meta_whatsapp_service.send_test_message()
    
    def get_service_status(self) -> dict:
        """Obtiene el estado del servicio"""
        return meta_whatsapp_service.get_friends_status()


def webhook_verify() -> rx.Component:
    """Endpoint para verificar el webhook de Meta"""
    return rx.text("Webhook verification endpoint")


def webhook_receive() -> rx.Component:
    """Endpoint para recibir mensajes del webhook"""
    return rx.text("Webhook receive endpoint")


def admin_panel() -> rx.Component:
    """Panel de administración para WhatsApp"""
    return rx.vstack(
        rx.heading(
            "Panel de Administración WhatsApp",
            size="6",
            color="#DC143C",
            text_align="center"
        ),
        
        rx.box(
            rx.vstack(
                rx.text(
                    "Estado del Servicio",
                    font_weight="bold",
                    color="#FFD700",
                    font_size="1.2em"
                ),
                rx.text(
                    id="service-status",
                    color="#FFFFFF"
                ),
                rx.button(
                    "Actualizar Estado",
                    on_click=WebhookState.get_service_status,
                    background="#DC143C",
                    color="#FFFFFF",
                    border_radius="8px",
                    padding="10px 20px"
                ),
                align="center",
                spacing="2"
            ),
            padding=Size.BIG.value,
            background="rgba(0,0,0,0.7)",
            border_radius="8px",
            border="2px solid #FFD700",
            width="100%"
        ),
        
        rx.box(
            rx.vstack(
                rx.text(
                    "Envío de Mensajes",
                    font_weight="bold",
                    color="#FFD700",
                    font_size="1.2em"
                ),
                rx.hstack(
                    rx.button(
                        "Mensaje de Prueba",
                        on_click=WebhookState.send_test_message,
                        background="#228B22",
                        color="#FFFFFF",
                        border_radius="8px",
                        padding="10px 20px"
                    ),
                    rx.button(
                        "Mensaje del Día",
                        on_click=WebhookState.send_daily_message,
                        background="#DC143C",
                        color="#FFFFFF",
                        border_radius="8px",
                        padding="10px 20px"
                    ),
                    spacing="2",
                    justify="center",
                    flex_wrap="wrap"
                ),
                rx.text(
                    "⚠️ Los mensajes se enviarán a todos los números configurados",
                    font_size="0.9em",
                    color="#FFD700",
                    text_align="center"
                ),
                align="center",
                spacing="3"
            ),
            padding=Size.BIG.value,
            background="rgba(0,0,0,0.7)",
            border_radius="8px",
            border="2px solid #FFD700",
            width="100%"
        ),
        
        rx.box(
            rx.vstack(
                rx.text(
                    "Configuración de Meta API",
                    font_weight="bold",
                    color="#FFD700",
                    font_size="1.2em"
                ),
                rx.text(
                    "Para configurar la automatización de mensajes:",
                    color="#FFFFFF"
                ),
                rx.vstack(
                    rx.text("1. Crea una cuenta de desarrollador en Meta", color="#FFFFFF"),
                    rx.text("2. Configura una aplicación de WhatsApp Business", color="#FFFFFF"),
                    rx.text("3. Obtén tu Access Token y Phone Number ID", color="#FFFFFF"),
                    rx.text("4. Configura las variables de entorno en Vercel:", color="#FFFFFF"),
                    rx.code_block(
                        """META_ACCESS_TOKEN=tu_access_token
META_PHONE_NUMBER_ID=tu_phone_number_id
META_VERIFY_TOKEN=tu_verify_token""",
                        language="bash",
                        background="rgba(0,0,0,0.8)",
                        border_radius="4px",
                        padding="10px"
                    ),
                    align="start",
                    spacing="1"
                ),
                align="center",
                spacing="3"
            ),
            padding=Size.BIG.value,
            background="rgba(0,0,0,0.7)",
            border_radius="8px",
            border="2px solid #FFD700",
            width="100%"
        ),
        
        rx.box(
            rx.vstack(
                rx.text(
                    "Números de Amigos Configurados",
                    font_weight="bold",
                    color="#FFD700",
                    font_size="1.2em"
                ),
                rx.text(
                    "Edita el archivo adeviento_web/config/whatsapp_config.py para añadir los números reales",
                    color="#FFFFFF",
                    text_align="center"
                ),
                rx.code_block(
                    """FRIENDS_PHONE_NUMBERS = [
    "34612345678",  # Amigo 1
    "34612345679",  # Amigo 2  
    "34612345680",  # Amigo 3
    "34612345681",  # Amigo 4
]""",
                    language="python",
                    background="rgba(0,0,0,0.8)",
                    border_radius="4px",
                    padding="10px"
                ),
                align="center",
                spacing="3"
            ),
            padding=Size.BIG.value,
            background="rgba(0,0,0,0.7)",
            border_radius="8px",
            border="2px solid #FFD700",
            width="100%"
        ),
        
        align="center",
        spacing="4",
        width="100%",
        max_width="800px",
        padding=Size.BIG.value
    )
