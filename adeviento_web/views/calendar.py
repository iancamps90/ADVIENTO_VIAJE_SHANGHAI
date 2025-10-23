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
        "🏮 ¡EMPIEZA LA CUENTA ATRÁS! 🐉",
        """¡Hola aventureros! Hoy comienza la cuenta atrás para nuestro viaje a Shanghai. ¡25 días de sorpresas, preparación y emoción!

🎯 **RETO DEL DÍA:**
¡FOTO CHALLENGE! Cambia tu foto de perfil por algo relacionado con Shanghai (dragón, farolillo, skyline...) y compártela aquí. ¡El más creativo gana puntos extra! 🏆

🧳 **Preparativos de maleta:**
• 📄 **Documentos:** Revisa tu pasaporte (debe tener 6+ meses de validez)
• 📱 **Apps esenciales:** Descarga Google Translate, Maps, Alipay
• 🎒 **Organización:** Empieza a hacer lista de maletas
• 🎯 **Motivación:** Cambia fondo de pantalla y comparte en el grupo

💡 **Tip del día:** Shanghai significa 'Sobre el mar' - ¡perfecto para nuestra aventura!

🏮 **Progreso del viaje:** 1/25 - ¡Solo empezamos!

🎥 **Video del día:** Graba un video presentándote como "aventurero rumbo a Shanghai" con tu mejor pose épica.

🧧 **Extra para el grupo:** 📸 Sube tu foto a Instagram con #CuentaAtrasShanghai y etiqueta al grupo.""",
        "La aventura comienza con un solo paso. ¡Y ese paso es hoy!",
        """💡 **Dato curioso:** Shanghai es la ciudad más poblada del mundo con 24 millones de habitantes.

🎯 **Actividades del día:**
• Cambia tu foto de perfil por algo de Shanghai
• Revisa documentos importantes
• Descarga apps esenciales
• ¡Comparte tu emoción con el grupo!""",
        "https://www.youtube.com/embed/YgL2XPZBMys",
        "/calendar_enhanced/1.png"
    ),
    (
        "💳 ¡APPS ESENCIALES PARA SHANGHAI! 📱",
        """¡Momento de ser responsables! Hoy toca preparar nuestro arsenal digital para conquistar Shanghai. 💪

🎯 **RETO DEL DÍA:**
¡MISIÓN DIGITAL ÉPICA! Descarga Alipay y activa el Tour Pass. ¡Comparte pantallazo + un selfie celebrando que ya eres "digitalmente chino"! ¡Bonus si lo haces con cara de espía! 📱🇨🇳🕵️

🧳 **Preparativos de maleta:**
• 📱 **Apps esenciales:** Descarga Alipay, WeChat, Google Translate
• 💳 **Configuración:** Activa Tour Pass en Alipay
• 🔌 **Electrónica:** Revisa cargadores universales y adaptadores para China
• 🗺️ **Navegación:** Descarga Maps y Baidu Maps

💡 **Tip del día:** En China se paga TODO con el móvil. ¡Sin Alipay no hay paraíso!

🎥 **Video del día:** Graba un video configurando Alipay con música épica y texto: "Día 2 – Convirtiéndome en digital chino 📱🇨🇳"

🧧 **Extra para el grupo:** 📸 Sube tu selfie "digitalmente chino" al grupo de WhatsApp con el texto: "¡Ya soy digital chino! 📱🇨🇳 #Día2Shanghai".""",
        "La preparación es la clave del éxito. ¡Cada app descargada es un paso más cerca! 🔑",
        """📱 **Apps imprescindibles:**
• Alipay (pagos y transporte) - ¡LA MÁS IMPORTANTE!
• WeChat (comunicación local) - WhatsApp chino
• Google Translate (idioma) - Para traducir menús
• Maps (navegación) - Aunque Baidu Maps es mejor
• Didi (taxis) - Uber chino
• Dianping (restaurantes) - Yelp chino
• Meituan (delivery) - Para pedir comida

💡 **Dato curioso:** China tiene 1.4 mil millones de usuarios de pagos móviles. ¡Somos una gota en el océano!""",
        "https://www.youtube.com/embed/KNMz8WqRS-w",
        "/calendar_enhanced/2.png"
    ),
    (
        "🏮 ¡CURIOSIDADES DE SHANGHAI! 🏙️",
        """¡Descubramos juntos los secretos de la ciudad más fascinante de China! 🌟

🎯 **RETO DEL DÍA:**
¡BÚSQUEDA DEL TESORO ÉPICA! Encuentra la foto más alucinante de Shanghai que puedas y compártela con tu frase motivacional personal. ¡Que nos emocione a todos! ¡El más épico gana! 🔍✨🏆

🧳 **Preparativos de maleta:**
• 🏥 **Botiquín:** Ibuprofeno, Fortasec, tiritas, paracetamol, algo para mareo
• 🧴 **Higiene:** Gel hidroalcohólico y toallitas húmedas
• 📱 **Apps:** Descarga Google Translate (ya configurado en día 2)
• 🗺️ **Investigación:** Investiga sobre el Bund y la Torre de Shanghai

💡 **Tip del día:** Descarga Google Translate y prueba su función de cámara instantánea para traducir carteles o menús. 🈶 Te salvará en los restaurantes locales.

🎥 **Video del día:** Graba tu reacción al ver fotos de Shanghai. Ponle música tipo "China Chill" y texto: "Día 3 – Descubriendo Shanghai 🏮🇨🇳"

🧧 **Extra para el grupo:** 📸 Sube tu foto más épica de Shanghai al grupo de WhatsApp con el texto: "¡Esta será nuestra aventura! 🏮🇨🇳 #Día3Shanghai".""",
        "Un viaje se empieza con los ojos… pero se recuerda con el paladar. ✈️🍜",
        """🏙️ **Curiosidades de Shanghai:**
• Shanghai significa literalmente "Sobre el mar" 🌊
• Tiene el skyline más iluminado del mundo (más de 50 rascacielos con luces LED)
• En cada esquina puedes encontrar un puesto de dumplings frescos 🥟
• Comer con ruido (¡slurp!) es señal de disfrute, no de mala educación 😄

🧠 **Dato curioso:** Los palillos no deben clavarse en el arroz. Se asocia a ofrendas funerarias. 👉 Siempre apóyalos sobre el cuenco o en un soporte.

💡 **Tip del día:** El metro de Shanghai tiene 831 km de vías - ¡más que cualquier otra ciudad!""",
        "https://www.youtube.com/embed/L_jWHffIx5E",
        "/calendar_enhanced/3.png"
    ),
    (
        "📄 ¡DOCUMENTOS Y SEGUROS! ✈️",
        """¡Momento de ser súper organizados! Hoy toca revisar que tenemos todos los papeles en regla para nuestra gran aventura. 📋

🎯 **RETO DEL DÍA:**
¡CHECKPOINT DOCUMENTOS ÉPICO! Haz una foto de tu pasaporte (solo portada) + tu cara de "¡estoy listo para la aventura!" ¡Demuestra que eres un viajero responsable! ¡Bonus si haces pose de superhéroe! ✈️📄🦸

🧳 **Preparativos de maleta:**
• 📄 **Pasaporte:** Verifica que tenga 6+ meses de validez
• 🏥 **Seguro de viaje:** Contrata uno que cubra China
• 📱 **Documentos digitales:** Crea carpeta en la nube con copias
• 🎫 **Billetes:** Guarda confirmaciones y códigos QR

💡 **Tip del día:** China requiere pasaporte con 6+ meses de validez. ¡Muchos países no lo saben!

🎥 **Video del día:** Graba un video revisando tus documentos con música épica y texto: "Día 4 – Viajero responsable ✈️📄"

🧧 **Extra para el grupo:** 📸 Sube tu foto de superhéroe con pasaporte al grupo de WhatsApp con el texto: "¡Documentos listos para conquistar Shanghai! 📄✈️ #Día4Shanghai".""",
        "La preparación es la clave del éxito en cualquier aventura. ¡Cada documento revisado es tranquilidad ganada!",
        """📄 **Documentos esenciales:**
• Pasaporte con 6+ meses de validez
• Seguro de viaje que cubra China
• Copias digitales en la nube
• Confirmaciones de vuelo y hotel

💡 **Dato curioso:** El seguro de viaje puede ahorrarte miles de euros en caso de emergencia médica en el extranjero.

🛡️ **Consejo de experto:** Guarda una copia de tu pasaporte en tu email y en la nube. ¡Nunca se sabe cuándo la necesitarás!""",
        "https://www.youtube.com/embed/H3HrJgYtjjY",
        "/calendar_enhanced/4.png"
    ),
    (
        "🍜 ¡COMIDA CHINA AUTÉNTICA! 🥢",
        """¡Hora de preparar el estómago para la aventura culinaria más épica! 🍽️

🎯 **RETO DEL DÍA:**
¡AVENTURA CULINARIA ÉPICA! Ve a un restaurante chino y pide algo que NUNCA hayas probado. ¡Comparte foto del plato + tu cara de sorpresa! ¿Serás valiente? ¡El más atrevido gana! 🥢😱🏆

🧳 **Preparativos de maleta:**
• 🍜 **Investigación:** Busca restaurante chino local
• 📱 **Apps:** Descarga Dianping (Yelp chino) para reseñas
• 🥢 **Técnica:** Aprende a usar palillos correctamente
• 📝 **Lista:** Haz lista de platos que quieres probar en Shanghai

💡 **Tip del día:** El xiaolongbao se inventó en Shanghai en 1875 y se come con una técnica especial para no quemarse.

🎥 **Video del día:** Graba un video probando comida china con música épica y texto: "Día 5 – Aventura culinaria 🍜🥢"

🧧 **Extra para el grupo:** 📸 Sube tu foto del plato más atrevido al grupo de WhatsApp con el texto: "¡Me atrevo con todo! 🥢😱 #Día5Shanghai".""",
        "La comida es el lenguaje universal que conecta culturas. ¡Cada bocado nos acerca más a Shanghai!",
        """🍜 **Platos icónicos de Shanghai:**
• Xiaolongbao (sopa de dumplings) - ¡el rey de Shanghai!
• Shengjianbao (pan frito con carne)
• Hongshao rou (cerdo en salsa de soja)
• Baiqie ji (pollo blanco cortado)

💡 **Dato curioso:** Shanghai tiene más de 50,000 restaurantes. ¡Imposible probarlos todos en una vida!

🥢 **Consejo de experto:** En China, hacer ruido al comer (slurp) es señal de que disfrutas la comida. ¡No tengas vergüenza!""",
        "https://www.youtube.com/embed/f1yIX7EMhQE",
        "/calendar_enhanced/5.png"
    ),
    (
        "🚇 ¡TRANSPORTE EN SHANGHAI! 🚌",
        """¡Hora de dominar el sistema de transporte más eficiente del mundo! 🚇

🎯 **RETO DEL DÍA:**
¡PLANIFICADOR DE RUTAS ÉPICO! Descarga la app del metro de Shanghai y diseña tu ruta perfecta para el primer día. ¡Comparte tu itinerario épico! ¡El más creativo gana! 🚇🗺️🏆

🧳 **Preparativos de maleta:**
• 📱 **Apps:** Descarga Shanghai Metro y Baidu Maps
• 🗺️ **Rutas:** Planifica tu itinerario del primer día
• 💳 **Pagos:** Configura Alipay para pagar el metro
• 📝 **Lista:** Haz lista de estaciones que quieres visitar

💡 **Tip del día:** Puedes pagar el metro con Alipay escaneando códigos QR. ¡Súper fácil!

🎥 **Video del día:** Graba un video planificando tu ruta con música épica y texto: "Día 6 – Planificador de rutas 🚇🗺️"

🧧 **Extra para el grupo:** 📸 Sube tu itinerario más creativo al grupo de WhatsApp con el texto: "¡Mi ruta épica por Shanghai! 🚇🗺️ #Día6Shanghai".""",
        "La emoción es el combustible de los grandes viajes. ¡Cada línea de metro nos lleva a una nueva aventura!",
        """🚇 **Sistema de transporte de Shanghai:**
• Metro: 831 km de vías (el más largo del mundo)
• Autobuses: Red extensa y económica
• Taxis: Didi (Uber chino) muy popular
• Bicicletas: Mobike y Ofo por toda la ciudad

💡 **Dato curioso:** El metro de Shanghai transporta 10+ millones de personas al día. ¡Vamos a ser parte de esa estadística!

🚌 **Consejo de experto:** En hora punta (7-9am, 5-7pm) el metro está súper lleno. ¡Mejor evitar esas horas!""",
        "https://www.youtube.com/embed/XVvhsfVz-WE",
        "/calendar_enhanced/6.png"
    ),
    (
        "🏛️ ¡LUGARES IMPRESCINDIBLES! 🎯",
        """¡Hora de crear nuestra lista de deseos de Shanghai! 🗺️

🎯 **RETO DEL DÍA:**
¡LISTA DE DESEOS ÉPICA! Elige tu TOP 3 lugares que NO te puedes perder en Shanghai. ¡Comparte tu lista + por qué cada lugar te emociona! ¡El más emocionante gana! 🏛️❤️🏆

🧳 **Preparativos de maleta:**
• 🗺️ **Investigación:** Busca información sobre lugares icónicos
• 📱 **Apps:** Descarga apps de turismo y mapas
• 💰 **Presupuesto:** Investiga precios y horarios de entrada
• 📝 **Lista:** Haz tu TOP 3 lugares imprescindibles

💡 **Tip del día:** El Bund tiene 52 edificios de diferentes estilos arquitectónicos. ¡Un museo al aire libre!

🎥 **Video del día:** Graba un video presentando tus 3 lugares favoritos con música épica y texto: "Día 7 – Lista de deseos 🏛️❤️"

🧧 **Extra para el grupo:** 📸 Sube tu TOP 3 lugares al grupo de WhatsApp con el texto: "¡Estos son mis imprescindibles! 🏛️❤️ #Día7Shanghai".""",
        "La comida es el lenguaje universal que conecta culturas. ¡Cada lugar que visitemos será una historia que contar!",
        """🏛️ **Lugares icónicos de Shanghai:**
• El Bund - Paseo marítimo con arquitectura histórica
• Torre de Shanghai - Segundo edificio más alto del mundo (632m)
• Templo del Buda de Jade - Templo budista más famoso
• Yu Garden - Jardín clásico chino del siglo XVI

💡 **Dato curioso:** La Torre de Shanghai es el segundo edificio más alto del mundo con 632 metros.

🎯 **Consejo de experto:** Visita el Bund al atardecer para ver el skyline iluminado. ¡Es espectacular!""",
        "https://www.youtube.com/embed/hk43UekQG4A",
        "/calendar_enhanced/7.png"
    ),
    (
        "🗣️ ¡IDIOMA CHINO BÁSICO! 📚",
        """¡Hora de aprender las frases que nos salvarán en Shanghai! 🎯

🎯 **RETO DEL DÍA:**
¡DESAFÍO CHINO ÉPICO! Graba un video diciendo 'Ni hao' (hola) y 'Xie xie' (gracias) en chino con tu mejor acento. ¡Luego grita '¡YA HABLO CHINO!' ¡El más chino gana! 🗣️🎬🏆

🧳 **Preparativos de maleta:**
• 📱 Descarga Google Translate y ChatGPT
• 🎧 Prueba la función de voz para traducción
• 📝 Haz una lista de 10 frases básicas
• 🎯 Practica la pronunciación con apps

💡 **Tip del día:** Los locales aprecian el esfuerzo. ¡Un simple 'Ni hao' puede abrir muchas puertas!

🎥 **Video del día:** Graba un video practicando chino con música épica y texto: "Día 8 – Aprendiendo chino 🗣️📚"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "El respeto por la cultura local abre puertas y corazones. ¡Cada palabra en chino es un puente hacia nuevas amistades! 🗣️",
        """💡 **Dato curioso:** El chino mandarín tiene más de 50,000 caracteres, pero solo necesitas 3,000 para leer un periódico.

🎯 **Actividades del día:**
• Aprende 5 frases básicas en chino
• Graba video de pronunciación
• Practica con Google Translate
• ¡Comparte tu progreso con el grupo!

🗣️ **Frases esenciales:**
• Ni hao (hola)
• Xie xie (gracias)
• Zai jian (adiós)
• Duo shao qian? (¿cuánto cuesta?)
• Wo bu dong (no entiendo)""",
        "https://www.youtube.com/embed/yiXNOAdXlzk",
        "/calendar_enhanced/8.png"
    ),
    (
        "🏮 ¡TRADICIONES CHINAS! 🎊",
        """¡Descubramos las tradiciones milenarias que hacen única a China! 🌟

🎯 **RETO DEL DÍA:**
¡BÚSQUEDA DEL TESORO TRADICIONAL! Busca información sobre el Año Nuevo Chino 2025 (Año del Dragón) y comparte un dato curioso. ¡Vamos a celebrar como locales! 🐉✨🏆

🧳 **Preparativos de maleta:**
• 📱 Descarga apps de cultura china
• 🎨 Busca algo rojo para llevar (color de buena suerte)
• 📚 Investiga sobre el Año del Dragón
• 🎯 Prepara frases tradicionales

💡 **Tip del día:** El dragón es símbolo de poder y buena fortuna. ¡2025 será nuestro año!

🎥 **Video del día:** Graba un video explicando una tradición china con música épica y texto: "Día 9 – Tradiciones chinas 🏮🎊"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "Los recuerdos son la única riqueza que nadie puede quitarte. ¡Cada tradición que conozcamos será un tesoro para siempre! 🏮",
        """💡 **Dato curioso:** El Año Nuevo Chino se celebra durante 15 días, no solo una noche como en Occidente.

🎯 **Actividades del día:**
• Investiga Año Nuevo Chino 2025
• Comparte dato curioso con el grupo
• Aprende sobre el Año del Dragón
• ¡Descubre tradiciones locales!

🏮 **Tradiciones del Año del Dragón:**
• 🐉 Dragón (poder y buena fortuna)
• 🏮 Farolillos rojos (buena suerte)
• 🥢 Uso de palillos (etiqueta)
• 🍵 Ceremonia del té
• 🧧 Sobres rojos (hongbao)
• 🎭 Ópera china""",
        "https://www.youtube.com/embed/AHpT7aCB4pY",
        "/calendar_enhanced/9.png"
    ),
    (
        "🛍️ ¡COMPRAS EN SHANGHAI! 💰",
        """¡Hora de planificar nuestra estrategia de compras! 🛒

🎯 **RETO DEL DÍA:**
¡LISTA DE COMPRAS ÉPICA! Haz una lista de 5 souvenirs que quieres comprar en Shanghai y compártela con el grupo. ¡Luego haz un video mostrando tu lista y grita '¡SHANGHAI, AQUÍ VENGO A COMPRAR!' ¡El más comprador gana! 🛍️🎬🏆

🧳 **Preparativos de maleta:**
• 💳 Revisa límites de tarjetas
• 📱 Configura Alipay para pagos
• 🎒 Prepara bolsas para compras
• 🎯 Investiga precios de souvenirs

💡 **Tip del día:** Nanjing Road es una de las calles comerciales más largas del mundo con 5.5 km.

🎥 **Video del día:** Graba un video mostrando tu lista de compras con música épica y texto: "Día 10 – Lista de compras 🛍️💰"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La preparación es la mitad del éxito. ¡Cada compra planificada será un recuerdo perfecto! 🛍️",
        """💡 **Dato curioso:** Puedes regatear en los mercados tradicionales hasta un 50% del precio inicial.

🎯 **Actividades del día:**
• Haz lista de 5 souvenirs
• Investiga precios
• Planifica rutas de compras
• ¡Comparte tu lista con el grupo!

🛍️ **Lugares de compras:**
• 🏪 Nanjing Road (calle comercial) - ¡LA MÁS FAMOSA!
• 🏮 Yu Garden Bazaar (souvenirs) - Tradición
• 🏬 Xintiandi (marcas internacionales) - Lujo
• 🎭 Tianzifang (arte y artesanía) - Arte
• 🛒 Super Brand Mall (centro comercial) - Moderno""",
        "https://www.youtube.com/embed/shanghai-shopping-guide",
        "/calendar_enhanced/10.png"
    ),
    (
        "🎨 ¡ARTE Y CULTURA! 🏛️",
        """¡Shanghai es un museo al aire libre! ¡Descubramos su rica herencia cultural! 🎭

🎯 **RETO DEL DÍA:**
¡BÚSQUEDA ARTÍSTICA ÉPICA! Busca una obra de arte china famosa y compártela con una explicación de por qué te gusta. ¡Vamos a ser cultos! 📚✨🏆

🧳 **Preparativos de maleta:**
• 📱 Descarga apps de museos
• 🎨 Prepara cámara para fotos
• 📚 Investiga sobre arte chino
• 🎯 Planifica rutas culturales

💡 **Tip del día:** Shanghai tiene más de 100 museos y galerías. ¡Imposible visitarlos todos!

🎥 **Video del día:** Graba un video explicando una obra de arte china con música épica y texto: "Día 11 – Arte y cultura 🎨🏛️"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "El respeto por la cultura local abre puertas y corazones. ¡Cada obra de arte nos cuenta una historia milenaria! 🎨",
        """🎨 **Museos y galerías de Shanghai:**
• 🏛️ Museo de Shanghai (arte clásico) - ¡IMPRESCINDIBLE!
• 🎭 Power Station of Art (arte moderno) - Vanguardia
• 🏮 M50 Creative Park (galerías) - Arte contemporáneo
• 🎪 Shanghai Grand Theatre - Ópera y ballet
• 🏛️ Shanghai Museum (historia) - Antigüedades
• 🎨 Tianzifang (arte callejero) - Barrio bohemio

💡 **Dato curioso:** Shanghai tiene más de 100 museos y galerías. ¡Imposible visitarlos todos!

🎭 **Consejo de experto:** Visita los museos por la mañana para evitar multitudes y tener mejor experiencia.""",
        "https://www.youtube.com/embed/hxVfrYNVO8A",
        "/calendar_enhanced/11.png"
    ),
    (
        "🎵 ¡MÚSICA Y ENTRETENIMIENTO! 🎪",
        """¡Shanghai nunca duerme! ¡Prepárate para su vibrante escena musical y de entretenimiento! 🎶

🎯 **RETO DEL DÍA:**
¡DESAFÍO MUSICAL ÉPICO! Busca una canción china famosa y compártela con el grupo. ¡Luego graba un video cantándola (aunque no sepas chino) con tu mejor voz! ¡El más valiente gana! 🎵🎬🏆

🧳 **Preparativos de maleta:**
• 🎤 Prepara tu repertorio de karaoke
• 📱 Descarga apps de música china
• 🎧 Prepara auriculares para practicar
• 🎯 Investiga sobre música tradicional

💡 **Tip del día:** El karaoke es una actividad social muy importante - ¡atrévete a cantar!

🎥 **Video del día:** Graba un video cantando una canción china con música épica y texto: "Día 12 – Música y entretenimiento 🎵🎪"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "Cada día es una página nueva en el libro de tu vida. ¡Cada canción que escuchemos será la banda sonora de nuestra aventura! 🎵",
        "🎵 **Entretenimiento en Shanghai:**\n• 🎤 Karaoke (KTV) - ¡muy popular!\n• 🎭 Ópera china tradicional\n• 🎪 Shanghai Circus World\n• 🎵 Conciertos en Mercedes-Benz Arena\n• 🕺 Discotecas en Xintiandi\n• 🎨 Shows de acrobacias\n\n💡 **Tip del día:** El karaoke es una actividad social muy importante - ¡atrévete a cantar!",
        "https://www.youtube.com/embed/shanghai-entertainment",
        "/calendar_enhanced/12.png"
    ),
    (
        "🍜 ¡COMIDA CHINA! 🥢",
        """¡Prepárate para la aventura culinaria más intensa de Shanghai! 🍽️

🎯 **RETO DEL DÍA:**
¡DESAFÍO COMIDA CHINA ÉPICO! Ve a un restaurante chino y pide algo que nunca hayas probado. ¡Haz un video comiéndolo y grita '¡EN SHANGHAI SERÉ COMILÓN!' ¡El más aventurero gana! 🍜🎬🏆

🧳 **Preparativos de maleta:**
• 🍽️ Prepara estómago aventurero
• 📱 Descarga apps de comida china
• 🥢 Practica con palillos en casa
• 🎯 Investiga platos que probar en Shanghai

💡 **Tip del día:** Shanghai tiene más de 50,000 puestos de comida callejera. ¡Imposible probarlos todos!

🎥 **Video del día:** Graba un video probando comida china con música épica y texto: "Día 12 – Comida china 🍜🥢"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La comida callejera es el alma de una ciudad. ¡Cada bocado nos acerca más a la cultura local! 🍜",
        "🍜 **Comida callejera en Shanghai:**\n• 🥟 Dim sum (dumplings al vapor)\n• 🥖 Baozi (panecillos rellenos)\n• 🥞 Jianbing (crepes chinos)\n• 🍡 Tanghulu (frutas caramelizadas)\n• 🍜 Fideos de calle\n• 🥘 Hot pot callejero\n\n💡 **Tip del día:** La comida callejera es más auténtica que los restaurantes - ¡atrévete a probar!",
        "https://www.youtube.com/embed/shanghai-street-food",
        "/calendar_enhanced/13.png"
    ),
    (
        "💻 ¡TECNOLOGÍA CHINA! 🚀",
        """¡Shanghai es el Silicon Valley de Asia! ¡Prepárate para las innovaciones tecnológicas más increíbles! 🤖

🎯 **RETO DEL DÍA:**
¡DESAFÍO TECH ÉPICO! Investiga sobre una empresa tecnológica china famosa (Alibaba, Tencent, Baidu) y comparte un dato curioso. ¡Luego graba un video explicando por qué es genial! ¡El más tech-savvy gana! 💡🎬🏆

🧳 **Preparativos de maleta:**
• 📱 Configura todas las apps chinas
• 💳 Prueba pagos móviles
• 🚚 Investiga sobre delivery
• 🎯 Prepara para la ciudad inteligente

💡 **Tip del día:** Todo se paga con el móvil - ¡incluso en mercados callejeros!

🎥 **Video del día:** Graba un video explicando tecnología china con música épica y texto: "Día 14 – Tecnología china 💻🚀"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "Moverse como un local es la mejor forma de conocer una ciudad. ¡Cada innovación tecnológica nos muestra el futuro! 💻",
        "💻 **Tecnología en Shanghai:**\n• 📱 Pagos móviles (Alipay/WeChat Pay)\n• 🚚 Delivery súper rápido (30 min)\n• 🚇 Metro inteligente\n• 🤖 Taxis autónomos\n• 🏪 Tiendas sin cajeros\n• 🚲 Bicicletas compartidas inteligentes\n\n💡 **Tip del día:** Todo se paga con el móvil - ¡incluso en mercados callejeros!",
        "https://www.youtube.com/embed/shanghai-technology-innovation",
        "/calendar_enhanced/14.png"
    ),
    (
        "🌃 ¡VIDA NOCTURNA EN SHANGHAI! 🍸",
        """¡Shanghai nunca duerme! ¡Prepárate para su vibrante vida nocturna! 🌙

🎯 **RETO DEL DÍA:**
¡DESAFÍO NOCTURNO ÉPICO! Busca un bar o club famoso de Shanghai y compártelo con el grupo. ¡Luego graba un video imitando un cóctel que te gustaría pedir! ¡El más creativo gana! 🍻🎬🏆

🧳 **Preparativos de maleta:**
• 👔 Prepara ropa para salir de noche
• 🍸 Investiga cócteles famosos
• 📱 Descarga apps de bares
• 🎯 Planifica rutas nocturnas

💡 **Tip del día:** Shanghai tiene más de 10,000 bares y clubs. ¡Imposible visitarlos todos!

🎥 **Video del día:** Graba un video preparando un cóctel con música épica y texto: "Día 15 – Vida nocturna 🌃🍸"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La noche es joven y Shanghai nos espera. ¡Cada copa que tomemos será un brindis por la aventura! 🌃",
        """🌃 **Vida nocturna en Shanghai:**
• 🍸 Bar Rouge (vistas al Bund) - ¡ICÓNICO!
• 🕺 M1NT (discoteca de lujo) - Exclusivo
• 🎤 Party World KTV (karaoke) - Tradición
• 🍻 The Camel (bar expat) - Internacional
• 🌙 Bar Rouge (vistas espectaculares) - Vistas
• 🎭 Shanghai Grand Theatre (shows) - Cultura

💡 **Dato curioso:** Shanghai tiene más de 10,000 bares y clubs. ¡Imposible visitarlos todos!

🍸 **Consejo de experto:** Los bares con vistas al Bund son más caros pero valen la pena por la experiencia.""",
        "https://www.youtube.com/embed/dsVDXeGNh8M",
        "/calendar_enhanced/15.png"
    ),
    (
        "🏃‍♂️ ¡DEPORTES Y ACTIVIDADES! 🧘‍♀️",
        """¡Shanghai es perfecta para mantenerse activo! ¡Prepárate para sus mejores actividades deportivas! 🏃‍♀️

🎯 **RETO DEL DÍA:**
¡DESAFÍO DEPORTIVO ÉPICO! Busca una actividad deportiva de Shanghai que te gustaría probar y haz un video imitándola. ¡Luego grita '¡EN SHANGHAI SERÉ DEPORTISTA!' ¡El más atlético gana! 🏃‍♂️🎬🏆

🧳 **Preparativos de maleta:**
• 👟 Prepara ropa deportiva cómoda
• 🧘‍♀️ Investiga sobre Tai Chi
• 🚴‍♂️ Busca rutas de ciclismo
• 🎯 Planifica actividades matutinas

💡 **Tip del día:** El Tai Chi al amanecer en People's Park es una experiencia única - ¡prueba!

🎥 **Video del día:** Graba un video haciendo ejercicio con música épica y texto: "Día 16 – Deportes y actividades 🏃‍♂️🧘‍♀️"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "Las mejores compras son las que cuentan una historia. ¡Cada actividad deportiva será una historia de superación! 🏃‍♂️",
        "🏃‍♂️ **Actividades deportivas:**\n• 🧘‍♀️ Tai Chi en People's Park\n• 🚴‍♂️ Ciclismo por el Bund\n• 🏃‍♀️ Running en Century Park\n• 🧘‍♂️ Yoga en Xintiandi\n• 🏊‍♀️ Natación en hoteles\n• 🎾 Tenis en clubes locales\n\n💡 **Tip del día:** El Tai Chi al amanecer en People's Park es una experiencia única - ¡prueba!",
        "https://www.youtube.com/embed/S1QzWUb4SnQ",
        "/calendar_enhanced/16.png"
    ),
    (
        "🏗️ ¡ARQUITECTURA DE SHANGHAI! 🏙️",
        """¡Shanghai es un museo de arquitectura al aire libre! ¡Prepárate para ver sus rascacielos! 🌆

🎯 **RETO DEL DÍA:**
¡DESAFÍO ARQUITECTÓNICO ÉPICO! Busca el rascacielos más alto de Shanghai y haz un video imitando su forma. ¡Luego grita '¡EN SHANGHAI SERÉ ARQUITECTO!' ¡El más creativo gana! 🏗️🎬🏆

🧳 **Preparativos de maleta:**
• 📸 Prepara cámara para fotos
• 🏗️ Investiga sobre arquitectura de Shanghai
• 🎯 Planifica qué edificios visitar
• 📱 Descarga apps de arquitectura

💡 **Tip del día:** La Torre de Shanghai es el segundo edificio más alto del mundo con 632 metros.

🎥 **Video del día:** Graba un video imitando edificios con música épica y texto: "Día 17 – Arquitectura 🏗️🏙️"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La arquitectura es música congelada. ¡Cada edificio de Shanghai es una sinfonía visual! 🏗️",
        """🏗️ **Rascacielos icónicos de Shanghai:**
• 🏗️ Torre de Shanghai (632m) - ¡EL MÁS ALTO!
• 🏢 Jin Mao Tower (420m) - Clásico
• 🏙️ Shanghai World Financial Center (492m) - Icono
• 🏛️ Bund (arquitectura colonial) - Historia
• 🏗️ Oriental Pearl Tower (468m) - Futurista
• 🏢 Shanghai Tower (632m) - Moderno

💡 **Dato curioso:** La Torre de Shanghai es el segundo edificio más alto del mundo con 632 metros.

🏗️ **Consejo de experto:** Visita los miradores de los rascacielos al atardecer para ver la ciudad iluminada.""",
        "https://www.youtube.com/embed/51Op3A-8HSA",
        "/calendar_enhanced/17.png"
    ),
    (
        "🌿 ¡NATURALEZA DE SHANGHAI! 🌸",
        """¡Descubre los oasis verdes de Shanghai! ¡Prepárate para la naturaleza china! 🌳

🎯 **RETO DEL DÍA:**
¡DESAFÍO NATURALEZA ÉPICO! Busca información sobre Wuzhen y haz un video imitando el Tai Chi. ¡Luego grita '¡EN SHANGHAI SERÉ ZEN!' ¡El más relajado gana! 🌿🎬🏆

🧳 **Preparativos de maleta:**
• 🧘‍♀️ Prepara ropa cómoda para parques
• 📸 Prepara cámara para naturaleza
• 🌿 Investiga sobre jardines chinos
• 🎯 Planifica qué parques visitar en Shanghai

💡 **Tip del día:** Wuzhen es una ciudad acuática de 1,300 años considerada la Venecia de China.

🎥 **Video del día:** Graba un video haciendo Tai Chi con música épica y texto: "Día 18 – Naturaleza 🌿🌸"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La naturaleza es el mejor antídoto contra el estrés urbano. ¡Cada parque es un refugio de paz! 🌿",
        """🌿 **Parques y naturaleza en Shanghai:**
• 🌿 Yu Garden (jardín clásico) - ¡IMPRESCINDIBLE!
• 🌸 Century Park (parque moderno) - Grande
• 🌳 Zhongshan Park (parque histórico) - Tradición
• 🏮 Wuzhen (ciudad acuática) - ¡MÁGICA!
• 🌊 Huangpu Park (junto al río) - Vistas

💡 **Dato curioso:** Wuzhen es una ciudad acuática de 1,300 años considerada la Venecia de China.

🌿 **Consejo de experto:** Visita los jardines por la mañana temprano para evitar multitudes y disfrutar de la tranquilidad.""",
        "https://www.youtube.com/embed/SkWSR6EgS3I",
        "/calendar_enhanced/18.png"
    ),
    (
        "💭 ¡FRASE DEL DÍA! ✨",
        """Los recuerdos son el único tesoro que puedes llevarte contigo. ¡Shanghai nos dará tesoros infinitos! 💎

🎯 **RETO DEL DÍA:**
¡DESAFÍO RECUERDOS ÉPICO! Haz una foto de algo que te recuerde a Shanghai en tu ciudad. ¡Puede ser un farolillo, dragón, o lo que se te ocurra! ¡El más creativo gana! 📸🏮🏆

🧳 **Preparativos de maleta:**
• 📸 Prepara cámara para recuerdos
• 🎯 Busca elementos chinos en tu ciudad
• 📱 Descarga apps de fotos
• 🎨 Prepara para crear arte

💡 **Tip del día:** Los recuerdos se fortalecen cuando los compartes con otros.

🎥 **Video del día:** Graba un video explicando tu foto con música épica y texto: "Día 19 – Frase del día 💭✨"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "Los recuerdos son el único tesoro que aumenta con el tiempo.",
        """💭 **Creando recuerdos únicos:**
• 🏮 Tiendas de productos chinos
• 🐉 Estatuas o decoraciones asiáticas
• 🏛️ Museos con arte oriental
• 🌸 Jardines con estilo asiático

💡 **Dato curioso:** Los recuerdos se fortalecen cuando los compartes con otros.

📸 **Consejo de experto:** Haz fotos de elementos chinos en tu ciudad para crear conexiones visuales con Shanghai.""",
        "https://www.youtube.com/embed/memories-shanghai",
        "/calendar_enhanced/19.png"
    ),
    (
        "🎒 ¡ÚLTIMOS PREPARATIVOS! ✈️",
        """¡Solo quedan 5 días! ¡Revisa que tengas todo: cargadores, medicinas, ¡y muchas ganas! ⚡

🎯 **RETO DEL DÍA:**
¡DESAFÍO MALETA ÉPICO! Haz una foto de tu maleta/equipaje preparado para Shanghai. ¡Incluye algo especial que te lleves! ¡El más organizado gana! 🧳✈️🏆

🧳 **Preparativos de maleta:**
• 🔌 Revisa cargadores y adaptadores
• 💊 Prepara medicinas básicas
• 👕 Organiza ropa para clima subtropical
• 🎯 Haz lista de verificación final

💡 **Tip del día:** El enchufe en China es diferente - necesitarás un adaptador universal.

🎥 **Video del día:** Graba un video mostrando tu maleta con música épica y texto: "Día 20 – Últimos preparativos 🎒✈️"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "Los últimos detalles son los que marcan la diferencia.",
        """🎒 **Lista final de preparativos:**
• 🏥 Farmacia (medicinas)
• 🛒 Tienda de electrónicos (adaptadores)
• 🧳 Tienda de maletas
• 📱 Tienda de móviles (cargadores)

💡 **Dato curioso:** El enchufe en China es diferente - necesitarás un adaptador universal.

🎒 **Consejo de experto:** Haz una lista de verificación final y táchala conforme vayas completando cada item.""",
        "https://www.youtube.com/embed/travel-packing-guide",
        "/calendar_enhanced/20.png"
    ),
    (
        "💪 ¡FRASE MOTIVACIONAL FINAL! 🚀",
        """La aventura comienza cuando sales de tu zona de confort. ¡Shanghai nos espera! 🌍

🎯 **RETO DEL DÍA:**
¡DESAFÍO EMOCIÓN ÉPICO! Haz un video de 10 segundos diciendo por qué estás emocionado por Shanghai. ¡Que se note la pasión! ¡El más emocionado gana! 🎬🔥🏆

🧳 **Preparativos de maleta:**
• 💪 Prepara actitud aventurera
• 🎯 Visualiza la aventura
• 📱 Prepara para documentar
• 🚀 ¡Activa modo aventurero!

💡 **Tip del día:** Shanghai está a 9,000 km de distancia. ¡Vamos a cruzar medio mundo!

🎥 **Video del día:** Graba un video de motivación con música épica y texto: "Día 21 – Frase motivacional final 💪🚀"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La magia sucede fuera de tu zona de confort.",
        """💪 **Preparándote para la aventura:**
• 🏠 Lugares favoritos de tu ciudad
• 🍽️ Restaurantes que extrañarás
• 🌳 Parques locales
• 🏛️ Lugares con recuerdos

💡 **Dato curioso:** Shanghai está a 9,000 km de distancia. ¡Vamos a cruzar medio mundo!

🚀 **Consejo de experto:** Abraza lo desconocido y sé valiente - la magia sucede fuera de tu zona de confort.""",
        "https://www.youtube.com/embed/motivation-travel",
        "/calendar_enhanced/21.png"
    ),
    (
        "⏰ ¡CASI LLEGAMOS! 🎯",
        """¡Solo quedan 3 días! ¡La emoción está por las nubes! ¡Shanghai está a la vuelta de la esquina! 🏮

🎯 **RETO DEL DÍA:**
¡DESAFÍO CUENTA ATRÁS ÉPICO! Haz un video contando del 3 al 1 y gritando "¡SHANGHAI NOS ESPERA!" ¡Que se escuche en toda la casa! ¡El más ruidoso gana! 🎊📢🏆

🧳 **Preparativos de maleta:**
• ⏰ Prepara cuenta atrás final
• 🎯 Visualiza la aventura
• 📱 Prepara para documentar
• 🚀 ¡Activa modo aventurero!

💡 **Tip del día:** En 3 días estaremos volando hacia Shanghai. ¡El tiempo vuela cuando te diviertes!

🎥 **Video del día:** Graba un video de cuenta atrás con música épica y texto: "Día 22 – Casi llegamos ⏰🎯"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La emoción es el mejor equipaje para cualquier viaje.",
        """⏰ **Últimos días antes del viaje:**
• 🏠 Casa - ¡últimos días!
• 🍽️ Restaurantes favoritos
• 🌳 Lugares especiales
• 🏛️ Lugares con recuerdos

💡 **Dato curioso:** En 3 días estaremos volando hacia Shanghai. ¡El tiempo vuela cuando te diviertes!

⏰ **Consejo de experto:** Mantén la emoción y comparte con el grupo - ¡estos últimos días son especiales!""",
        "https://www.youtube.com/embed/countdown-shanghai",
        "/calendar_enhanced/22.png"
    ),
    (
        "🎄 ¡ÚLTIMA NOCHE ANTES DEL VIAJE! 🏮",
        """¡Mañana es Nochebuena y pasado mañana... ¡NOS VAMOS A SHANGHAI! 🎄🏮
¡Última noche para preparar todo y disfrutar de la emoción!

🎯 **RETO DEL DÍA:**
¡DESAFÍO ÚLTIMA NOCHE ÉPICO! Haz una foto de tu maleta/equipaje preparado para Shanghai. ¡Incluye algo especial que te lleves! ¡El más organizado gana! 🧳✈️🏆

🧳 **Preparativos de maleta:**
• 🎄 Prepara para Nochebuena
• ✈️ Revisa maleta final
• 🎯 Visualiza la aventura
• 🚀 ¡Activa modo aventurero!

💡 **Tip del día:** El vuelo dura aproximadamente 12 horas. ¡Tendremos Navidad en el aire!

🎥 **Video del día:** Graba un video de preparación final con música épica y texto: "Día 23 – Última noche 🎄🏮"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "¡La aventura más épica de nuestras vidas comienza en 2 días! ¡Nochebuena + vuelo a Shanghai = ¡NAVIDAD PERFECTA!",
        """🎄 **Última noche antes del viaje:**
• 🏠 Casa - ¡Última noche!
• 🧳 Maletas preparadas
• 📱 Apps descargadas
• ✈️ Documentos listos

💡 **Dato curioso:** El vuelo dura aproximadamente 12 horas. ¡Tendremos Navidad en el aire!

🎄 **Consejo de experto:** Disfruta la última noche en casa y prepárate para la aventura más épica de nuestras vidas.""",
        "https://www.youtube.com/embed/b1LkyFaXHtI",
        "/calendar_enhanced/23.png"
    ),
    (
        "🎄 ¡NOCHEBUENA ÉPICA! 🏮",
        """¡HOY ES NOCHEBUENA! ¡Cenamos con nuestras familias y mañana... ¡NOS VAMOS A SHANGHAI! 🎄🏮
¡Salimos a las 3 de la madrugada hacia Madrid, esperamos en el aeropuerto y volamos el 25 por la mañana!

🎯 **RETO DEL DÍA:**
¡DESAFÍO NOCHEBUENA ÉPICO! ¡Hoy cenamos con nuestras familias y mañana... ¡NOS VAMOS A SHANGHAI! 🎄✈️ Comparte una foto de tu cena navideña + tu cara de "¡mañana estoy en el avión!" ¡Que se note la emoción! ¡El más emocionado gana! 🏮🎊🏆

🧳 **Preparativos de maleta:**
• 🎄 Disfruta la cena navideña
• ✈️ Prepara para salida a las 3 AM
• 🎯 Visualiza la aventura
• 🚀 ¡Activa modo aventurero!

💡 **Tip del día:** El vuelo sale a las 10 de la mañana del 25. ¡Navidad en el avión!

🎥 **Video del día:** Graba un video del brindis navideño con música épica y texto: "Día 24 – Nochebuena épica 🎄🏮"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "¡La aventura más épica de nuestras vidas comienza MAÑANA! ¡Nochebuena + vuelo a Shanghai = ¡NAVIDAD PERFECTA!",
        """🎄 **Nochebuena épica:**
• 🏠 Casa familiar - ¡Última cena!
• 🚗 Camino a Madrid (3 AM)
• ✈️ Aeropuerto de Madrid
• 🛫 Preparación para el vuelo

💡 **Dato curioso:** El vuelo sale a las 10 de la mañana del 25. ¡Navidad en el avión!

🎄 **Consejo de experto:** Disfruta la cena navideña con la familia y prepárate para la aventura más épica de nuestras vidas.""",
        "https://www.youtube.com/embed/9bZkp7q19f0",
        "/calendar_enhanced/24.png"
    ),
    (
        "✈️ ¡DÍA DEL VUELO A SHANGHAI! 🎊",
        """¡HOY VOLAMOS A SHANGHAI! ¡Después de la Nochebuena épica, hoy es el gran día! ¡El avión nos lleva a la aventura más increíble!

🎯 **RETO DEL DÍA:**
¡DESAFÍO VUELO ÉPICO! Haz una foto en el aeropuerto con tu mejor pose de "¡me voy a Shanghai!" ¡Que se note que es el día más emocionante! ¡El más épico gana! ✈️🎊🏆

🧳 **Preparativos de maleta:**
• ✈️ Prepara para el vuelo
• 🎯 Visualiza la aventura
• 📱 Prepara para documentar
• 🚀 ¡Activa modo aventurero!

💡 **Tip del día:** El vuelo cruza 9,000 km y 7 zonas horarias. ¡Vamos a cruzar medio mundo!

🎥 **Video del día:** Graba un video en el aeropuerto con música épica y texto: "Día 25 – Día del vuelo ✈️🎊"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "¡El avión despega y con él nuestros sueños! ¡Shanghai nos espera al otro lado del mundo!",
        """✈️ **Día del vuelo a Shanghai:**
• ✈️ Aeropuerto de Madrid - ¡DESPEGUE!
• ☁️ Cielos internacionales
• 🌍 Cruce de continentes
• 🛬 Aeropuerto de Shanghai (mañana)

💡 **Dato curioso:** El vuelo cruza 9,000 km y 7 zonas horarias. ¡Vamos a cruzar medio mundo!

✈️ **Consejo de experto:** Disfruta cada momento del vuelo - ¡es parte de la aventura!""",
        "https://www.youtube.com/embed/WJd-BopESW0",
        "/calendar_enhanced/25.png"
    ),
    (
        "🏮 ¡LLEGAMOS A SHANGHAI! ✨",
        """¡FELIZ NAVIDAD EN SHANGHAI! ¡Hemos llegado a la ciudad de los sueños! ¡Que empiece la magia! 🎄

🎯 **RETO DEL DÍA:**
¡DESAFÍO LLEGADA ÉPICO! ¡Primera foto en Shanghai! Haz una foto en el aeropuerto con tu mejor pose de "¡HEMOS LLEGADO!" ¡Que se note la emoción! ¡El más emocionado gana! 🏮🎊🏆

🧳 **Preparativos de maleta:**
• 🏮 ¡Disfruta la llegada!
• 🎯 Visualiza la aventura
• 📱 Prepara para documentar
• 🚀 ¡Activa modo aventurero!

💡 **Tip del día:** Shanghai recibe más de 30 millones de turistas al año. ¡Somos parte de esa estadística!

🎥 **Video del día:** Graba un video de llegada con música épica y texto: "Día 26 – Llegada a Shanghai 🏮✨"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "¡Hemos llegado! Ahora comienza la verdadera aventura. ¡Que empiece la magia de Shanghai! 🏮",
        """🏮 **Llegada a Shanghai:**
• 🏮 Aeropuerto de Shanghai - ¡PRIMER CONTACTO!
• 🌃 Bund - Vistas espectaculares
• 🏙️ Torre de Shanghai - Skyline
• 🏮 Yu Garden - Tradición
• 🚇 Metro de Shanghai - Movilidad
• 🍜 Mercados de comida - Autenticidad

💡 **Dato curioso:** Shanghai recibe más de 30 millones de turistas al año. ¡Somos parte de esa estadística!

🏮 **Consejo de experto:** Disfruta cada momento de la llegada - ¡es el comienzo de la aventura más épica de nuestras vidas!""",
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
