"""
API endpoint para webhooks de WhatsApp en Vercel
Versión ultra-simple para garantizar compatibilidad
"""

from http.server import BaseHTTPRequestHandler
import json
import urllib.parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Maneja las peticiones GET para verificación del webhook"""
        try:
            # Parsear query parameters
            query_params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            
            mode = query_params.get('hub.mode', [None])[0]
            token = query_params.get('hub.verify_token', [None])[0]
            challenge = query_params.get('hub.challenge', [None])[0]
            
            # Verificar webhook - token hardcodeado para garantizar funcionamiento
            verify_token = 'shanghai_2025_verify_token'
            
            if mode == 'subscribe' and token == verify_token and challenge:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(challenge.encode())
                return
            
            # Si no es verificación, devolver error
            self.send_response(403)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Forbidden')
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Error: {str(e)}'.encode())
    
    def do_POST(self):
        """Maneja las peticiones POST para recibir mensajes"""
        try:
            # Leer el cuerpo de la petición
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Parsear JSON
            data = json.loads(post_data.decode('utf-8'))
            
            # Respuesta simple
            result = {"status": "ok"}
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def do_OPTIONS(self):
        """Maneja las peticiones OPTIONS para CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
