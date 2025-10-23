import os
import subprocess
import sys

port = os.getenv("PORT", "8080")
print(f"🚀 Starting Reflex backend on port {port}")

os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

cmd = [
    sys.executable,
    "-m", "reflex",
    "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", port,
    "--no-frontend",
    "--loglevel", "warning",
]

subprocess.run(cmd, check=True)
