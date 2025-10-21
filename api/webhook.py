"""
API endpoint para webhooks de WhatsApp en Vercel
Este archivo debe estar en la carpeta /api/ para que Vercel lo reconozca como endpoint
"""

from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
from adeviento_web.services.meta_whatsapp_service import meta_whatsapp_service


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Maneja las peticiones GET para verificación del webhook"""
        if self.path.startswith('/api/webhook'):
            # Parsear query parameters
            query_params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            
            mode = query_params.get('hub.mode', [None])[0]
            token = query_params.get('hub.verify_token', [None])[0]
            challenge = query_params.get('hub.challenge', [None])[0]
            
            # Verificar webhook
            result = meta_whatsapp_service.verify_webhook(mode, token, challenge)
            
            if result:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(result.encode())
            else:
                self.send_response(403)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Verification failed')
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        """Maneja las peticiones POST para recibir mensajes"""
        if self.path.startswith('/api/webhook'):
            # Leer el cuerpo de la petición
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                # Parsear JSON
                data = json.loads(post_data.decode('utf-8'))
                
                # Procesar webhook
                result = meta_whatsapp_service.process_webhook(data)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(result).encode())
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_OPTIONS(self):
        """Maneja las peticiones OPTIONS para CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
