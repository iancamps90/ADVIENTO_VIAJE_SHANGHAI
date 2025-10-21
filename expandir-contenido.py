#!/usr/bin/env python3
"""
Script para expandir el contenido de los días del calendario
Permite añadir fácilmente más información, videos y contenido
"""

import json
from typing import Dict, List, Tuple

# Estructura expandida para cada día
def create_expanded_day_structure() -> Dict:
    """Crea la estructura expandida para un día"""
    return {
        "titulo": "🎯 TÍTULO DEL DÍA 🏮",
        "mensaje_principal": """¡Mensaje principal del día!

**Reto del día:** [Acción específica y divertida]

**¿Por qué es importante?** [Explicación detallada]

**¿Qué nos espera?** [Expectativas y emociones]

**Dato curioso:** [Información interesante sobre Shanghai/China]

**¿Sabías que...?** [Dato adicional fascinante]""",
        
        "frase_motivacional": "Frase motivacional del día ✨",
        
        "contenido_detallado": """📋 **Checklist del día:**
• ✅ Tarea 1 específica
• ✅ Tarea 2 específica  
• ✅ Tarea 3 específica
• ✅ Tarea 4 específica

🍽️ **Gastronomía del día:**
• [Plato específico de Shanghai]
• [Restaurante recomendado]
• [Ingrediente especial]

🏛️ **Lugares del día:**
• [Lugar específico en Shanghai]
• [Horarios y precios]
• [Cómo llegar]

📱 **Apps y tecnología:**
• [App específica para el día]
• [Función importante]
• [Consejo de uso]

🎭 **Cultura y tradiciones:**
• [Tradición china específica]
• [Significado cultural]
• [Cómo participar]

💡 **Tip del día:** [Consejo súper útil]

🎯 **Reto extra:** [Desafío adicional opcional]""",
        
        "video_youtube": "https://www.youtube.com/embed/[VIDEO_ID]",
        "imagen_calendario": "/calendar_enhanced/[numero].png",
        
        # Campos adicionales
        "categoria": "preparacion",  # preparacion, cultura, experiencia, final
        "dificultad": "facil",  # facil, medio, dificil
        "tiempo_estimado": "15 minutos",
        "interactividad": "alta",  # baja, media, alta
        "tags": ["shanghai", "viaje", "aventura"],
        "contenido_extra": {
            "frases_chinas": [],
            "mapas": [],
            "enlaces_utiles": [],
            "fotos_adicionales": []
        }
    }

# Plantillas específicas por categoría
PLANTILLAS_POR_CATEGORIA = {
    "preparacion": {
        "titulo_template": "🎯 {tema} 🧳",
        "retos": [
            "Descarga la app {app} y comparte pantallazo",
            "Busca información sobre {tema} y compártela",
            "Haz una lista de {elemento} para el viaje",
            "Practica {habilidad} y comparte tu progreso"
        ],
        "tips": [
            "💡 Tip del día: {consejo}",
            "🔑 Clave del éxito: {clave}",
            "⚠️ Importante: {importante}",
            "🎯 Objetivo: {objetivo}"
        ]
    },
    
    "cultura": {
        "titulo_template": "🎭 {tema} 🏮",
        "retos": [
            "Aprende sobre {tradicion} y comparte un dato curioso",
            "Practica {habilidad_cultural} y comparte foto",
            "Investiga sobre {aspecto_cultural} de Shanghai",
            "Comparte una foto relacionada con {tema}"
        ],
        "tips": [
            "🏮 Tradición: {tradicion}",
            "📚 Cultura: {aspecto_cultural}",
            "🎨 Arte: {arte}",
            "🎪 Entretenimiento: {entretenimiento}"
        ]
    },
    
    "experiencia": {
        "titulo_template": "🌟 {tema} ✨",
        "retos": [
            "Planifica tu {experiencia} en Shanghai",
            "Busca fotos de {lugar} y compártelas",
            "Investiga precios de {actividad}",
            "Crea tu lista de {elemento} para Shanghai"
        ],
        "tips": [
            "🌟 Experiencia: {experiencia}",
            "📍 Lugar: {lugar}",
            "💰 Precio: {precio}",
            "⏰ Horario: {horario}"
        ]
    },
    
    "final": {
        "titulo_template": "🎊 {tema} 🚀",
        "retos": [
            "¡Últimos preparativos para {tema}!",
            "Revisa tu lista de {elemento}",
            "¡Comparte tu emoción por {tema}!",
            "¡Ya casi estamos en Shanghai!"
        ],
        "tips": [
            "🎊 ¡Último empujón!",
            "🚀 ¡Casi llegamos!",
            "🏮 ¡Shanghai nos espera!",
            "✨ ¡La aventura comienza!"
        ]
    }
}

