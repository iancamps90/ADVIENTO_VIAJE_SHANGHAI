import reflex as rx
import datetime
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import TextColor
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
from adeviento_web.components.day import day


# Contenido personalizado para el viaje a Shanghai - 25 días de sorpresas
# Estructura: (título, mensaje, frase_motivacional, recomendaciones, video_youtube, foto_url)
_shanghai_days = [
    (
        "🏮 DÍA 1: CUENTA ATRÁS 🐉",
        """🎯 **OBJETIVO:** Mentalizarse para el viaje.

🧳 **PREPARATIVOS:**
• 📄 Revisa pasaporte (validez > 6 meses).
• 📱 Descarga WeChat y Alipay.
• 🎒 Empieza lista de maleta.

💡 **TIP:** Shanghai significa 'Sobre el mar'.

🎥 **VIDEO:** Presentación "Aventurero rumbo a Shanghai".""",
        "La aventura comienza con un solo paso.",
        """💡 **DATO:** Shanghai tiene 24M habitantes.

🎯 **TO-DO:**
• Cambiar foto perfil (tema Shanghai).
• Compartir emoción en grupo.""",
        "https://www.youtube.com/embed/YgL2XPZBMys",
        "/calendar_enhanced/1.png"
    ),
    (
        "💳 DÍA 2: APPS ESENCIALES 📱",
        """🎯 **OBJETIVO:** Configurar pagos y mapas.

🧳 **PREPARATIVOS:**
• 💳 Activa Tour Pass en Alipay.
• 🗺️ Descarga Baidu Maps (Google Maps falla).
• 🔌 Revisa adaptadores (tipo A, I, C).

💡 **TIP:** En China TODO se paga con móvil.

🎥 **VIDEO:** Configurando Alipay.""",
        "La preparación es clave.",
        """📱 **APPS MUST-HAVE:**
• Alipay (Pagos/Metro)
• WeChat (WhatsApp chino)
• Google Translate
• Baidu Maps

💡 **DATO:** Casi nadie usa efectivo ya.""",
        "https://www.youtube.com/embed/KNMz8WqRS-w",
        "/calendar_enhanced/2.png"
    ),
    (
        "🏮 DÍA 3: CURIOSIDADES 🏙️",
        """🎯 **OBJETIVO:** Conocer la ciudad.

🧳 **PREPARATIVOS:**
• 🏥 Botiquín básico (Ibuprofeno, Fortasec).
• 🧴 Gel hidroalcohólico.
• 🗣️ Prueba traducción con cámara de Google.

💡 **TIP:** El metro es la mejor forma de moverse.

🎥 **VIDEO:** Reacción a fotos de Shanghai.""",
        "Un viaje se empieza con los ojos.",
        """🏙️ **CURIOSIDADES:**
• Skyline más iluminado del mundo.
• Dumplings en cada esquina.

🧠 **CULTURA:** No claves los palillos en el arroz (es de mala educación).""",
        "https://www.youtube.com/embed/L_jWHffIx5E",
        "/calendar_enhanced/3.png"
    ),
    (
        "📄 DÍA 4: DOCUMENTOS ✈️",
        """🎯 **OBJETIVO:** Papeles en regla.

🧳 **PREPARATIVOS:**
• 📄 Copia digital de pasaporte en nube/email.
• 🏥 Seguro de viaje (imprescindible).
• 🎫 Billetes descargados offline.

💡 **TIP:** Lleva siempre una copia física del pasaporte.

🎥 **VIDEO:** Revisando documentos.""",
        "Viajero precavido vale por dos.",
        """📄 **CHECKLIST:**
• Pasaporte (+6 meses)
• Seguro
• Vuelos
• Reservas hotel

🛡️ **CONSEJO:** Ten a mano teléfonos de emergencia.""",
        "https://www.youtube.com/embed/H3HrJgYtjjY",
        "/calendar_enhanced/4.png"
    ),
    (
        "🍜 DÍA 5: GASTRONOMÍA 🥢",
        """🎯 **OBJETIVO:** Preparar el paladar.

🧳 **PREPARATIVOS:**
• 🥢 Practica con palillos.
• 📱 App Dianping (para restaurantes).
• 📝 Lista de platos a probar.

💡 **TIP:** El Xiaolongbao es el rey de Shanghai.

🎥 **VIDEO:** Probando comida china local.""",
        "La comida conecta culturas.",
        """🍜 **PLATOS TOP:**
• Xiaolongbao (dumplings sopa)
• Shengjianbao (pan frito)
• Pato laqueado

🥢 **CULTURA:** Sorber la sopa es señal de que te gusta.""",
        "https://www.youtube.com/embed/f1yIX7EMhQE",
        "/calendar_enhanced/5.png"
    ),
    (
        "🚇 DÍA 6: TRANSPORTE 🚌",
        """🎯 **OBJETIVO:** Moverse como un local.

🧳 **PREPARATIVOS:**
• 📱 Descarga Shanghai Metro App.
• 🗺️ Planifica ruta hotel-centro.
• 💳 Vincula Alipay para pagar metro.

💡 **TIP:** Evita horas punta (8-9am, 6-7pm).

🎥 **VIDEO:** Cómo usar el metro en China.""",
        "El camino es parte del destino.",
        """🚇 **TRANSPORTE:**
• Metro: Rápido, barato, en inglés.
• Didi: El Uber chino (baratísimo).
• Maglev: Tren más rápido del mundo (430km/h).

💡 **DATO:** El metro de Shanghai es el más largo del mundo.""",
        "https://www.youtube.com/embed/XVvhsfVz-WE",
        "/calendar_enhanced/6.png"
    ),
    (
        "🏛️ DÍA 7: IMPRESCINDIBLES 🎯",
        """🎯 **OBJETIVO:** Definir el Top 3.

🧳 **PREPARATIVOS:**
• 🗺️ Ubica: The Bund, Yu Garden, Lujiazui.
• 🎫 Revisa si necesitas reservar entradas.
• 📸 Prepara batería extra.

💡 **TIP:** El Bund es mejor al atardecer.

🎥 **VIDEO:** Top 10 cosas que ver en Shanghai.""",
        "Colecciona momentos, no cosas.",
        """🏛️ **MUST-SEE:**
• The Bund (Vistas skyline)
• Yu Garden (Jardín clásico)
• Shanghai Tower (Vistas desde arriba)
• Templo Jing'an (Budista moderno)

💡 **DATO:** La Shanghai Tower tiene 632m.""",
        "https://www.youtube.com/embed/hk43UekQG4A",
        "/calendar_enhanced/7.png"
    ),
    (
        "🗣️ DÍA 8: IDIOMA BÁSICO 📚",
        """🎯 **OBJETIVO:** Sobrevivir en chino.

🧳 **PREPARATIVOS:**
• 📱 Google Translate (descarga idioma offline).
• 🗣️ Aprende: Ni hao, Xie xie.
• 📸 Usa el traductor de cámara.

💡 **TIP:** Sonríe, ayuda más que el idioma.

🎥 **VIDEO:** Frases básicas en chino.""",
        "El idioma del respeto es universal.",
        """🗣️ **DICCIONARIO EXPRESS:**
• Ni hao = Hola
• Xie xie = Gracias
• Zai jian = Adiós
• Duo shao qian? = ¿Cuánto cuesta?
• Ting bu dong = No entiendo

💡 **DATO:** El tono cambia el significado.""",
        "https://www.youtube.com/embed/yiXNOAdXlzk",
        "/calendar_enhanced/8.png"
    ),
    (
        "🏮 DÍA 9: TRADICIONES 🎊",
        """🎯 **OBJETIVO:** Entender la cultura.

🧳 **PREPARATIVOS:**
• 🧧 Investiga sobre el Año Nuevo Chino.
• 🔴 El rojo es el color de la suerte.
• 🐉 2025 es el año de la Serpiente (o Dragón según toque).

💡 **TIP:** Nunca regales relojes (significa muerte).

🎥 **VIDEO:** Tradiciones chinas explicadas.""",
        "La cultura es el alma de un pueblo.",
        """🏮 **CURIOSIDADES:**
• 8 es número de la suerte (riqueza).
• 4 es mala suerte (muerte).
• Agua caliente: La beben para todo.

💡 **DATO:** El Año Nuevo Chino cambia de fecha cada año.""",
        "https://www.youtube.com/embed/AHpT7aCB4pY",
        "/calendar_enhanced/9.png"
    ),
    (
        "🛍️ DÍA 10: COMPRAS 💰",
        """🎯 **OBJETIVO:** Souvenirs y regateo.

🧳 **PREPARATIVOS:**
• 🎒 Lleva una maleta vacía (o casi).
• 💴 Aprende a decir "Tai gui le" (muy caro).
• 📱 Calculadora en mano para negociar.

💡 **TIP:** ¡REGATEA! Empieza ofreciendo el 20-30%.

🎥 **VIDEO:** Guía de compras en Shanghai.""",
        "Quien no llora, no mama (versión china).",
        """🛍️ **ZONAS DE COMPRAS:**
• Nanjing Road: La más famosa (turística).
• Mercado de imitaciones (AP Plaza).
• Tianzifang: Artesanía y cosas cuquis.

💡 **DATO:** Nanjing Road tiene 5.5km de tiendas.""",
        "https://www.youtube.com/embed/shanghai-shopping-guide",
        "/calendar_enhanced/10.png"
    ),
    (
        "🎨 DÍA 11: ARTE Y CULTURA 🏛️",
        """🎯 **OBJETIVO:** Inspirarse.

🧳 **PREPARATIVOS:**
• 🏛️ Reserva Museo de Shanghai (WeChat).
• 📅 Evita los lunes (suelen cerrar).
• 📸 Cámara lista para M50.

💡 **TIP:** Muchos museos son gratis pero requieren reserva.

🎥 **VIDEO:** Arte contemporáneo en Shanghai.""",
        "El arte lava del alma el polvo de la vida cotidiana.",
        """🎨 **LUGARES CULTURALES:**
• Museo de Shanghai (Clásico).
• Power Station of Art (Moderno).
• M50 Creative Park (Hipster/Graffiti).
• Tianzifang (Callejuelas artísticas).

💡 **DATO:** M50 era una antigua fábrica textil.""",
        "https://www.youtube.com/embed/hxVfrYNVO8A",
        "/calendar_enhanced/11.png"
    ),
    (
        "🎵 DÍA 12: ENTRETENIMIENTO 🎪",
        """🎯 **OBJETIVO:** Cantar en un KTV.

🧳 **PREPARATIVOS:**
• 🎤 Prepara tu canción estrella.
• 👯‍♂️ El KTV se hace en salas privadas con amigos.
• 🎪 Revisa horarios del Circo de Shanghai.

💡 **TIP:** En China el karaoke es sagrado.

🎥 **VIDEO:** Qué es un KTV en China.""",
        "La música es el lenguaje de las emociones.",
        """🎵 **QUÉ HACER:**
• Ir a un KTV (Karaoke).
• Ver el show acrobático ERA.
• Jazz en el Peace Hotel.

💡 **DATO:** Los KTV tienen buffet de comida incluido a veces.""",
        "https://www.youtube.com/embed/shanghai-entertainment",
        "/calendar_enhanced/12.png"
    ),
    (
        "🍜 DÍA 13: COMIDA CALLEJERA 🍢",
        """🎯 **OBJETIVO:** Comer en la calle.

🧳 **PREPARATIVOS:**
• 🍢 Busca puestos con cola (señal de calidad).
• 🥤 Lleva agua embotellada siempre.
• 🧻 Lleva pañuelos (servilletas no siempre hay).

💡 **TIP:** Jianbing es el mejor desayuno del mundo.

🎥 **VIDEO:** Street food tour Shanghai.""",
        "La mejor comida no siempre necesita mantel.",
        """🍢 **MUST-TRY:**
• Jianbing (Crepe chino).
• Tanghulu (Brocheta fruta caramelizada).
• Stinky Tofu (Si te atreves...).
• Bubble Tea (Origen asiático).

💡 **DATO:** El desayuno se vende hasta las 9-10am.""",
        "https://www.youtube.com/embed/shanghai-street-food",
        "/calendar_enhanced/13.png"
    ),
    (
        "💻 DÍA 14: TECNOLOGÍA 🤖",
        """🎯 **OBJETIVO:** Vivir el Cyberpunk.

🧳 **PREPARATIVOS:**
• 🔋 Powerbank de gran capacidad.
• 🤖 Busca tiendas de electrónica en Xujiahui.
• 🚄 Maglev al aeropuerto (si no lo has probado).

💡 **TIP:** Hay robots que te sirven comida en algunos sitios.

🎥 **VIDEO:** Tecnología futurista en China.""",
        "El futuro ya está aquí.",
        """💻 **TECH SPOTS:**
• Tienda insignia de Huawei/Xiaomi.
• Tren Maglev (430 km/h).
• Robots repartidores en hoteles.

💡 **DATO:** China lidera en pagos móviles e IA.""",
        "https://www.youtube.com/embed/shanghai-technology-innovation",
        "/calendar_enhanced/14.png"
    ),
    (
        "🌃 DÍA 15: VIDA NOCTURNA 🍸",
        """🎯 **OBJETIVO:** Ver Shanghai iluminado.

🧳 **PREPARATIVOS:**
• 👗 Ropa un poco más arreglada ("Smart Casual").
• 🍸 Presupuesto para un cóctel con vistas.
• 🆔 Pasaporte (a veces lo piden en clubs).

💡 **TIP:** Las luces del Bund se apagan a las 10-11pm.

🎥 **VIDEO:** Shanghai de noche.""",
        "La ciudad nunca duerme.",
        """🌃 **MEJORES VISTAS:**
• Bar Rouge (Clásico, caro, vistas top).
• Flair Rooftop (Ritz-Carlton).
• Paseo por el Bund (Gratis y espectacular).

💡 **DATO:** La electricidad del skyline cuesta millones.""",
        "https://www.youtube.com/embed/dsVDXeGNh8M",
        "/calendar_enhanced/15.png"
    ),
    (
        "🏃‍♂️ DÍA 16: DEPORTES 🧘‍♀️",
        """🎯 **OBJETIVO:** Mover el esqueleto.

🧳 **PREPARATIVOS:**
• 👟 Zapatillas cómodas (vas a andar mucho).
• 🧘‍♀️ Madruga para ver Tai Chi en el parque.
• 🚴‍♂️ Alquila una bici compartida.

💡 **TIP:** En los parques verás gente bailando y haciendo ejercicio.

🎥 **VIDEO:** Tai Chi en Shanghai.""",
        "Mens sana in corpore sano.",
        """🏃‍♂️ **ACTIVIDADES:**
• Tai Chi en el Bund (amanecer).
• Bici por la Concesión Francesa.
• Bádminton (deporte nacional).

💡 **DATO:** El ping-pong es religión aquí.""",
        "https://www.youtube.com/embed/S1QzWUb4SnQ",
        "/calendar_enhanced/16.png"
    ),
    (
        "🏗️ DÍA 17: ARQUITECTURA 🏙️",
        """🎯 **OBJETIVO:** Mirar hacia arriba.

🧳 **PREPARATIVOS:**
• 📸 Lente gran angular (si tienes).
• 🏙️ Sube a un mirador (SWFC o Shanghai Tower).
• 🔭 Prismáticos (opcional).

💡 **TIP:** El "Abrebotellas" es el SWFC.

🎥 **VIDEO:** Rascacielos de Shanghai.""",
        "La arquitectura es música congelada.",
        """🏗️ **ICONOS:**
• Shanghai Tower (632m).
• SWFC "Abrebotellas" (492m).
• Jin Mao Tower (420m).
• Oriental Pearl Tower (468m).

💡 **DATO:** La Shanghai Tower tiene el ascensor más rápido.""",
        "https://www.youtube.com/embed/51Op3A-8HSA",
        "/calendar_enhanced/17.png"
    ),
    (
        "🌿 DÍA 18: NATURALEZA 🌸",
        """🎯 **OBJETIVO:** Relax Zen.

🧳 **PREPARATIVOS:**
• 🍵 Visita una casa de té tradicional.
• 🌸 Yu Garden (imprescindible).
• 🦟 Repelente (en verano).

💡 **TIP:** Yu Garden tiene 400 años de historia.

🎥 **VIDEO:** Jardines clásicos chinos.""",
        "La naturaleza no se apresura, todo se logra.",
        """🌿 **OASIS URBANOS:**
• Yu Garden (Jardín Yuyuan).
• Century Park (el más grande).
• Fuxing Park (estilo francés).

💡 **DATO:** El diseño de jardines busca armonía (Feng Shui).""",
        "https://www.youtube.com/embed/SkWSR6EgS3I",
        "/calendar_enhanced/18.png"
    ),
    (
        "💭 DÍA 19: RECUERDOS ✨",
        """🎯 **OBJETIVO:** Inmortalizar el viaje.

🧳 **PREPARATIVOS:**
• 📮 Compra sellos y postales.
• 📝 Escribe un diario de viaje.
• 📸 Imprime alguna foto allí mismo.

💡 **TIP:** Envíate una postal a ti mismo para recibirla al volver.

🎥 **VIDEO:** Recuerdos de viaje.""",
        "Los recuerdos son el único paraíso del que no podemos ser expulsados.",
        """💭 **IDEAS:**
• Sellos personalizados (talla tu nombre).
• Diario de viaje.
• Fotos con locales (pide permiso).

💡 **DATO:** El correo chino es bastante fiable.""",
        "https://www.youtube.com/embed/memories-shanghai",
        "/calendar_enhanced/19.png"
    ),
    (
        "🎒 DÍA 20: MALETA FINAL ✈️",
        """🎯 **OBJETIVO:** Tetris nivel experto.

🧳 **PREPARATIVOS:**
• ⚖️ Pesa la maleta (ojo con el sobrepeso).
• 🔒 Candado TSA.
• 🏷️ Etiqueta con tus datos.

💡 **TIP:** Deja espacio para compras (o lleva bolsa extra).

🎥 **VIDEO:** Cómo hacer la maleta perfecta.""",
        "Viaja ligero, vive intenso.",
        """🎒 **CHECKLIST FINAL:**
• Pasaporte y Visado (si aplica).
• Powerbank (siempre en equipaje de mano).
• Medicinas.
• Adaptador enchufes.

💡 **DATO:** Las baterías de litio NO pueden ir facturadas.""",
        "https://www.youtube.com/embed/travel-packing-guide",
        "/calendar_enhanced/20.png"
    ),
    (
        "💪 DÍA 21: MOTIVACIÓN 🚀",
        """🎯 **OBJETIVO:** Visualizar el éxito.

🧳 **PREPARATIVOS:**
• 🛌 Duerme bien (acumula sueño).
• 🏠 Deja la casa ordenada.
• 🗑️ Tira la basura antes de irte.

💡 **TIP:** Shanghai está a 9,000 km.

🎥 **VIDEO:** Motivación viajera.""",
        "La magia sucede fuera de tu zona de confort.",
        """💪 **MENTALIDAD:**
• Abraza la incertidumbre.
• Sé flexible.
• Disfruta cada contratiempo (es una anécdota).

💡 **DATO:** El huso horario es GMT+8.""",
        "https://www.youtube.com/embed/motivation-travel",
        "/calendar_enhanced/21.png"
    ),
    (
        "⏰ DÍA 22: 3 DÍAS... 🎯",
        """🎯 **OBJETIVO:** No entrar en pánico.

🧳 **PREPARATIVOS:**
• ✈️ Check-in online (si está disponible).
• 📱 Descarga pelis/series para el vuelo.
• 🍬 Compra chicles/snacks.

💡 **TIP:** Revisa el tiempo en Shanghai una última vez.

🎥 **VIDEO:** Cuenta atrás final.""",
        "La emoción es el mejor equipaje.",
        """⏰ **ÚLTIMOS PASOS:**
• Confirmar transporte al aeropuerto.
• Avisar a familia/amigos.
• Desactivar datos móviles (para no tener roaming sorpresa).

💡 **DATO:** El vuelo será largo, pero vale la pena.""",
        "https://www.youtube.com/embed/countdown-shanghai",
        "/calendar_enhanced/22.png"
    ),
    (
        "🎄 DÍA 23: ÚLTIMA NOCHE 🏮",
        """🎯 **OBJETIVO:** Despedida.

🧳 **PREPARATIVOS:**
• 🔋 Carga TODO al 100%.
• 🚿 Ducha relajante.
• ⏰ Pon la alarma (dos veces).

💡 **TIP:** Deja la ropa de viaje preparada fuera.

🎥 **VIDEO:** Preparación final.""",
        "Mañana empieza todo.",
        """🎄 **CHECK FINAL:**
• ¿Pasaporte? Sí.
• ¿Móvil? Sí.
• ¿Ganas? ¡TODAS!

💡 **DATO:** Mañana cenamos en el aire.""",
        "https://www.youtube.com/embed/b1LkyFaXHtI",
        "/calendar_enhanced/23.png"
    ),
    (
        "🎅 DÍA 24: NOCHEBUENA ✈️",
        """🎯 **OBJETIVO:** Aeropuerto y Vuelo.

🧳 **PREPARATIVOS:**
• 🚗 Salida hacia Madrid (3 AM).
• ✈️ Vuelo a las 10:00 AM.
• 😴 Intenta dormir en el avión.

💡 **TIP:** Bebe mucha agua en el vuelo.

🎥 **VIDEO:** Brindis navideño.""",
        "Navidad en las nubes.",
        """🎅 **ITINERARIO:**
• 03:00 - Salida a MAD.
• 10:00 - Despegue.
• Todo el día - Volando voy, volando vengo.

💡 **DATO:** Cruzaremos 7 zonas horarias.""",
        "https://www.youtube.com/embed/9bZkp7q19f0",
        "/calendar_enhanced/24.png"
    ),
    (
        "✈️ DÍA 25: EL VUELO 🎊",
        """🎯 **OBJETIVO:** Aterrizar.

🧳 **PREPARATIVOS:**
• 🧘‍♀️ Estira las piernas cada 2h.
• 🧴 Hidrata tu piel.
• 🎧 Usa cancelación de ruido.

💡 **TIP:** Ajusta tu reloj a hora Shanghai ya.

🎥 **VIDEO:** Vlog de vuelo.""",
        "Shanghai nos espera.",
        """✈️ **EN EL AIRE:**
• Películas.
• Comida de avión (yum?).
• Dormir (intentarlo).

💡 **DATO:** Llegaremos mañana por la mañana (hora local).""",
        "https://www.youtube.com/embed/WJd-BopESW0",
        "/calendar_enhanced/25.png"
    ),
    (
        "🏮 DÍA 26: ¡HOLA SHANGHAI! ✨",
        """🎯 **OBJETIVO:** Sobrevivir al Jet Lag.

🧳 **PREPARATIVOS:**
• 🛂 Control de pasaportes (paciencia).
• 🛄 Recoger maletas.
• 🚇 Maglev al centro.

💡 **TIP:** ¡NO TE DUERMAS hasta la noche!

🎥 **VIDEO:** Llegada a Shanghai.""",
        "Un sueño cumplido.",
        """🏮 **PRIMEROS PASOS:**
• Sacar dinero / Pagar con Alipay.
• Check-in hotel.
• Ver el Bund de noche.

💡 **DATO:** ¡ESTAMOS EN CHINA!""",
        "https://www.youtube.com/embed/WJd-BopESW0",
        "/calendar_enhanced/26.png"
    )
]

