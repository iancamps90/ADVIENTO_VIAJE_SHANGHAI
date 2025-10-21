import requests
import datetime
from typing import List, Dict
import adeviento_web.config.whatsapp_config as config
from adeviento_web.views.calendar import (
    _shanghai_days, _shanghai_day_name, _shanghai_day_message, 
    _shanghai_day_motivation, _shanghai_day_recommendations
)


class WhatsAppService:
    """Servicio para envío de mensajes de WhatsApp"""
    
    def __init__(self):
        self.friends_numbers = config.FRIENDS_PHONE_NUMBERS
        self.base_message = config.BASE_WHATSAPP_MESSAGE
        self.test_message = config.TEST_MESSAGE
    
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
        
        # Crear contenido formateado
        content = f"*{day_name}*\n\n{day_message}"
        
        if day_motivation:
            content += f"\n\n💫 *Frase del día:*\n\"{day_motivation}\""
        
        if day_recommendations:
            # Tomar solo las primeras 2 recomendaciones para el mensaje
            recommendations = day_recommendations.split('\n')[:2]
            content += f"\n\n📋 *Recomendaciones:*\n" + "\n".join(recommendations)
        
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
        day_url = f"https://shanghai-advent.vercel.app/day/{day_number}"
        
        # Crear mensaje final
        message = self.base_message.format(
            day_content=day_content["content"],
            day_url=day_url,
            day_number=day_number,
            days_left=days_left
        )
        
        return message
    
    def send_to_friends(self, message: str) -> Dict[str, bool]:
        """Envía el mensaje a todos los amigos"""
        results = {}
        
        for phone_number in self.friends_numbers:
            try:
                # Crear URL de WhatsApp
                whatsapp_url = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20').replace('\n', '%0A')}"
                
                # En una implementación real, aquí harías una llamada a la API de WhatsApp
                # Por ahora, solo simulamos el envío
                print(f"Enviando mensaje a {phone_number}: {message[:50]}...")
                
                # Simular éxito
                results[phone_number] = True
                
            except Exception as e:
                print(f"Error enviando a {phone_number}: {e}")
                results[phone_number] = False
        
        return results
    
    def send_daily_message(self, day_number: int = None) -> Dict[str, bool]:
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
    
    def send_test_message(self) -> Dict[str, bool]:
        """Envía un mensaje de prueba a todos los amigos"""
        return self.send_to_friends(self.test_message)
    
    def get_friends_status(self) -> Dict[str, str]:
        """Obtiene el estado de configuración de los amigos"""
        return {
            "total_friends": len(self.friends_numbers),
            "numbers_configured": [num[:3] + "***" + num[-3:] for num in self.friends_numbers],
            "auto_send_enabled": config.AUTO_SEND_ENABLED,
            "auto_send_time": config.AUTO_SEND_TIME
        }


# Instancia global del servicio
whatsapp_service = WhatsAppService()
