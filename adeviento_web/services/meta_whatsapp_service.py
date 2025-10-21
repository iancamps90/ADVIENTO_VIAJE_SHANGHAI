import requests
import datetime
import json
import os
from typing import List, Dict, Optional
import adeviento_web.config.whatsapp_config as config
from adeviento_web.views.calendar import (
    _shanghai_days, _shanghai_day_name, _shanghai_day_message, 
    _shanghai_day_motivation, _shanghai_day_recommendations
)


class MetaWhatsAppService:
    """Servicio para envío de mensajes de WhatsApp usando Meta API"""
    
    def __init__(self):
        # Configuración de Meta API
        self.access_token = os.getenv('META_ACCESS_TOKEN')
        self.phone_number_id = os.getenv('META_PHONE_NUMBER_ID')
        self.verify_token = os.getenv('META_VERIFY_TOKEN')
        self.webhook_url = os.getenv('WEBHOOK_URL', 'https://shanghai.iancamps.dev/webhook')
        
        # Configuración de amigos
        self.friends_numbers = config.FRIENDS_PHONE_NUMBERS
        self.base_message = config.BASE_WHATSAPP_MESSAGE
        self.test_message = config.TEST_MESSAGE
        
        # URL base de la API de Meta
        self.api_url = f"https://graph.facebook.com/v18.0/{self.phone_number_id}/messages"
    
    def is_configured(self) -> bool:
        """Verifica si el servicio está configurado correctamente"""
        return bool(self.access_token and self.phone_number_id)
    
    def get_current_day_content(self, day_number: int) -> Dict[str, str]:
        """Obtiene el contenido del día actual"""
        if day_number < 1 or day_number > 25:
            return {}
        
        day_index = day_number - 1
        if day_index >= len(_shanghai_days):
            return {}
        
        day_name = _shanghai_day_name(day_index)
        day_message = _shanghai_day_message(day_index)
        day_motivation = _shanghai_day_motivation(day_index)
        day_recommendations = _shanghai_day_recommendations(day_index)
        
        # Crear contenido formateado para WhatsApp
        content = f"*{day_name}*\n\n{day_message}"
        
        if day_motivation:
            content += f"\n\n*Frase del día:*\n\"{day_motivation}\""
        
        if day_recommendations:
            # Tomar solo las primeras 3 recomendaciones para el mensaje
            recommendations = day_recommendations.split('\n')[:3]
            content += f"\n\n*Recomendaciones:*\n" + "\n".join(recommendations)
        
        return {
            "content": content,
            "day_name": day_name,
            "day_message": day_message,
            "day_motivation": day_motivation,
            "day_recommendations": day_recommendations
        }
    
    def create_whatsapp_message(self, day_number: int) -> str:
        """Crea el mensaje completo para WhatsApp"""
        day_content = self.get_current_day_content(day_number)
        
        if not day_content:
            return "Error: No se pudo obtener el contenido del día"
        
        # Calcular días restantes
        days_left = 25 - day_number
        
        # URL del día
        day_url = f"https://shanghai.iancamps.dev/day/{day_number}"
        
        # Crear mensaje final
        message = self.base_message.format(
            day_content=day_content["content"],
            day_url=day_url,
            day_number=day_number,
            days_left=days_left
        )
        
        return message
    
    def send_message(self, phone_number: str, message: str) -> Dict[str, any]:
        """Envía un mensaje individual usando Meta API"""
        if not self.is_configured():
            return {
                "success": False,
                "error": "Servicio no configurado. Faltan credenciales de Meta API."
            }
        
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        
        data = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "text",
            "text": {
                "body": message
            }
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "message_id": response.json().get('messages', [{}])[0].get('id'),
                    "phone_number": phone_number
                }
            else:
                return {
                    "success": False,
                    "error": f"Error {response.status_code}: {response.text}",
                    "phone_number": phone_number
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "phone_number": phone_number
            }
    
    def send_to_friends(self, message: str) -> Dict[str, any]:
        """Envía el mensaje a todos los amigos"""
        results = {
            "total_sent": 0,
            "total_failed": 0,
            "details": {}
        }
        
        for phone_number in self.friends_numbers:
            result = self.send_message(phone_number, message)
            results["details"][phone_number] = result
            
            if result["success"]:
                results["total_sent"] += 1
            else:
                results["total_failed"] += 1
        
        return results
    
    def send_daily_message(self, day_number: int = None) -> Dict[str, any]:
        """Envía el mensaje del día a todos los amigos"""
        if day_number is None:
            # Obtener día actual
            today = datetime.date.today()
            if today.month == 12 and today.year == 2025:
                day_number = today.day
            else:
                day_number = 1  # Para testing
        
        message = self.create_whatsapp_message(day_number)
        return self.send_to_friends(message)
    
    def send_test_message(self) -> Dict[str, any]:
        """Envía un mensaje de prueba a todos los amigos"""
        return self.send_to_friends(self.test_message)
    
    def send_custom_message(self, message: str) -> Dict[str, any]:
        """Envía un mensaje personalizado a todos los amigos"""
        return self.send_to_friends(message)
    
    def get_friends_status(self) -> Dict[str, str]:
        """Obtiene el estado de configuración de los amigos"""
        return {
            "total_friends": len(self.friends_numbers),
            "numbers_configured": [num[:3] + "***" + num[-3:] for num in self.friends_numbers],
            "auto_send_enabled": config.AUTO_SEND_ENABLED,
            "auto_send_time": config.AUTO_SEND_TIME,
            "meta_api_configured": self.is_configured(),
            "webhook_url": self.webhook_url
        }
    
    def verify_webhook(self, mode: str, token: str, challenge: str) -> Optional[str]:
        """Verifica el webhook de Meta"""
        if mode == "subscribe" and token == self.verify_token:
            return challenge
        return None
    
    def process_webhook(self, data: dict) -> dict:
        """Procesa los mensajes recibidos del webhook"""
        try:
            # Procesar mensajes entrantes
            if 'entry' in data:
                for entry in data['entry']:
                    if 'changes' in entry:
                        for change in entry['changes']:
                            if 'value' in change and 'messages' in change['value']:
                                for message in change['value']['messages']:
                                    # Procesar mensaje recibido
                                    return self._handle_incoming_message(message)
            
            return {"status": "processed"}
            
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def _handle_incoming_message(self, message: dict) -> dict:
        """Maneja mensajes entrantes"""
        # Aquí puedes añadir lógica para responder automáticamente
        # Por ejemplo, si alguien escribe "ayuda", enviar información del calendario
        
        sender_phone = message.get('from', '')
        message_text = message.get('text', {}).get('body', '').lower()
        
        if 'ayuda' in message_text or 'help' in message_text:
            help_message = """*¡Hola! Soy el asistente del Calendario de Adviento Shanghai!* 🏮

*Comandos disponibles:*
• *ayuda* - Muestra este mensaje
• *día* - Muestra el día actual
• *progreso* - Muestra el progreso del viaje
• *shanghai* - Información sobre el viaje

*¡Solo quedan unos días para Shanghai!* ✈️🇨🇳

#ShanghaiAdvent2025"""
            
            return self.send_message(sender_phone, help_message)
        
        elif 'día' in message_text or 'day' in message_text:
            today = datetime.date.today()
            if today.month == 12 and today.year == 2025:
                current_day = today.day
            else:
                current_day = 1
            
            day_message = self.create_whatsapp_message(current_day)
            return self.send_message(sender_phone, day_message)
        
        elif 'progreso' in message_text or 'progress' in message_text:
            today = datetime.date.today()
            if today.month == 12 and today.year == 2025:
                current_day = today.day
            else:
                current_day = 1
            
            progress_message = f"""*Progreso del viaje a Shanghai* 📊

*Día actual:* {current_day}/25
*Días restantes:* {25 - current_day}
*Progreso:* {(current_day/25)*100:.1f}%

*¡Seguimos avanzando hacia Shanghai!* 🏮✈️

#ShanghaiAdvent2025"""
            
            return self.send_message(sender_phone, progress_message)
        
        return {"status": "no_action"}


# Instancia global del servicio
meta_whatsapp_service = MetaWhatsAppService()
