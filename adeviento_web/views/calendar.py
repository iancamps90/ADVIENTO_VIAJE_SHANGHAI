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
        "🎊 ¡Empieza la cuenta atrás! 🧳✈️🎯",
        "¡Bienvenidos a la aventura más épica del año! En 25 días estaremos en Shanghai. ¡Que empiece la magia! 🎊🏮\n\n**Reto del día:** Cambia tu fondo de pantalla por algo relacionado con Shanghai y mándalo al grupo. ¡Vamos a crear ambiente! 🔥\n\n**¿Listos para la aventura?** ¡Cada día una nueva sorpresa nos espera!",
        "La aventura comienza con un solo paso. ¡Y ese paso es hoy! 🚀",
        "📋 **Checklist del día:**\n• 📄 Revisa tu pasaporte (debe tener 6+ meses de validez)\n• 📱 Descarga apps útiles: Google Translate, Maps, Alipay\n• 🎒 Empieza a hacer lista de maletas\n• 🎯 Cambia fondo de pantalla y comparte en el grupo\n\n💡 **Tip del día:** Shanghai significa 'Sobre el mar' - ¡perfecto para nuestra aventura!",
        "https://www.youtube.com/embed/dQw4w9WgXcQ",
        "/calendar_enhanced/1.png"
    ),
    (
        "💳 Apps esenciales para Shanghai 📱",
        """¡Momento de ser responsables! Hoy toca preparar nuestro arsenal digital para conquistar Shanghai. 💪

**Reto del día:** Descarga Alipay y activa el Tour Pass. ¡Comparte pantallazo cuando lo tengas listo! 📸

**¿Por qué es importante?** En China se paga TODO con el móvil. ¡Sin Alipay no hay paraíso! 🏮

**¿Qué nos espera?** Un mundo digital completamente diferente donde el móvil es tu llave para todo.

**Dato curioso:** China tiene 1.4 mil millones de usuarios de pagos móviles. ¡Somos una gota en el océano!

**¿Sabías que...?** Alipay procesa más transacciones que Visa y Mastercard juntas.""",
        "La preparación es la clave del éxito. ¡Cada app descargada es un paso más cerca! 🔑",
        """📱 **Apps imprescindibles:**
• Alipay (pagos y transporte) - ¡LA MÁS IMPORTANTE!
• WeChat (comunicación local) - WhatsApp chino
• Google Translate (idioma) - Para traducir menús
• Maps (navegación) - Aunque Baidu Maps es mejor
• Didi (taxis) - Uber chino
• Dianping (restaurantes) - Yelp chino
• Meituan (delivery) - Para pedir comida

🍽️ **Gastronomía del día:**
• Aprende a pagar con Alipay
• Configura tu Tour Pass
• Practica escaneando códigos QR

🏛️ **Lugares del día:**
• Cualquier tienda para probar pagos
• Metro para activar transporte
• Restaurante para pedir comida

📱 **Apps y tecnología:**
• Alipay - Configuración desde cero
• WeChat Pay - Alternativa a Alipay
• Baidu Maps - Navegación local

🎭 **Cultura y tradiciones:**
• Pagos móviles como estilo de vida
• Códigos QR en todas partes
• Sin efectivo = normalidad

💡 **Tip del día:** Descarga Alipay ANTES de llegar a China

🎯 **Reto extra:** Graba un video pagando con Alipay""",
        "https://www.youtube.com/embed/KNMz8WqRS-w",
        "/calendar_enhanced/2.png"
    ),
    (
        "🏮 Curiosidades de Shanghai 🏙️",
        "¡Descubramos juntos los secretos de la ciudad más fascinante de China! 🌟\n\n**¿Sabías que...?**\n• Shanghai significa 'Sobre el mar' 🌊\n• Es la ciudad más poblada del mundo (24 millones) 👥\n• Tiene el metro más largo del planeta 🚇\n• El Bund es Patrimonio de la Humanidad 🏛️\n\n**Reto del día:** Busca una foto icónica de Shanghai y compártela con una frase motivacional! 📸✨",
        "La distancia se mide en historias que vas a vivir, no en kilómetros. ¡Shanghai nos espera! 🏮",
        "🎯 **Actividades del día:**\n• Visualiza el viaje perfecto\n• Comparte tu emoción con el grupo\n• ¡Mantén la actitud positiva!\n• Investiga sobre el Bund y la Torre de Shanghai\n\n💡 **Dato curioso:** El metro de Shanghai tiene 831 km de vías - ¡más que cualquier otra ciudad!",
        "https://www.youtube.com/embed/L_jWHffIx5E",
        "/calendar_enhanced/3.png"
    ),
    (
        "📄 Documentos y seguros ✈️",
        """¡Momento de ser súper organizados! Hoy toca revisar que tenemos todos los papeles en regla. 📋

**Reto del día:** Haz una foto de tu pasaporte (solo la portada) y compártela cuando esté todo listo. ¡Vamos a estar 100% preparados! 📸

**¿Por qué es crucial?** Sin documentos en regla, no hay viaje. ¡Mejor prevenir que lamentar! 🛡️

**¿Qué nos espera?** Un proceso de documentación que puede ser complejo pero es esencial.

**Dato curioso:** China requiere pasaporte con 6+ meses de validez. ¡Muchos países no lo saben!

**¿Sabías que...?** El seguro de viaje puede ahorrarte miles de euros en caso de emergencia.""",
        "La preparación es la clave del éxito en cualquier aventura. ¡Cada documento revisado es tranquilidad ganada! 📋",
        """📋 **Checklist de documentos:**
• ✅ Pasaporte con 6+ meses de validez
• ✅ Copias digitales de documentos importantes
• ✅ Seguro de viaje internacional
• ✅ Reservas de vuelo y hotel
• ✅ Visado (si es necesario)
• ✅ Certificado de vacunación
• ✅ Reservas de hotel confirmadas

🍽️ **Gastronomía del día:**
• Documentos para restaurantes
• Reservas en restaurantes especiales
• Información dietética importante

🏛️ **Lugares del día:**
• Embajada/consulado chino
• Oficina de seguros
• Aeropuerto (documentos de vuelo)

📱 **Apps y tecnología:**
• Apps de seguros de viaje
• Documentos digitales
• Traductor de documentos

🎭 **Cultura y tradiciones:**
• Documentos culturales importantes
• Permisos especiales
• Regulaciones locales

💡 **Tip del día:** Guarda copias en la nube y en el móvil - ¡nunca se sabe!

🎯 **Reto extra:** Crea una carpeta digital con todos tus documentos""",
        "https://www.youtube.com/embed/H3HrJgYtjjY",
        "/calendar_enhanced/4.png"
    ),
    (
        "🍜 Comida china auténtica 🥢",
        """¡Hora de preparar el estómago para la aventura culinaria más épica! 🍽️

**Reto del día:** Busca un restaurante chino en tu ciudad y pide algo que nunca hayas probado. ¡Comparte foto y experiencia! 📸

**¿Qué nos espera?** Dim sum, xiaolongbao, hot pot... ¡Shanghai es el paraíso de la comida callejera! 🌟

**¿Por qué es importante?** La comida es la puerta de entrada a la cultura china. ¡Cada plato cuenta una historia!

**Dato curioso:** Shanghai tiene más de 50,000 restaurantes. ¡Imposible probarlos todos en una vida!

**¿Sabías que...?** El xiaolongbao se inventó en Shanghai en 1875 y se come con una técnica especial para no quemarse.""",
        "La comida es el lenguaje universal que conecta culturas. ¡Cada bocado nos acerca más a Shanghai! 🥢",
        """📋 **Checklist del día:**
• ✅ Busca restaurante chino local
• ✅ Pide algo nuevo y desconocido
• ✅ Comparte foto y experiencia
• ✅ Investiga sobre xiaolongbao

🍽️ **Gastronomía del día:**
• Xiaolongbao (sopa en bolsita) - ¡EL PLATO ESTRELLA!
• Fideos de Shanghai - Tradición local
• Cangrejo de Shanghai - Delicatessen
• Mooncakes - Postre tradicional
• Té chino tradicional - Ceremonia

🏛️ **Lugares del día:**
• Yu Garden Bazaar - Comida tradicional
• Mercado de comida callejera
• Restaurantes del Bund
• Dim sum tradicional

📱 **Apps y tecnología:**
• Dianping (Yelp chino) - Reseñas
• Meituan (delivery) - Pedidos
• Alipay (pagos) - Pagar comida
• Google Translate (menús) - Traducir

🎭 **Cultura y tradiciones:**
• Etiqueta en restaurantes
• Uso de palillos correcto
• Compartir platos familiares
• Té chino como ritual

💡 **Tip del día:** Aprende a usar palillos - ¡será súper útil!

🎯 **Reto extra:** Graba un video comiendo con palillos""",
        "https://www.youtube.com/embed/f1yIX7EMhQE",
        "/calendar_enhanced/5.png"
    ),
    (
        "🚇 Transporte en Shanghai 🚌",
        """¡Hora de dominar el sistema de transporte más eficiente del mundo! 🚇

**Reto del día:** Descarga la app del metro de Shanghai y explora las líneas principales. ¡Comparte tu ruta favorita! 📱

**¿Sabías que?** El metro de Shanghai transporta 10+ millones de personas al día. ¡Vamos a ser parte de esa estadística! 📊

**¿Por qué es importante?** El transporte público es la clave para explorar Shanghai como un local.

**Dato curioso:** Shanghai tiene el metro más largo del mundo con 831 km de vías. ¡Más que cualquier otra ciudad!

**¿Sabías que...?** Puedes pagar el metro con Alipay escaneando códigos QR.""",
        "La emoción es el combustible de los grandes viajes. ¡Cada línea de metro nos lleva a una nueva aventura! 🚇",
        """📋 **Checklist del día:**
• ✅ Descarga app del metro de Shanghai
• ✅ Explora las líneas principales
• ✅ Planifica rutas favoritas
• ✅ Aprende a pagar con Alipay

🍽️ **Gastronomía del día:**
• Comida en estaciones de metro
• Vendedores ambulantes
• Tiendas de conveniencia

🏛️ **Lugares del día:**
• Estaciones principales del metro
• Línea 2 (cruza el río Huangpu)
• Estación de People's Square
• Estación de Nanjing Road

📱 **Apps y tecnología:**
• Metro Shanghai (oficial)
• Alipay (pagos QR)
• Baidu Maps (navegación)
• Didi (taxis alternativos)

🎭 **Cultura y tradiciones:**
• Etiqueta en el metro
• Horarios de pico
• Comportamiento local
• Tradiciones de transporte

💡 **Tip del día:** La línea 2 cruza el río Huangpu - ¡vistas espectaculares!

🎯 **Reto extra:** Graba un video pagando el metro con Alipay""",
        "https://www.youtube.com/embed/XVvhsfVz-WE",
        "/calendar_enhanced/6.png"
    ),
    (
        "🏛️ Lugares imprescindibles 🎯",
        """¡Hora de crear nuestra lista de deseos de Shanghai! 🗺️

**Reto del día:** Elige tu top 3 lugares que NO te puedes perder y compártelos con el grupo. ¡Vamos a planificar la aventura perfecta! 📸

**¿Cuáles son tus favoritos?** Bund, Torre de Shanghai, Templo del Buda de Jade... ¡Hay tanto que ver! 🌟

**¿Por qué es importante?** Shanghai tiene lugares icónicos que definen la ciudad. ¡No podemos perdérnoslos!

**Dato curioso:** El Bund tiene 52 edificios de diferentes estilos arquitectónicos. ¡Un museo al aire libre!

**¿Sabías que...?** La Torre de Shanghai es el segundo edificio más alto del mundo con 632 metros.""",
        "La comida es el lenguaje universal que conecta culturas. ¡Cada lugar que visitemos será una historia que contar! 🏛️",
        """📋 **Checklist del día:**
• ✅ Elige tu top 3 lugares
• ✅ Comparte con el grupo
• ✅ Planifica rutas
• ✅ Investiga horarios y precios

🍽️ **Gastronomía del día:**
• Restaurantes con vistas al Bund
• Comida en Yu Garden
• Cafés en Xintiandi
• Mercados de comida

🏛️ **Lugares imprescindibles:**
• 🌃 El Bund (paseo junto al río) - ¡ICÓNICO!
• 🗼 Torre de Shanghai (632m) - Vistas espectaculares
• 🏮 Templo del Buda de Jade - Tradición
• 🏛️ Museo de Shanghai - Cultura
• 🌸 Jardín Yuyuan - Historia
• 🎭 Distrito de Xintiandi - Modernidad

📱 **Apps y tecnología:**
• Google Maps (navegación)
• Dianping (reseñas)
• Alipay (entradas)
• Google Translate (información)

🎭 **Cultura y tradiciones:**
• Historia del Bund
• Arquitectura colonial
• Tradiciones del templo
• Arte moderno

💡 **Tip del día:** El Bund al atardecer es mágico - ¡no te lo pierdas!

🎯 **Reto extra:** Haz una lista de 8 estafas a evitar en Shanghai""",
        "https://www.youtube.com/embed/hk43UekQG4A",
        "/calendar_enhanced/7.png"
    ),
    (
        "🗣️ Idioma chino básico 📚",
        """¡Hora de aprender las frases que nos salvarán en Shanghai! 🎯

**Reto del día:** Graba un video diciendo 'Ni hao' (hola) y 'Xie xie' (gracias) en chino. ¡Comparte tu mejor pronunciación! 📹

**¿Por qué es importante?** Los locales aprecian el esfuerzo. ¡Un simple 'Ni hao' puede abrir muchas puertas! 🚪✨

**¿Qué nos espera?** Un idioma fascinante con 4 tonos diferentes. ¡Cada palabra es una aventura!

**Dato curioso:** El chino mandarín tiene más de 50,000 caracteres, pero solo necesitas 3,000 para leer un periódico.

**¿Sabías que...?** ChatGPT puede ayudarte a traducir chino en tiempo real usando la función de voz.""",
        "El respeto por la cultura local abre puertas y corazones. ¡Cada palabra en chino es un puente hacia nuevas amistades! 🗣️",
        """📋 **Checklist del día:**
• ✅ Aprende 5 frases básicas
• ✅ Graba video de pronunciación
• ✅ Practica con Google Translate
• ✅ Comparte tu progreso

🍽️ **Gastronomía del día:**
• Frases para pedir comida
• Nombres de platos básicos
• Cómo pedir la cuenta
• Expresiones de cortesía

🏛️ **Lugares del día:**
• Frases para preguntar direcciones
• Cómo pedir ayuda
• Expresiones de agradecimiento
• Frases de emergencia

📱 **Apps y tecnología:**
• Google Translate (traducción)
• ChatGPT (voz y traducción)
• Pleco (diccionario chino)
• HelloChinese (aprendizaje)

🎭 **Cultura y tradiciones:**
• Frases de cortesía
• Expresiones culturales
• Títulos de respeto
• Tradiciones del idioma

💡 **Tip del día:** La pronunciación es clave - ¡practica con Google Translate!

🎯 **Reto extra:** Usa ChatGPT en voz para traducir chino en tiempo real""",
        "https://www.youtube.com/embed/yiXNOAdXlzk",
        "/calendar_enhanced/8.png"
    ),
    (
        "🏮 Tradiciones chinas 🎊",
        """¡Descubramos las tradiciones milenarias que hacen única a China! 🌟

**Reto del día:** Busca información sobre el Año Nuevo Chino 2025 (Año del Dragón) y comparte un dato curioso. ¡Vamos a celebrar como locales! 🐉

**¿Sabías que?** El dragón es símbolo de poder y buena fortuna. ¡2025 será nuestro año! 🍀

**¿Por qué es importante?** Entender las tradiciones nos ayuda a conectar con la cultura local.

**Dato curioso:** El Año Nuevo Chino se celebra durante 15 días, no solo una noche como en Occidente.

**¿Sabías que...?** ChatGPT puede ayudarte a entender las tradiciones chinas y traducir frases tradicionales.""",
        "Los recuerdos son la única riqueza que nadie puede quitarte. ¡Cada tradición que conozcamos será un tesoro para siempre! 🏮",
        """📋 **Checklist del día:**
• ✅ Investiga Año Nuevo Chino 2025
• ✅ Comparte dato curioso
• ✅ Aprende sobre el Año del Dragón
• ✅ Descubre tradiciones locales

🍽️ **Gastronomía del día:**
• Comida tradicional del Año Nuevo
• Dumplings (jiaozi)
• Nian gao (pastel de año nuevo)
• Té ceremonial

🏛️ **Lugares del día:**
• Templos tradicionales
• Mercados de Año Nuevo
• Barrios históricos
• Centros culturales

📱 **Apps y tecnología:**
• ChatGPT (tradiciones y traducción)
• Google Translate (frases tradicionales)
• Apps de cultura china
• Calendario lunar

🎭 **Cultura y tradiciones:**
• 🐉 Año Nuevo Chino (Febrero 2025)
• 🏮 Farolillos rojos (buena suerte)
• 🥢 Uso de palillos (etiqueta)
• 🍵 Ceremonia del té
• 🎭 Ópera china
• 🧧 Sobres rojos (hongbao)

💡 **Tip del día:** El rojo es color de buena suerte - ¡llévate algo rojo!

🎯 **Reto extra:** Usa ChatGPT en voz para aprender frases tradicionales""",
        "https://www.youtube.com/embed/AHpT7aCB4pY",
        "/calendar_enhanced/9.png"
    ),
    (
        "🛍️ Compras en Shanghai 💰",
        """¡Hora de planificar nuestra estrategia de compras! 🛒

**Reto del día:** Haz una lista de 5 souvenirs que quieres comprar en Shanghai y compártela con el grupo. ¡Vamos a ser compradores inteligentes! 🎯

**¿Dónde comprar?** Mercados tradicionales, centros comerciales, tiendas de lujo... ¡Shanghai lo tiene todo! 🏪✨

**¿Por qué es importante?** Shanghai es un paraíso de compras con opciones para todos los presupuestos.

**Dato curioso:** Nanjing Road es una de las calles comerciales más largas del mundo con 5.5 km.

**¿Sabías que...?** Puedes regatear en los mercados tradicionales hasta un 50% del precio inicial.""",
        "La preparación es la mitad del éxito. ¡Cada compra planificada será un recuerdo perfecto! 🛍️",
        """📋 **Checklist del día:**
• ✅ Haz lista de 5 souvenirs
• ✅ Investiga precios
• ✅ Planifica rutas de compras
• ✅ Comparte tu lista con el grupo

🍽️ **Gastronomía del día:**
• Comida en centros comerciales
• Cafés en tiendas de lujo
• Mercados de comida
• Restaurantes con vistas

🏛️ **Lugares del día:**
• 🏪 Nanjing Road (calle comercial) - ¡LA MÁS FAMOSA!
• 🏮 Yu Garden Bazaar (souvenirs) - Tradición
• 🏬 Xintiandi (marcas internacionales) - Lujo
• 🎭 Tianzifang (arte y artesanía) - Arte
• 🛒 Super Brand Mall (centro comercial) - Moderno
• 🏮 Mercado de antigüedades - Historia

📱 **Apps y tecnología:**
• Alipay (pagos móviles)
• Dianping (reseñas de tiendas)
• Google Translate (etiquetas)
• Maps (navegación)

🎭 **Cultura y tradiciones:**
• Arte de regatear
• Etiqueta de compras
• Tradiciones comerciales
• Souvenirs culturales

💡 **Tip del día:** Regatea en los mercados tradicionales - ¡es parte de la experiencia!

🎯 **Reto extra:** Graba un video regateando en un mercado""",
        "https://www.youtube.com/embed/shanghai-shopping-guide",
        "/calendar_enhanced/10.png"
    ),
    (
        "🎨 Arte y cultura 🏛️",
        """¡Shanghai es un museo al aire libre! ¡Descubramos su rica herencia cultural! 🎭

**Reto del día:** Busca una obra de arte china famosa y compártela con una explicación de por qué te gusta. ¡Vamos a ser cultos! 📚

**¿Qué nos espera?** Museos, galerías, arte callejero, arquitectura... ¡Shanghai respira cultura! 🌟

**¿Por qué es importante?** El arte es la ventana al alma de una cultura. ¡Shanghai tiene milenios de historia artística!

**Dato curioso:** Shanghai tiene más de 100 museos y galerías. ¡Imposible visitarlos todos!

**¿Sabías que...?** El barrio de Tianzifang es famoso por su arte callejero y galerías independientes.""",
        "El respeto por la cultura local abre puertas y corazones. ¡Cada obra de arte nos cuenta una historia milenaria! 🎨",
        """📋 **Checklist del día:**
• ✅ Busca obra de arte china famosa
• ✅ Comparte con explicación
• ✅ Investiga sobre el artista
• ✅ Planifica visita a museos

🍽️ **Gastronomía del día:**
• Cafés en galerías de arte
• Restaurantes en museos
• Comida en barrios artísticos
• Té en centros culturales

🏛️ **Lugares del día:**
• 🏛️ Museo de Shanghai (arte clásico) - ¡IMPRESCINDIBLE!
• 🎭 Power Station of Art (arte moderno) - Vanguardia
• 🏮 M50 Creative Park (galerías) - Arte contemporáneo
• 🎪 Shanghai Grand Theatre - Ópera y ballet
• 🏛️ Shanghai Museum (historia) - Antigüedades
• 🎨 Tianzifang (arte callejero) - Barrio bohemio

📱 **Apps y tecnología:**
• Apps de museos
• Google Arts & Culture
• Traductores de arte
• Guías culturales

🎭 **Cultura y tradiciones:**
• Historia del arte chino
• Tradiciones artísticas
• Artistas famosos
• Movimientos culturales

💡 **Tip del día:** Muchos museos son gratuitos los viernes - ¡aprovéchalo!

🎯 **Reto extra:** Visita un barrio pobre para ver arte auténtico""",
        "https://www.youtube.com/embed/hxVfrYNVO8A",
        "/calendar_enhanced/11.png"
    ),
    (
        "🎵 Música y entretenimiento 🎪",
        "¡Shanghai nunca duerme! ¡Descubramos su vibrante escena musical y de entretenimiento! 🎶\n\n**Reto del día:** Busca una canción china famosa y compártela con el grupo. ¡Vamos a ampliar nuestro repertorio musical! 🎵\n\n**¿Qué nos espera?** Karaoke, conciertos, shows tradicionales, discotecas... ¡Shanghai es pura energía! ⚡",
        "Cada día es una página nueva en el libro de tu vida. ¡Cada canción que escuchemos será la banda sonora de nuestra aventura! 🎵",
        "🎵 **Entretenimiento en Shanghai:**\n• 🎤 Karaoke (KTV) - ¡muy popular!\n• 🎭 Ópera china tradicional\n• 🎪 Shanghai Circus World\n• 🎵 Conciertos en Mercedes-Benz Arena\n• 🕺 Discotecas en Xintiandi\n• 🎨 Shows de acrobacias\n\n💡 **Tip del día:** El karaoke es una actividad social muy importante - ¡atrévete a cantar!",
        "https://www.youtube.com/embed/shanghai-entertainment",
        "/calendar_enhanced/12.png"
    ),
    (
        "🏃‍♂️ Deportes y actividades 🧘‍♀️",
        "¡Shanghai es perfecta para mantenerse activo! ¡Descubramos sus mejores actividades deportivas! 🏃‍♀️\n\n**Reto del día:** Busca un parque o actividad deportiva en Shanghai que te gustaría probar y compártela. ¡Vamos a estar en forma para la aventura! 💪\n\n**¿Qué nos espera?** Tai Chi en el parque, ciclismo, running, yoga... ¡Shanghai es saludable! 🌱",
        "Las mejores compras son las que cuentan una historia. ¡Cada actividad deportiva será una historia de superación! 🏃‍♂️",
        "🏃‍♂️ **Actividades deportivas:**\n• 🧘‍♀️ Tai Chi en People's Park\n• 🚴‍♂️ Ciclismo por el Bund\n• 🏃‍♀️ Running en Century Park\n• 🧘‍♂️ Yoga en Xintiandi\n• 🏊‍♀️ Natación en hoteles\n• 🎾 Tenis en clubes locales\n\n💡 **Tip del día:** El Tai Chi al amanecer en People's Park es una experiencia única - ¡prueba!",
        "https://www.youtube.com/embed/shanghai-sports-activities",
        "/calendar_enhanced/13.png"
    ),
    (
        "💻 Tecnología china 🚀",
        "¡Shanghai es el Silicon Valley de Asia! ¡Descubramos las innovaciones tecnológicas más increíbles! 🤖\n\n**Reto del día:** Investiga sobre una empresa tecnológica china famosa (Alibaba, Tencent, Baidu) y comparte un dato curioso. ¡Vamos a ser tech-savvy! 💡\n\n**¿Qué nos espera?** Pagos móviles, delivery súper rápido, ciudades inteligentes... ¡Shanghai es el futuro! 🌟",
        "Moverse como un local es la mejor forma de conocer una ciudad. ¡Cada innovación tecnológica nos muestra el futuro! 💻",
        "💻 **Tecnología en Shanghai:**\n• 📱 Pagos móviles (Alipay/WeChat Pay)\n• 🚚 Delivery súper rápido (30 min)\n• 🚇 Metro inteligente\n• 🤖 Taxis autónomos\n• 🏪 Tiendas sin cajeros\n• 🚲 Bicicletas compartidas inteligentes\n\n💡 **Tip del día:** Todo se paga con el móvil - ¡incluso en mercados callejeros!",
        "https://www.youtube.com/embed/shanghai-technology-innovation",
        "/calendar_enhanced/14.png"
    ),
    (
        "🌃 Vida nocturna en Shanghai 🍸",
        """¡Shanghai nunca duerme! ¡Descubramos su vibrante vida nocturna! 🌙

**Reto del día:** Busca un bar o club famoso de Shanghai y compártelo con el grupo. ¡Vamos a planificar nuestras noches épicas! 🍻

**¿Qué nos espera?** Bares con vistas, discotecas, karaoke, shows... ¡Shanghai es pura energía nocturna! ⚡

**¿Por qué es importante?** La vida nocturna de Shanghai es legendaria. ¡Es una experiencia que no te puedes perder!

**Dato curioso:** Shanghai tiene más de 10,000 bares y clubs. ¡Imposible visitarlos todos!

**¿Sabías que...?** El Bund se ilumina de manera espectacular por la noche, creando un skyline único.""",
        "La noche es joven y Shanghai nos espera. ¡Cada copa que tomemos será un brindis por la aventura! 🌃",
        """📋 **Checklist del día:**
• ✅ Busca bar o club famoso
• ✅ Comparte con el grupo
• ✅ Planifica rutas nocturnas
• ✅ Investiga precios y horarios

🍽️ **Gastronomía del día:**
• Cócteles de autor
• Tapas en bares
• Comida nocturna
• Bebidas tradicionales

🏛️ **Lugares del día:**
• 🍸 Bar Rouge (vistas al Bund) - ¡ICÓNICO!
• 🕺 M1NT (discoteca de lujo) - Exclusivo
• 🎤 Party World KTV (karaoke) - Tradición
• 🍻 The Camel (bar expat) - Internacional
• 🌙 Bar Rouge (vistas espectaculares) - Vistas
• 🎭 Shanghai Grand Theatre (shows) - Cultura

📱 **Apps y tecnología:**
• Apps de bares y clubs
• Reservas online
• Mapas nocturnos
• Apps de transporte nocturno

🎭 **Cultura y tradiciones:**
• Etiqueta en bares
• Tradiciones nocturnas
• Costumbres locales
• Horarios típicos

💡 **Tip del día:** Los bares con vistas al Bund son caros pero valen la pena - ¡reserva con antelación!

🎯 **Reto extra:** Graba un video en un bar con vistas al Bund""",
        "https://www.youtube.com/embed/dsVDXeGNh8M",
        "/calendar_enhanced/15.png"
    ),
    (
        "🍜 Comida callejera épica 🥢",
        """¡100 horas de comida callejera china! ¡Prepárate para la aventura culinaria más intensa! 🍽️

**Reto del día:** Busca un plato de comida callejera china que nunca hayas probado y compártelo. ¡Vamos a ser aventureros culinarios! 🎯

**¿Qué nos espera?** Dim sum, baozi, jianbing, tanghulu... ¡Shanghai es el paraíso de la comida callejera! 🌟

**¿Por qué es importante?** La comida callejera es el corazón de la cultura culinaria china. ¡No te la puedes perder!

**Dato curioso:** Shanghai tiene más de 50,000 puestos de comida callejera. ¡Imposible probarlos todos!

**¿Sabías que...?** La comida callejera china es considerada una de las mejores del mundo.""",
        "La comida callejera es el alma de una ciudad. ¡Cada bocado nos acerca más a la cultura local! 🍜",
        """📋 **Checklist del día:**
• ✅ Busca plato de comida callejera nuevo
• ✅ Comparte con el grupo
• ✅ Investiga ingredientes
• ✅ Planifica rutas de comida

🍽️ **Gastronomía del día:**
• 🥟 Dim sum (dumplings al vapor)
• 🥖 Baozi (panecillos rellenos)
• 🥞 Jianbing (crepes chinos)
• 🍡 Tanghulu (frutas caramelizadas)
• 🍜 Fideos de calle
• 🥘 Hot pot callejero

🏛️ **Lugares del día:**
• Mercados de comida callejera
• Puestos tradicionales
• Calles famosas por comida
• Mercados nocturnos

📱 **Apps y tecnología:**
• Dianping (reseñas de comida)
• Meituan (delivery callejero)
• Google Translate (menús)
• Maps (ubicación de puestos)

🎭 **Cultura y tradiciones:**
• Etiqueta en comida callejera
• Tradiciones culinarias
• Ingredientes únicos
• Técnicas de cocina

💡 **Tip del día:** La comida callejera es más auténtica que los restaurantes - ¡atrévete a probar!

🎯 **Reto extra:** Graba un video probando 5 platos diferentes""",
        "https://www.youtube.com/embed/S1QzWUb4SnQ",
        "/calendar_enhanced/16.png"
    ),
    (
        "🏗️ Arquitectura moderna de Shanghai 🏙️",
        """¡Shanghai es un museo de arquitectura al aire libre! ¡Descubramos sus rascacielos más impresionantes! 🌆

**Reto del día:** Busca el rascacielos más alto de Shanghai y comparte un dato curioso sobre él. ¡Vamos a ser arquitectos por un día! 🏗️

**¿Qué nos espera?** Torres futuristas, edificios históricos, arquitectura colonial... ¡Shanghai es pura innovación! ✨

**¿Por qué es importante?** La arquitectura de Shanghai cuenta la historia de la ciudad. ¡Cada edificio tiene una historia!

**Dato curioso:** Shanghai tiene más de 1,000 rascacielos. ¡Es una de las ciudades con más rascacielos del mundo!

**¿Sabías que...?** La Torre de Shanghai es el segundo edificio más alto del mundo con 632 metros.""",
        "La arquitectura es música congelada. ¡Cada edificio de Shanghai es una sinfonía visual! 🏗️",
        """📋 **Checklist del día:**
• ✅ Busca rascacielos más alto
• ✅ Comparte dato curioso
• ✅ Planifica ruta arquitectónica
• ✅ Investiga historia de edificios

🍽️ **Gastronomía del día:**
• Restaurantes en rascacielos
• Cafés con vistas panorámicas
• Comida en edificios históricos
• Bares en azoteas

🏛️ **Lugares del día:**
• 🏗️ Torre de Shanghai (632m) - ¡EL MÁS ALTO!
• 🏢 Jin Mao Tower (420m) - Clásico
• 🏙️ Shanghai World Financial Center (492m) - Icono
• 🏛️ Bund (arquitectura colonial) - Historia
• 🏗️ Oriental Pearl Tower (468m) - Futurista
• 🏢 Shanghai Tower (632m) - Moderno

📱 **Apps y tecnología:**
• Apps de arquitectura
• Guías de edificios
• Mapas arquitectónicos
• Realidad aumentada

🎭 **Cultura y tradiciones:**
• Historia arquitectónica
• Estilos arquitectónicos
• Tradiciones de construcción
• Simbolismo cultural

💡 **Tip del día:** Las vistas desde los rascacielos son espectaculares - ¡no te las pierdas!

🎯 **Reto extra:** Graba un video desde la azotea de un rascacielos""",
        "https://www.youtube.com/embed/51Op3A-8HSA",
        "/calendar_enhanced/17.png"
    ),
    (
        "🌿 Parques y naturaleza en Shanghai 🌸",
        """¡Descubre los oasis verdes de Shanghai! ¡Incluso en la ciudad más moderna hay naturaleza! 🌳

**Reto del día:** Busca información sobre la antigua ciudad de Wuzhen y comparte por qué te gustaría visitarla. ¡Vamos a explorar la naturaleza! 🌿

**¿Qué nos espera?** Parques urbanos, jardines tradicionales, lagos, canales... ¡Shanghai tiene naturaleza oculta! ✨

**¿Por qué es importante?** La naturaleza nos conecta con la esencia de China. ¡Es una experiencia única!

**Dato curioso:** Shanghai tiene más de 200 parques y jardines. ¡Es una de las ciudades más verdes de China!

**¿Sabías que...?** Wuzhen es una ciudad acuática de 1,300 años considerada la Venecia de China.""",
        "La naturaleza es el mejor antídoto contra el estrés urbano. ¡Cada parque es un refugio de paz! 🌿",
        """📋 **Checklist del día:**
• ✅ Investiga sobre Wuzhen
• ✅ Comparte por qué te gustaría visitarla
• ✅ Planifica rutas de naturaleza
• ✅ Descubre parques locales

🍽️ **Gastronomía del día:**
• Comida en parques
• Picnics tradicionales
• Té en jardines
• Comida local en Wuzhen

🏛️ **Lugares del día:**
• 🌿 Yu Garden (jardín clásico) - ¡IMPRESCINDIBLE!
• 🌸 Century Park (parque moderno) - Grande
• 🌳 Zhongshan Park (parque histórico) - Tradición
• 🏮 Wuzhen (ciudad acuática) - ¡MÁGICA!
• 🌊 Huangpu Park (junto al río) - Vistas
• 🌺 Fuxing Park (parque francés) - Estilo europeo

📱 **Apps y tecnología:**
• Apps de parques
• Guías de naturaleza
• Mapas de senderos
• Apps de turismo

🎭 **Cultura y tradiciones:**
• Jardines tradicionales chinos
• Filosofía del Feng Shui
• Tradiciones de la naturaleza
• Simbolismo de plantas

💡 **Tip del día:** Los jardines chinos están diseñados para la meditación - ¡disfruta la paz!

🎯 **Reto extra:** Graba un video en un jardín tradicional chino""",
        "https://www.youtube.com/embed/SkWSR6EgS3I",
        "/calendar_enhanced/18.png"
    ),
    (
        "Frase del día 🌟",
        "Los recuerdos son el único tesoro que puedes llevarte contigo. ¡Shanghai nos dará tesoros infinitos! 💎",
        "Los recuerdos son el único tesoro que aumenta con el tiempo.",
        "• Documenta todo\n• Vive intensamente\n• ¡Crea recuerdos únicos!",
        "",
        "/19.png"
    ),
    (
        "Últimos preparativos 🎒",
        "¡Solo quedan 5 días! ¡Revisa que tengas todo: cargadores, medicinas, ¡y muchas ganas! ⚡",
        "Los últimos detalles son los que marcan la diferencia.",
        "• Lista final de maletas\n• Cargadores y adaptadores\n• Medicinas básicas\n• ¡Actitud aventurera!",
        "",
        "/20.png"
    ),
    (
        "Frase motivacional final 💪",
        "La aventura comienza cuando sales de tu zona de confort. ¡Shanghai nos espera! 🌍",
        "La magia sucede fuera de tu zona de confort.",
        "• Abraza lo desconocido\n• Sé valiente\n• ¡Vive la aventura!",
        "",
        "/21.png"
    ),
    (
        "¡Casi llegamos! 🎉",
        "¡Solo quedan 3 días! ¡La emoción está por las nubes! ¡Shanghai está a la vuelta de la esquina! 🏮",
        "La emoción es el mejor equipaje para cualquier viaje.",
        "• ¡Mantén la emoción!\n• Comparte con el grupo\n• ¡Prepara la cuenta atrás final!",
        "",
        "/22.png"
    ),
    (
        "🎄 Nochebuena en Shanghai 🎊",
        """¡Vamos a celebrar la Nochebuena más épica en Shanghai! ¡Será una Navidad inolvidable! 🎆

**Reto del día:** Planifica cómo vas a celebrar la Nochebuena en Shanghai y compártelo con el grupo. ¡Vamos a crear recuerdos únicos! 🎯

**¿Qué nos espera?** Fuegos artificiales en el Bund, cena especial, brindis con vista al skyline... ¡Shanghai en Navidad es mágico! ✨

**¿Por qué es importante?** Celebrar Navidad en Shanghai será una experiencia única que recordarás toda la vida.

**Dato curioso:** Shanghai se ilumina de manera espectacular en Navidad. ¡Es una de las ciudades más bonitas del mundo!

**¿Sabías que...?** El Bund se convierte en un espectáculo de luces durante las fiestas navideñas.""",
        "Celebrar en un lugar nuevo es crear recuerdos únicos. ¡Esta Navidad será la más especial! 🎄",
        """📋 **Checklist del día:**
• ✅ Planifica celebración de Nochebuena
• ✅ Comparte con el grupo
• ✅ Reserva restaurante especial
• ✅ Prepara brindis épico

🍽️ **Gastronomía del día:**
• Cena especial de Navidad
• Comida tradicional china
• Bebidas navideñas
• Postres especiales

🏛️ **Lugares del día:**
• 🎆 Bund (fuegos artificiales) - ¡ESPECTACULAR!
• 🍽️ Restaurantes con vistas
• 🎪 Centros comerciales navideños
• 🏮 Barrios iluminados

📱 **Apps y tecnología:**
• Apps de eventos navideños
• Reservas de restaurantes
• Mapas de luces navideñas
• Apps de transporte festivo

🎭 **Cultura y tradiciones:**
• Tradiciones navideñas chinas
• Celebraciones locales
• Costumbres festivas
• Simbolismo navideño

💡 **Tip del día:** Reserva con antelación - ¡Shanghai en Navidad es muy popular!

🎯 **Reto extra:** Graba un video del brindis de Nochebuena con vista al Bund""",
        "https://www.youtube.com/embed/b1LkyFaXHtI",
        "/calendar_enhanced/24.png"
    ),
    (
        "¡DÍA DEL VUELO! ✈️",
        "¡HOY ES EL DÍA! ¡Nos vamos a Shanghai! ¡Que empiece la aventura más épica del año! 🎊🇨🇳",
        "Hoy comienza la aventura que recordarás toda la vida.",
        "• ¡Llegar temprano al aeropuerto!\n• Documentos a mano\n• ¡Actitud aventurera!\n• ¡Disfruta cada momento!",
        "https://www.youtube.com/embed/9bZkp7q19f0",
        "/24.png"
    ),
    (
        "🏮 ¡Llegamos a Shanghai! ✨",
        """¡FELIZ NAVIDAD EN SHANGHAI! ¡Hemos llegado a la ciudad de los sueños! ¡Que empiece la magia! 🎄

**¡MISIÓN CUMPLIDA!** Hemos llegado a Shanghai después de 25 días de preparación. ¡La aventura más épica comienza ahora! 🚀

**¿Qué nos espera?** Una ciudad llena de sorpresas, cultura milenaria, tecnología futurista... ¡Shanghai nos espera! 🌟

**¿Por qué es especial?** Este es el momento que hemos estado esperando durante 25 días. ¡Cada preparación ha valido la pena!

**Dato curioso:** Shanghai recibe más de 30 millones de turistas al año. ¡Somos parte de esa estadística!

**¿Sabías que...?** Hay cosas que no sabías antes de viajar que te habrían ayudado mucho.""",
        "¡Hemos llegado! Ahora comienza la verdadera aventura. ¡Que empiece la magia de Shanghai! 🏮",
        """📋 **Checklist del día:**
• ✅ ¡Bienvenidos a Shanghai!
• ✅ Primera foto en el aeropuerto
• ✅ Activar Alipay y apps
• ✅ ¡Explora la ciudad!

🍽️ **Gastronomía del día:**
• Primera comida en Shanghai
• Xiaolongbao auténtico
• Té chino tradicional
• Comida callejera

🏛️ **Lugares del día:**
• 🏮 Aeropuerto de Shanghai - ¡PRIMER CONTACTO!
• 🌃 Bund - Vistas espectaculares
• 🏙️ Torre de Shanghai - Skyline
• 🏮 Yu Garden - Tradición
• 🚇 Metro de Shanghai - Movilidad
• 🍜 Mercados de comida - Autenticidad

📱 **Apps y tecnología:**
• Alipay (pagos)
• WeChat (comunicación)
• Maps (navegación)
• Google Translate (idioma)

🎭 **Cultura y tradiciones:**
• Primera impresión de China
• Cultura local
• Tradiciones milenarias
• Costumbres chinas

💡 **Tip del día:** Disfruta cada momento - ¡Shanghai te sorprenderá!

🎯 **Reto extra:** Graba un video de tu primera impresión de Shanghai""",
        "https://www.youtube.com/embed/WJd-BopESW0",
        "/calendar_enhanced/25.png"
    )
]

_current_day = len(_shanghai_days) - 1


def _is_day_available(day_number: int) -> bool:
    """
    Determina si un día está disponible para ver.
    Solo se pueden ver días que ya han pasado + el día actual.
    Día 1 = 1 de diciembre, Día 25 = 25 de diciembre
    """
    today = datetime.date.today()
    current_year = today.year
    
    # Para testing: desbloquear todos los días (cambiar a False para producción)
    TESTING_MODE = True
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
            size=rx.breakpoints(
                initial="6",
                xs="7", 
                sm="8",
                md="9",
                lg="9",
                xl="9"
            ),
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
            columns=rx.breakpoints(
                initial="2",
                xs="3", 
                sm="4",
                md="5",
                lg="5",
                xl="5"
            ),
            spacing="3",
            width="100%",
            padding_y=Size.BIG.value,
            class_name="calendar-container"
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