# Generador de contenido automático
def generate_day_content(day_number: int, tema: str, categoria: str, video_id: str = None) -> Dict:
    """Genera contenido automático para un día específico"""
    
    plantilla = PLANTILLAS_POR_CATEGORIA.get(categoria, PLANTILLAS_POR_CATEGORIA["preparacion"])
    
    contenido = create_expanded_day_structure()
    contenido["titulo"] = plantilla["titulo_template"].format(tema=tema)
    contenido["categoria"] = categoria
    contenido["imagen_calendario"] = f"/calendar_enhanced/{day_number}.png"
    
    if video_id:
        contenido["video_youtube"] = f"https://www.youtube.com/embed/{video_id}"
    
    return contenido

# Ejemplos de contenido expandido
EJEMPLOS_EXPANDIDOS = {
    1: {
        "tema": "¡Empieza la cuenta atrás!",
        "categoria": "preparacion",
        "video_id": "dQw4w9WgXcQ",
        "contenido_extra": {
            "frases_chinas": ["你好 (Ni hao) - Hola", "谢谢 (Xie xie) - Gracias"],
            "mapas": ["Mapa de Shanghai", "Ubicación del hotel"],
            "enlaces_utiles": ["Guía oficial de Shanghai", "App del metro"],
            "fotos_adicionales": ["Skyline de Shanghai", "Bund al atardecer"]
        }
    },
    
    5: {
        "tema": "Comida china auténtica",
        "categoria": "cultura",
        "video_id": "9bZkp7q19f0",
        "contenido_extra": {
            "frases_chinas": ["我要这个 (Wo yao zhe ge) - Quiero esto", "好吃 (Hao chi) - Está rico"],
            "mapas": ["Mapa de restaurantes", "Mercados de comida"],
            "enlaces_utiles": ["Guía gastronómica", "Restaurantes recomendados"],
            "fotos_adicionales": ["Xiaolongbao", "Mercado de comida callejera"]
        }
    }
}

def main():
    """Función principal para generar contenido"""
    print("🏮 GENERADOR DE CONTENIDO EXPANDIDO - SHANGHAI 2025 🐉")
    print("=" * 60)
    
    # Mostrar ejemplos
    print("\n📋 EJEMPLOS DE CONTENIDO EXPANDIDO:")
    for dia, info in EJEMPLOS_EXPANDIDOS.items():
        print(f"\nDía {dia}: {info['tema']}")
        print(f"Categoría: {info['categoria']}")
        print(f"Video: {info['video_id']}")
        print(f"Frases chinas: {len(info['contenido_extra']['frases_chinas'])}")
    
    print("\n🎯 PLANTILLAS DISPONIBLES:")
    for categoria, plantilla in PLANTILLAS_POR_CATEGORIA.items():
        print(f"• {categoria.upper()}: {plantilla['titulo_template']}")
    
    print("\n📝 PARA USAR ESTE SCRIPT:")
    print("1. Define el tema del día")
    print("2. Selecciona la categoría")
    print("3. Añade el video de YouTube")
    print("4. Personaliza el contenido extra")
    print("5. Genera el contenido expandido")

if __name__ == "__main__":
    main()
