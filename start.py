import os
import subprocess

port = os.getenv("PORT", "8000")

print(f"🚀 Starting Reflex backend on port {port}")

subprocess.run([
    "reflex", "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", port,
    "--loglevel", "info",
])
