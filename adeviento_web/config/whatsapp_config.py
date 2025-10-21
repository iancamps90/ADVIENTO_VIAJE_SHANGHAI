# Configuración de WhatsApp para el grupo de amigos
# Añade aquí los números de teléfono de tus 4 amigos (con código de país, sin +)

# Ejemplo: +34612345678 -> "34612345678"
FRIENDS_PHONE_NUMBERS = [
    "34612345678",  # Amigo 1 - Reemplaza con el número real
    "34612345679",  # Amigo 2 - Reemplaza con el número real  
    "34612345680",  # Amigo 3 - Reemplaza con el número real
    "34612345681",  # Amigo 4 - Reemplaza con el número real
]

# Mensaje base que se envía cada día
BASE_WHATSAPP_MESSAGE = """🎁 *¡Nuevo día en el Calendario de Adviento Shanghai!*

{day_content}

🔗 *Ver detalles completos:* {day_url}

📅 *Día {day_number} de 25* - ¡Solo quedan {days_left} días para Shanghai!

#ShanghaiAdvent2025 #ViajeShanghai2025 🏮"""

# Configuración de envío automático
AUTO_SEND_TIME = "09:00"  # Hora de envío automático (formato 24h)
AUTO_SEND_ENABLED = True  # Cambiar a False para desactivar envío automático

# Mensaje de prueba para verificar configuración
TEST_MESSAGE = """🧪 *Mensaje de prueba - Calendario Shanghai*

¡Hola! Este es un mensaje de prueba para verificar que la configuración de WhatsApp funciona correctamente.

Si recibes este mensaje, ¡todo está listo para el calendario de adviento! 🎉

#ShanghaiAdvent2025"""