_current_day = len(_shanghai_days) - 1  # Ahora tenemos 26 días (1-25 + llegada el 26)


def _is_day_available(day_number: int) -> bool:
    """
    Determina si un día está disponible para ver.
    Solo se pueden ver días que ya han pasado + el día actual.
    Día 1 = 1 de diciembre, Día 25 = 25 de diciembre
    """
    today = datetime.date.today()
    current_year = today.year
    
    # Para testing: desbloquear todos los días (cambiar a False para producción)
    TESTING_MODE = False
    if TESTING_MODE:
        return True
    
    # Si estamos en 2024, todos los días están bloqueados
    if current_year < 2025:
        return False
    
    # Si estamos en 2025, verificar el día
    if current_year == 2025:
        # Día 1 = 1 de diciembre, Día 25 = 25 de diciembre
        if today.month == 12:
            return today.day >= day_number
        elif today.month < 12:
            return False
        else:
            return True  # Después de diciembre 2025
    
    # Si estamos en 2026 o después, todos los días están disponibles
    return True


def _get_current_available_day() -> int:
    """
    Obtiene el día actual disponible (el último día que se puede ver)
    """
    today = datetime.date.today()
    current_year = today.year
    
    if current_year < 2025:
        return 0  # Ningún día disponible
    
    if current_year == 2025:
        # Si estamos en diciembre, el día actual
        if today.month == 12:
            return min(today.day, 25)
        # Si estamos antes de diciembre, ningún día
        elif today.month < 12:
            return 0
        # Si estamos después de diciembre, todos los días
        else:
            return 25
    
    # Si estamos en 2026 o después, todos los días
    return 25


