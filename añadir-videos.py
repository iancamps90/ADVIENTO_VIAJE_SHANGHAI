#!/usr/bin/env python3
"""
Script para añadir videos de YouTube y expandir contenido
Permite actualizar fácilmente los días con videos reales
"""

import re
import json
from typing import Dict, List

def extract_youtube_id(url: str) -> str:
    """Extrae el ID del video de YouTube de una URL"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
        r'youtube\.com\/watch\?.*v=([^&\n?#]+)',
        r'youtu\.be\/([^&\n?#]+)',
        r'youtube\.com\/embed\/([^&\n?#]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return url  # Si no se puede extraer, devolver la URL original

def create_video_embed_url(video_id: str) -> str:
    """Crea la URL de embed de YouTube"""
    return f"https://www.youtube.com/embed/{video_id}"

def update_day_video(day_number: int, video_url: str, description: str = "") -> Dict:
    """Actualiza el video de un día específico"""
    video_id = extract_youtube_id(video_url)
    embed_url = create_video_embed_url(video_id)
    
    return {
        "day": day_number,
        "video_url": video_url,
        "video_id": video_id,
        "embed_url": embed_url,
        "description": description,
        "status": "updated"
    }

# Plantilla para añadir videos por categoría
VIDEOS_POR_CATEGORIA = {
    "preparacion": {
        "temas": [
            "Apps esenciales (Alipay, WeChat)",
            "Documentos y seguros",
            "Transporte en Shanghai",
            "Lugares imprescindibles"
        ],
        "tipos_videos": [
            "Tutoriales de apps",
            "Guías de documentos",
            "Tours del metro",
            "Guías de lugares"
        ]
    },
    
    "cultura": {
        "temas": [
            "Idioma chino básico",
            "Tradiciones chinas",
            "Comida china auténtica",
            "Arte y cultura"
        ],
        "tipos_videos": [
            "Lecciones de chino",
            "Documentales culturales",
            "Recetas y comida",
            "Arte y museos"
        ]
    },
    
    "experiencia": {
        "temas": [
            "Vida nocturna",
            "Comida callejera",
            "Arquitectura moderna",
            "Parques y naturaleza"
        ],
        "tipos_videos": [
            "Tours nocturnos",
            "Street food tours",
            "Arquitectura urbana",
            "Parques y jardines"
        ]
    },
    
    "final": {
        "temas": [
            "Últimos preparativos",
            "Nochebuena especial",
            "Día del viaje",
            "Llegada a Shanghai"
        ],
        "tipos_videos": [
            "Checklist final",
            "Celebraciones",
            "Aeropuerto y vuelos",
            "Primeros pasos en Shanghai"
        ]
    }
}

# Función para generar contenido con video
def generate_day_with_video(day_number: int, tema: str, video_url: str, categoria: str) -> str:
    """Genera el código Python para un día con video"""
    
    video_id = extract_youtube_id(video_url)
    embed_url = create_video_embed_url(video_id)
    
    # Plantilla base
    template = f'''    (
        "{tema}",
        "¡Mensaje principal del día!

**Reto del día:** [Acción específica]

**¿Por qué es importante?** [Explicación]

**¿Qué nos espera?** [Expectativas]

**Dato curioso:** [Información interesante]",
        "Frase motivacional del día ✨",
        "📋 **Checklist del día:**
• ✅ Tarea 1
• ✅ Tarea 2
• ✅ Tarea 3

💡 **Tip del día:** [Consejo útil]",
        "{embed_url}",
        "/calendar_enhanced/{day_number}.png"
    ),'''
    
    return template

def main():
    """Función principal"""
    print("🎥 AÑADIR VIDEOS AL CALENDARIO SHANGHAI 🏮")
    print("=" * 50)
    
    print("\n📋 CATEGORÍAS DISPONIBLES:")
    for categoria, info in VIDEOS_POR_CATEGORIA.items():
        print(f"\n🎯 {categoria.upper()}:")
        for tema in info["temas"]:
            print(f"  • {tema}")
    
    print("\n🎥 TIPOS DE VIDEOS QUE NECESITAMOS:")
    print("• Tutoriales de apps chinas")
    print("• Documentales de Shanghai")
    print("• Guías de comida callejera")
    print("• Tours virtuales de lugares")
    print("• Lecciones de chino básico")
    print("• Recetas de Shanghai")
    print("• Guías del metro")
    print("• Arquitectura moderna")
    print("• Vida nocturna")
    print("• Tradiciones chinas")
    
    print("\n📝 FORMATO PARA ENVIARME VIDEOS:")
    print("""
DÍA X: [TÍTULO DEL DÍA]
Video: https://www.youtube.com/watch?v=[ID]
Tema: [Descripción del video]
Duración: [X minutos]
Por qué es perfecto: [Explicación]
Categoría: [preparacion/cultura/experiencia/final]
""")
    
    print("\n🔧 FUNCIONES DISPONIBLES:")
    print("• extract_youtube_id(url) - Extrae ID del video")
    print("• create_video_embed_url(id) - Crea URL de embed")
    print("• update_day_video(day, url, desc) - Actualiza día")
    print("• generate_day_with_video(day, tema, url, cat) - Genera código")

if __name__ == "__main__":
    main()
