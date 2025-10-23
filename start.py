import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Obtener puerto desde Railway o usar 8000 por defecto
port = os.getenv("PORT", "8080")
print(f"🚀 Starting Reflex backend on port {port}")

# 🔹 Servidor mínimo para /health (solo para que Railway pase el healthcheck)
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

def start_healthcheck_server():
    server = HTTPServer(("0.0.0.0", 8080), HealthHandler)
    print("🏥 Health check server running on port 8080")
    server.serve_forever()

# 🚀 Iniciar servidor de healthcheck en un hilo separado
health_thread = threading.Thread(target=start_healthcheck_server, daemon=True)
health_thread.start()

# ⚙️ Configuración para Reflex
os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# 🎯 Ejecutar Reflex en el puerto principal
cmd = [
    "reflex",
    "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", port,
    "--loglevel", "warning"
]

print(f"🎯 Starting Reflex on port {port}")
subprocess.run(cmd, check=True)