def calendar() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Camino a Shanghai 🇨🇳 🐉",
            size={
                "initial": "6",
                "xs": "7", 
                "sm": "8",
                "md": "9",
                "lg": "9",
                "xl": "9"
            },
            color="#DC143C",
            class_name="chinese-text",
            text_align="center",
            text_shadow="3px 3px 6px rgba(0,0,0,0.8)",
            background="rgba(255,255,255,0.1)",
            padding="1em 2em",
            border_radius="15px",
            border="2px solid #DC143C",
            margin_bottom="1em"
        ),
        # rx.vstack(
        #     rx.text(
        #         "El regalo de hoy",
        #         class_name="title",
        #         color=TextColor.ACCENT.value
        #     ),
        #     rx.flex(
        #         rx.box(
        #             day(
        #                 _current_day + 1,
        #                 _gift_name(_current_day),
        #                 _gift_url(_current_day),
        #             ),
        #             height="14em",
        #             width="14em",
        #             aspect_ratio="1",
        #             margin_right=Size.BIG.value
        #         ),
        #         rx.vstack(
        #             rx.el.span(
        #                 f"Día {_current_day + 1}"),
        #             rx.link(
        #                 _gift_name(_current_day),
        #                 href=_gift_info(_current_day),
        #                 is_external=True
        #             ),
        #             rx.spacer(),
        #             rx.flex(
        #                 button(
        #                     "Participa",
        #                     _gift_url(_current_day)
        #                 ),
        #                 rx.cond(
        #                     _current_day > 1,
        #                     button(
        #                         f"Día {_current_day}",
        #                         _gift_url(_current_day - 1)
        #                     )
        #                 ),
        #                 align_items="start",
        #                 flex_direction=styles.FLEX_DIRECTION
        #             ),
        #             align_items="start",
        #             margin_top=Size.BIG.value
        #         ),
        #         flex_direction=styles.FLEX_DIRECTION
        #     ),
        #     width="100%",
        #     class_name="nes-container is-dark with-title",
        #     align_items="start"
        # ),
        rx.grid(
            *[
                day(
                    number + 1,
                    _shanghai_day_name(number),
                    _shanghai_day_url(number),
                    _is_day_available(number + 1),  # Estado de disponibilidad
                )
                for _, number in enumerate(range(0, len(_shanghai_days)))
            ],
            columns={
                "initial": "2",
                "xs": "3", 
                "sm": "4",
                "md": "5",
                "lg": "5",
                "xl": "5"
            },
            spacing="3",
            width="100%",
            padding_y=Size.BIG.value,
            class_name="calendar-container calendar-grid"
        ),
        # rx.vstack(
        #     rx.hstack(
        #         rx.text(
        #             "Próximo regalo y ganadores en",
        #             # "Calendario 2024 en",
        #             margin_right=Size.DEFAULT.value
        #         ),
        #         rx.text(
        #             id="countdown",
        #             margin_left=Size.ZERO.value
        #         ),
        #         align_items="start",
        #         flex_direction=styles.FLEX_DIRECTION
        #     ),
        #     # button(
        #     #     "Recordar",
        #     #     constants.DISCORD_EVENT_URL
        #     # ),
        #     rx.el.span(
        #         "• Los regalos son sorpresa, permanecerán ocultos hasta el día de su publicación. No olvides pasarte por aquí cada día para descubrir un nuevo sorteo."
        #     ),
        #     rx.el.span(
        #         "• Puedes seleccionar cada regalo para conocer a los ganadores una vez se haya publicado el nuevo sorteo (aparecerá en rojo)."
        #     ),
        #     class_name="nes-container is-dark",
        #     align_items="start",
        #     width="100%"
        # ),
        # rx.script(src="/js/countdown.js"),
        style=styles.max_width_style
    )


