"""
API endpoint para envío automático de mensajes diarios
Este endpoint se puede llamar desde un cron job o servicio externo
"""

from http.server import BaseHTTPRequestHandler
import json
import datetime
from adeviento_web.services.meta_whatsapp_service import meta_whatsapp_service


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Envía el mensaje del día actual"""
        try:
            # Obtener día actual
            today = datetime.date.today()
            
            # Solo enviar si estamos en diciembre 2025
            if today.month == 12 and today.year == 2025:
                day_number = today.day
                
                # Verificar que el día esté en rango
                if 1 <= day_number <= 25:
                    # Enviar mensaje
                    result = meta_whatsapp_service.send_daily_message(day_number)
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        "success": True,
                        "day": day_number,
                        "result": result
                    }).encode())
                else:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        "success": False,
                        "error": "Día fuera de rango (1-25)"
                    }).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": False,
                    "error": "No es diciembre 2025"
                }).encode())
                
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "error": str(e)
            }).encode())
    
    def do_POST(self):
        """Envía mensaje para un día específico"""
        try:
            # Leer el cuerpo de la petición
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Parsear JSON
            data = json.loads(post_data.decode('utf-8'))
            day_number = data.get('day')
            
            if not day_number:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": False,
                    "error": "Parámetro 'day' requerido"
                }).encode())
                return
            
            # Enviar mensaje
            result = meta_whatsapp_service.send_daily_message(day_number)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": True,
                "day": day_number,
                "result": result
            }).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "error": str(e)
            }).encode())
    
    def do_OPTIONS(self):
        """Maneja las peticiones OPTIONS para CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
