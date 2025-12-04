import reflex as rx
import os

# Detecta automáticamente el backend_url
backend_url = os.getenv("BACKEND_URL", "http://localhost:8080")

config = rx.Config(
    app_name="adeviento_web",
    backend_url=backend_url,
    db_url="sqlite:///reflex.db",
    env=rx.Env.PROD,
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    cors_allowed_origins=["*"],
)
