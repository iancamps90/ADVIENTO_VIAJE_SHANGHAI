import os
import subprocess
import sys

port = os.getenv("PORT", "10000")

print(f"🚀 Starting Reflex on port: {port}")

os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

cmd = [
    "reflex", "run",
    "--env", "prod",
    "--backend-host", "0.0.0.0",
    "--backend-port", port,
    "--loglevel", "warning"
]

subprocess.run(cmd, check=True)
