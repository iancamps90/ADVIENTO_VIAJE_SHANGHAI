#!/usr/bin/env python3
"""
Script para probar la API directamente
Útil para probar sin desplegar en Vercel
"""

import requests
import json
import os
from datetime import datetime

def test_local_api():
    """Prueba la API localmente"""
    print("🧪 Probando API localmente...")
    
    # URL base (cambiar por tu dominio cuando esté desplegado)
    base_url = "https://shanghai.iancamps.dev"  # Cambiar por localhost:3000 si pruebas local
    
    # Probar endpoint de mensaje diario
    print(f"📡 Probando: {base_url}/api/daily-message")
    
    try:
        response = requests.get(f"{base_url}/api/daily-message", timeout=10)
        print(f"📊 Status Code: {response.status_code}")
        print(f"📝 Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ API funcionando correctamente")
        else:
            print("❌ Error en la API")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")

def test_webhook():
    """Prueba el webhook"""
    print("\n🔗 Probando webhook...")
    
    base_url = "https://shanghai.iancamps.dev"
    
    # Probar verificación del webhook
    params = {
        'hub.mode': 'subscribe',
        'hub.verify_token': 'shanghai_advent_2025_verify',
        'hub.challenge': 'test_challenge_123'
    }
    
    try:
        response = requests.get(f"{base_url}/api/webhook", params=params, timeout=10)
        print(f"📊 Status Code: {response.status_code}")
        print(f"📝 Response: {response.text}")
        
        if response.status_code == 200 and response.text == 'test_challenge_123':
            print("✅ Webhook verificado correctamente")
        else:
            print("❌ Error en la verificación del webhook")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")

def test_message_specific_day():
    """Prueba mensaje para un día específico"""
    print("\n📅 Probando mensaje para día específico...")
    
    base_url = "https://shanghai.iancamps.dev"
    
    data = {
        "day": 1
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/daily-message",
            json=data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        print(f"📊 Status Code: {response.status_code}")
        print(f"📝 Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ Mensaje del día 1 enviado correctamente")
        else:
            print("❌ Error al enviar mensaje del día")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")

def main():
    """Función principal"""
    print("🏮 PRUEBA DE API - CALENDARIO SHANGHAI 🐉")
    print("=" * 50)
    
    # Verificar si las variables de entorno están configuradas
    access_token = os.getenv('META_ACCESS_TOKEN')
    if not access_token:
        print("⚠️  META_ACCESS_TOKEN no está configurado")
        print("🔧 Configúralo en Vercel o como variable de entorno local")
    
    # Probar endpoints
    test_local_api()
    test_webhook()
    test_message_specific_day()
    
    print("\n" + "=" * 50)
    print("🏁 Pruebas completadas")
    print("\n💡 Para probar localmente:")
    print("   1. Ejecuta: python test-whatsapp.py")
    print("   2. O usa el panel de administración en /whatsapp-admin")

if __name__ == "__main__":
    main()
