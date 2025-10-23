import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time

# Obtener puerto desde Railway
railway_port = os.getenv("PORT", "8080")
reflex_port = "8081"  # Puerto separado para Reflex
print(f"🚀 Starting Reflex backend on port {reflex_port}")

# Servidor de healthcheck y API
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}')
        elif self.path == "/api/health":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(b'{"status": "ok", "message": "Backend is running"}')
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_OPTIONS(self):
        # Manejar preflight CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def log_message(self, format, *args):
        pass  # Silenciar logs del healthcheck

def start_healthcheck_server():
    try:
        server = HTTPServer(("0.0.0.0", int(railway_port)), HealthHandler)
        print(f"🏥 Health check server running on port {railway_port}")
        server.serve_forever()
    except Exception as e:
        print(f"❌ Health check server error: {e}")

# Iniciar servidor de healthcheck en hilo separado
health_thread = threading.Thread(target=start_healthcheck_server, daemon=True)
health_thread.start()

# Esperar un poco para que el healthcheck esté listo
time.sleep(2)

# Configuración para Reflex
os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# Ejecutar Reflex
cmd = [
    "reflex",
    "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", reflex_port,
    "--loglevel", "warning"
]

print(f"🎯 Starting Reflex on port {reflex_port}")
subprocess.run(cmd, check=True)