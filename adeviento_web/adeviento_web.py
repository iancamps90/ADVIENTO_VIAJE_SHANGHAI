import reflex as rx
import adeviento_web.styles.styles as styles
from adeviento_web.views.navbar import navbar
from adeviento_web.views.header import header
from adeviento_web.views.calendar import calendar
from adeviento_web.views.footer import footer
from adeviento_web.views.day_detail import day_detail
from adeviento_web.views.admin import admin
from adeviento_web.views.webhook import admin_panel
from adeviento_web.components.countdown import countdown_timer, countdown_script
from adeviento_web.components.special_effects import special_effects_script, countdown_enhanced

title = "Calendario de Adviento Shanghai 2025 | 25 días. 25 sorpresas para el viaje"
description = "¡Calendario de adviento personalizado para nuestro viaje a Shanghai! Del 1 al 25 de diciembre de 2025, cada día una nueva sorpresa para calentar el viaje."
preview = "https://adviento.dev/preview.jpg"


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.script(src="/js/snow.js"),
        rx.script(src="/js/mobile-animations.js"),
        rx.script(src="/js/fireworks.js"),
        rx.script(src="/js/sound-effects.js"),
        countdown_script(),
        # special_effects_script(),  # Comentado temporalmente
        
        # Elementos flotantes chinos
        rx.box(
            rx.text("🏮", class_name="lantern"),
            rx.text("🏮", class_name="lantern"),
            rx.text("🏮", class_name="lantern"),
            rx.text("🏮", class_name="lantern"),
            rx.text("🏮", class_name="lantern"),
            class_name="floating-lanterns"
        ),
        
        rx.box(
            rx.text("龙", class_name="chinese-char"),
            rx.text("福", class_name="chinese-char"),
            rx.text("喜", class_name="chinese-char"),
            rx.text("财", class_name="chinese-char"),
            class_name="floating-characters"
        ),
        
        navbar(),
        rx.vstack(
            header(),
            countdown_enhanced(),
            calendar(),
            footer(),
            align="center",
            width="100%",
            spacing="6"
        )
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-Y6GDVB3FJB"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-Y6GDVB3FJB');
"""
        ),
    ],
)


app.add_page(
    index,
    title=title,
    description=description,
    image=preview,
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@shanghaiadvent"}
    ]
)

# Añadir página de administración
app.add_page(
    admin,
    route="/admin",
    title="Panel de Administración - Calendario de Adviento Shanghai 2025",
    description="Panel de administración para gestionar el calendario de adviento",
    image=preview
)

# Añadir página de administración de WhatsApp (comentado temporalmente)
# app.add_page(
#     admin_panel,
#     route="/whatsapp-admin",
#     title="Panel de WhatsApp - Calendario de Adviento Shanghai 2025",
#     description="Panel de administración para gestionar mensajes de WhatsApp",
#     image=preview
# )

# Añadir páginas para cada día del calendario (1-25)
for day_num in range(1, 26):
    day_title = f"Día {day_num} - Calendario de Adviento Shanghai 2025"
    day_description = f"Sorpresa del día {day_num} para nuestro viaje a Shanghai"
    
    app.add_page(
        lambda day=day_num: day_detail(day),
        route=f"/day/{day_num}",
        title=day_title,
        description=day_description,
        image=preview,
        meta=[
            {"name": "og:type", "content": "website"},
            {"name": "og:title", "content": day_title},
            {"name": "og:description", "content": day_description},
            {"name": "og:image", "content": preview},
            {"name": "twitter:card", "content": "summary_large_image"},
            {"name": "twitter:site", "content": "@shanghaiadvent"}
        ]
    )