def _shanghai_day_name(day_index) -> str:
    if len(_shanghai_days) > day_index:
        return _shanghai_days[day_index][0]
    return ""


def _shanghai_day_url(day_index) -> str:
    if len(_shanghai_days) > day_index:
        return f"/day/{day_index + 1}"  # URL de la página del día
    return ""


def _shanghai_day_message(day_index) -> str:
    if len(_shanghai_days) > day_index:
        return _shanghai_days[day_index][1]  # Mensaje del día
    return ""


def _shanghai_day_motivation(day_index) -> str:
    if len(_shanghai_days) > day_index and len(_shanghai_days[day_index]) > 2:
        return _shanghai_days[day_index][2]  # Frase motivacional
    return ""


def _shanghai_day_recommendations(day_index) -> str:
    if len(_shanghai_days) > day_index and len(_shanghai_days[day_index]) > 3:
        return _shanghai_days[day_index][3]  # Recomendaciones
    return ""


def _shanghai_day_video(day_index) -> str:
    if len(_shanghai_days) > day_index and len(_shanghai_days[day_index]) > 4:
        return _shanghai_days[day_index][4]  # Video de YouTube
    return ""


def _shanghai_day_photo(day_index) -> str:
    if len(_shanghai_days) > day_index and len(_shanghai_days[day_index]) > 5:
        return _shanghai_days[day_index][5]  # Foto del día
    return ""
