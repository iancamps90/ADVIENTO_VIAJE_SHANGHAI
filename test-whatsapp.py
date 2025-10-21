#!/usr/bin/env python3
"""
Script de prueba para WhatsApp
Ejecuta este script para probar el envío de mensajes
"""

import os
import sys
import requests
import json
from datetime import datetime

# Añadir el directorio del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from adeviento_web.services.meta_whatsapp_service import meta_whatsapp_service

def test_whatsapp_configuration():
    """Prueba la configuración de WhatsApp"""
    print("🔧 Probando configuración de WhatsApp...")
    
    # Verificar variables de entorno
    access_token = os.getenv('META_ACCESS_TOKEN')
    phone_number_id = os.getenv('META_PHONE_NUMBER_ID')
    verify_token = os.getenv('META_VERIFY_TOKEN')
    
    print(f"✅ Access Token: {'Configurado' if access_token else '❌ No configurado'}")
    print(f"✅ Phone Number ID: {'Configurado' if phone_number_id else '❌ No configurado'}")
    print(f"✅ Verify Token: {'Configurado' if verify_token else '❌ No configurado'}")
    
    # Verificar configuración del servicio
    is_configured = meta_whatsapp_service.is_configured()
    print(f"✅ Servicio configurado: {'Sí' if is_configured else '❌ No'}")
    
    # Mostrar estado de amigos
    status = meta_whatsapp_service.get_friends_status()
    print(f"✅ Número de amigos: {status['total_friends']}")
    print(f"✅ Números configurados: {status['numbers_configured']}")
    
    return is_configured

def test_message_creation():
    """Prueba la creación de mensajes"""
    print("\n📝 Probando creación de mensajes...")
    
    # Probar mensaje del día 1
    message = meta_whatsapp_service.create_whatsapp_message(1)
    print(f"✅ Mensaje del día 1 creado: {len(message)} caracteres")
    print(f"📄 Preview: {message[:100]}...")
    
    return message

def test_single_message():
    """Prueba envío de un mensaje individual"""
    print("\n📱 Probando envío de mensaje individual...")
    
    # Tu número
    phone_number = "34615784663"
    
    # Mensaje de prueba
    test_message = """*🧪 Mensaje de Prueba - Calendario Shanghai* 🏮

¡Hola! Este es un mensaje de prueba para verificar que la configuración de WhatsApp funciona correctamente.

*Si recibes este mensaje, ¡todo está listo para el calendario de adviento!* ✨

*Características del calendario:*
• 🎊 Animaciones móviles espectaculares
• 🐉 Dragones voladores y farolillos chinos
• 📱 Efectos táctiles con vibración
• 🎯 25 días de sorpresas para Shanghai
• 🤖 Mensajes automáticos diarios

*¡Que empiece la aventura más épica del año!* 🚀

#ShanghaiAdvent2025 #ViajeShanghai2025"""
    
    print(f"📤 Enviando mensaje a {phone_number}...")
    result = meta_whatsapp_service.send_message(phone_number, test_message)
    
    if result["success"]:
        print("✅ ¡Mensaje enviado correctamente!")
        print(f"📨 Message ID: {result.get('message_id', 'N/A')}")
    else:
        print("❌ Error al enviar mensaje:")
        print(f"🔍 Error: {result.get('error', 'Error desconocido')}")
    
    return result

def test_daily_message():
    """Prueba el mensaje del día"""
    print("\n📅 Probando mensaje del día...")
    
    result = meta_whatsapp_service.send_daily_message(1)  # Día 1 para testing
    
    print(f"📊 Resultado del envío:")
    print(f"✅ Mensajes enviados: {result['total_sent']}")
    print(f"❌ Mensajes fallidos: {result['total_failed']}")
    
    for phone, detail in result['details'].items():
        status = "✅" if detail['success'] else "❌"
        print(f"{status} {phone}: {detail.get('error', 'Enviado correctamente')}")
    
    return result

def main():
    """Función principal de prueba"""
    print("🏮 CALENDARIO DE ADVIENTO SHANGHAI - PRUEBA DE WHATSAPP 🐉")
    print("=" * 60)
    
    # Paso 1: Verificar configuración
    if not test_whatsapp_configuration():
        print("\n❌ La configuración no está completa.")
        print("🔧 Asegúrate de configurar las variables de entorno:")
        print("   - META_ACCESS_TOKEN")
        print("   - META_PHONE_NUMBER_ID")
        print("   - META_VERIFY_TOKEN")
        return
    
    # Paso 2: Probar creación de mensajes
    message = test_message_creation()
    
    # Paso 3: Probar envío individual
    print("\n" + "=" * 60)
    print("🚀 INICIANDO PRUEBA DE ENVÍO...")
    
    result = test_single_message()
    
    if result["success"]:
        print("\n🎉 ¡PRUEBA EXITOSA!")
        print("✅ El mensaje se envió correctamente a tu número")
        print("📱 Revisa tu WhatsApp para confirmar la recepción")
        
        # Paso 4: Probar mensaje del día
        print("\n" + "=" * 60)
        print("📅 PROBANDO MENSAJE DEL DÍA...")
        test_daily_message()
        
    else:
        print("\n❌ PRUEBA FALLIDA")
        print("🔍 Revisa la configuración y los logs de error")
    
    print("\n" + "=" * 60)
    print("🏁 Prueba completada")

if __name__ == "__main__":
    main()
