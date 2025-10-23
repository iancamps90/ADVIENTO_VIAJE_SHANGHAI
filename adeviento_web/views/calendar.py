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
• 📄 Revisa tu pasaporte (debe tener 6+ meses de validez)
• 📱 Descarga apps útiles: Google Translate, Maps, Alipay
• 🎒 Empieza a hacer lista de maletas
• 🎯 Cambia fondo de pantalla y comparte en el grupo

💡 **Tip del día:** Shanghai significa 'Sobre el mar' - ¡perfecto para nuestra aventura!

🏮 **Progreso del viaje:** 1/25 - ¡Solo empezamos!

🎥 **Video del día:** Graba un video presentándote como "aventurero rumbo a Shanghai" con tu mejor pose épica.

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
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

**🎯 RETO DEL DÍA:**
¡MISIÓN DIGITAL ÉPICA! Descarga Alipay y activa el Tour Pass. ¡Comparte pantallazo + un selfie celebrando que ya eres "digitalmente chino"! ¡Bonus si lo haces con cara de espía! 📱🇨🇳🕵️

**¿Por qué es importante?** En China se paga TODO con el móvil. ¡Sin Alipay no hay paraíso! 🏮

**¿Qué nos espera?** Un mundo digital completamente diferente donde el móvil es tu llave para todo.

**Dato curioso:** China tiene 1.4 mil millones de usuarios de pagos móviles. ¡Somos una gota en el océano!

**¿Sabías que...?** Alipay procesa más transacciones que Visa y Mastercard juntas.

**🎥 Video del día:** Graba un video configurando Alipay con música épica y texto: "Día 2 – Convirtiéndome en digital chino 📱🇨🇳"

**🧳 Preparativos de maleta:** Hoy revisa que tengas cargadores universales y adaptadores para China. ¡Sin electricidad no hay aventura!

**💡 Tip del día:** Alipay procesa más transacciones que Visa y Mastercard juntas. ¡Es el rey de los pagos móviles!

**🏮 Progreso del viaje:** 2/25 - ¡Vamos por el 8%!

**🧧 Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La preparación es la clave del éxito. ¡Cada app descargada es un paso más cerca!",
        """🎯 **Actividades del día:**
• Descarga y configura Alipay
• Activa el Tour Pass
• Prueba la función de cámara de Google Translate
• ¡Comparte tu selfie "digitalmente chino"!

💡 **Dato curioso:** En China se paga TODO con el móvil. ¡Sin Alipay no hay paraíso!

🏮 **Progreso del viaje:** 2/25 - ¡Vamos por el 8%!""",
        "https://www.youtube.com/embed/KNMz8WqRS-w",
        "/calendar_enhanced/2.png"
    ),
    (
        "🏮 Curiosidades de Shanghai 🏙️",
        """¡Descubramos juntos los secretos de la ciudad más fascinante de China! 🌟

**🏙️ Curiosidades de Shanghai:**
• Shanghai significa literalmente "Sobre el mar" 🌊
• Tiene el skyline más iluminado del mundo (más de 50 rascacielos con luces LED)
• En cada esquina puedes encontrar un puesto de dumplings frescos 🥟
• Comer con ruido (¡slurp!) es señal de disfrute, no de mala educación 😄

**Reto del día:** ¡BÚSQUEDA DEL TESORO ÉPICA! Encuentra la foto más alucinante de Shanghai que puedas y compártela con tu frase motivacional personal. ¡Que nos emocione a todos! ¡El más épico gana! 🔍✨🏆

**🧠 Dato curioso:** Los palillos no deben clavarse en el arroz. Se asocia a ofrendas funerarias. 👉 Siempre apóyalos sobre el cuenco o en un soporte.

**🎥 Video del día:** Graba tu reacción al ver fotos de Shanghai. Ponle música tipo "China Chill" y texto: "Día 3 – Descubriendo Shanghai 🏮🇨🇳"

**🧳 Preparativos de maleta:** Hoy prepara tu mini botiquín de viaje: Ibuprofeno, Fortasec, tiritas, paracetamol, algo para el mareo o estómago. Añade también un pequeño gel hidroalcohólico y toallitas húmedas.

**💡 Tip del día:** Descarga Google Translate y prueba su función de cámara instantánea para traducir carteles o menús. 🈶 Te salvará en los restaurantes locales en Shanghai.

**🧧 Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto. Así luego las usas para el vídeo resumen final 🎥🔥""",
        "Un viaje se empieza con los ojos… pero se recuerda con el paladar. ✈️🍜",
        """🎯 **Actividades del día:**
• Visualiza el viaje perfecto
• Comparte tu emoción con el grupo
• ¡Mantén la actitud positiva!
• Investiga sobre el Bund y la Torre de Shanghai
• Prueba la función de cámara de Google Translate

💡 **Dato curioso:** El metro de Shanghai tiene 831 km de vías - ¡más que cualquier otra ciudad!

🏮 **Progreso del viaje:** 3/25 - ¡Ya vamos por el 12%!""",
        "https://www.youtube.com/embed/L_jWHffIx5E",
        "/calendar_enhanced/3.png"
    ),
    (
        "📄 ¡DOCUMENTOS Y SEGUROS! ✈️",
        """¡Momento de ser súper organizados! Hoy toca revisar que tenemos todos los papeles en regla. 📋

**🎯 RETO DEL DÍA:**
¡CHECKPOINT DOCUMENTOS ÉPICO! Haz una foto de tu pasaporte (solo portada) + tu cara de "¡estoy listo para la aventura!" ¡Demuestra que eres un viajero responsable! ¡Bonus si haces pose de superhéroe! ✈️📄🦸

**¿Por qué es crucial?** Sin documentos en regla, no hay viaje. ¡Mejor prevenir que lamentar! 🛡️

**¿Qué nos espera?** Un proceso de documentación que puede ser complejo pero es esencial.

**Dato curioso:** China requiere pasaporte con 6+ meses de validez. ¡Muchos países no lo saben!

**¿Sabías que...?** El seguro de viaje puede ahorrarte miles de euros en caso de emergencia.

**🎥 Video del día:** Graba un video revisando tus documentos con música épica y texto: "Día 4 – Viajero responsable ✈️📄"

**🧳 Preparativos de maleta:** Hoy organiza una carpeta digital con todos tus documentos importantes. ¡Guárdala en la nube por seguridad!

**💡 Tip del día:** China requiere pasaporte con 6+ meses de validez. ¡Muchos países no lo saben!

**🏮 Progreso del viaje:** 4/25 - ¡Vamos por el 16%!

**🧧 Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La preparación es la clave del éxito en cualquier aventura. ¡Cada documento revisado es tranquilidad ganada!",
        """🎯 **Actividades del día:**
• Revisa tu pasaporte (6+ meses de validez)
• Organiza documentos importantes
• Contrata seguro de viaje
• ¡Haz tu foto de superhéroe con pasaporte!

💡 **Dato curioso:** El seguro de viaje puede ahorrarte miles de euros en caso de emergencia.

🏮 **Progreso del viaje:** 4/25 - ¡Vamos por el 16%!""",
        "https://www.youtube.com/embed/H3HrJgYtjjY",
        "/calendar_enhanced/4.png"
    ),
    (
        "🍜 ¡COMIDA CHINA AUTÉNTICA! 🥢",
        """¡Hora de preparar el estómago para la aventura culinaria más épica! 🍽️

**🎯 RETO DEL DÍA:**
¡AVENTURA CULINARIA ÉPICA! Ve a un restaurante chino y pide algo que NUNCA hayas probado. ¡Comparte foto del plato + tu cara de sorpresa! ¿Serás valiente? ¡El más atrevido gana! 🥢😱🏆

**¿Qué nos espera?** Dim sum, xiaolongbao, hot pot... ¡Shanghai es el paraíso de la comida callejera! 🌟

**¿Por qué es importante?** La comida es la puerta de entrada a la cultura china. ¡Cada plato cuenta una historia!

**Dato curioso:** Shanghai tiene más de 50,000 restaurantes. ¡Imposible probarlos todos en una vida!

**¿Sabías que...?** El xiaolongbao se inventó en Shanghai en 1875 y se come con una técnica especial para no quemarse.

**🎥 Video del día:** Graba un video probando comida china con música épica y texto: "Día 5 – Aventura culinaria 🍜🥢"

**🧳 Preparativos de maleta:** Hoy investiga sobre la comida china que más te llama la atención. ¡Haz una lista de platos que quieres probar en Shanghai!

**💡 Tip del día:** Shanghai tiene más de 50,000 restaurantes. ¡Imposible probarlos todos en una vida!

**🏮 Progreso del viaje:** 5/25 - ¡Vamos por el 20%!

**🧧 Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La comida es el lenguaje universal que conecta culturas. ¡Cada bocado nos acerca más a Shanghai!",
        """🎯 **Actividades del día:**
• Busca restaurante chino local
• Pide algo que nunca hayas probado
• Comparte foto del plato + tu cara de sorpresa
• ¡Investiga sobre xiaolongbao!

💡 **Dato curioso:** El xiaolongbao se inventó en Shanghai en 1875 y se come con una técnica especial para no quemarse.

🏮 **Progreso del viaje:** 5/25 - ¡Vamos por el 20%!""",
        "https://www.youtube.com/embed/f1yIX7EMhQE",
        "/calendar_enhanced/5.png"
    ),
    (
        "🚇 ¡TRANSPORTE EN SHANGHAI! 🚌",
        """¡Hora de dominar el sistema de transporte más eficiente del mundo! 🚇

**🎯 RETO DEL DÍA:**
¡PLANIFICADOR DE RUTAS ÉPICO! Descarga la app del metro de Shanghai y diseña tu ruta perfecta para el primer día. ¡Comparte tu itinerario épico! ¡El más creativo gana! 🚇🗺️🏆

**¿Sabías que?** El metro de Shanghai transporta 10+ millones de personas al día. ¡Vamos a ser parte de esa estadística! 📊

**¿Por qué es importante?** El transporte público es la clave para explorar Shanghai como un local.

**Dato curioso:** Shanghai tiene el metro más largo del mundo con 831 km de vías. ¡Más que cualquier otra ciudad!

**¿Sabías que...?** Puedes pagar el metro con Alipay escaneando códigos QR.

**🎥 Video del día:** Graba un video planificando tu ruta con música épica y texto: "Día 6 – Planificador de rutas 🚇🗺️"

**🧳 Preparativos de maleta:** Hoy investiga sobre las estaciones de metro más importantes de Shanghai. ¡Haz una lista de las que quieres visitar!

**💡 Tip del día:** Shanghai tiene el metro más largo del mundo con 831 km de vías. ¡Más que cualquier otra ciudad!

**🏮 Progreso del viaje:** 6/25 - ¡Vamos por el 24%!

**🧧 Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La emoción es el combustible de los grandes viajes. ¡Cada línea de metro nos lleva a una nueva aventura!",
        """🎯 **Actividades del día:**
• Descarga app del metro de Shanghai
• Diseña tu ruta perfecta para el primer día
• Comparte tu itinerario épico
• ¡Aprende a pagar con Alipay!

💡 **Dato curioso:** El metro de Shanghai transporta 10+ millones de personas al día. ¡Vamos a ser parte de esa estadística!

🏮 **Progreso del viaje:** 6/25 - ¡Vamos por el 24%!""",
        "https://www.youtube.com/embed/XVvhsfVz-WE",
        "/calendar_enhanced/6.png"
    ),
    (
        "🏛️ ¡LUGARES IMPRESCINDIBLES! 🎯",
        """¡Hora de crear nuestra lista de deseos de Shanghai! 🗺️

**🎯 RETO DEL DÍA:**
¡LISTA DE DESEOS ÉPICA! Elige tu TOP 3 lugares que NO te puedes perder en Shanghai. ¡Comparte tu lista + por qué cada lugar te emociona! ¡El más emocionante gana! 🏛️❤️🏆

**¿Cuáles son tus favoritos?** Bund, Torre de Shanghai, Templo del Buda de Jade... ¡Hay tanto que ver! 🌟

**¿Por qué es importante?** Shanghai tiene lugares icónicos que definen la ciudad. ¡No podemos perdérnoslos!

**Dato curioso:** El Bund tiene 52 edificios de diferentes estilos arquitectónicos. ¡Un museo al aire libre!

**¿Sabías que...?** La Torre de Shanghai es el segundo edificio más alto del mundo con 632 metros.

**🎥 Video del día:** Graba un video presentando tus 3 lugares favoritos con música épica y texto: "Día 7 – Lista de deseos 🏛️❤️"

**🧳 Preparativos de maleta:** Hoy investiga sobre los horarios y precios de tus lugares favoritos. ¡Haz una lista de entradas que necesitas comprar!

**💡 Tip del día:** El Bund tiene 52 edificios de diferentes estilos arquitectónicos. ¡Un museo al aire libre!

**🏮 Progreso del viaje:** 7/25 - ¡Vamos por el 28%!

**🧧 Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "La comida es el lenguaje universal que conecta culturas. ¡Cada lugar que visitemos será una historia que contar!",
        """🎯 **Actividades del día:**
• Elige tu TOP 3 lugares que NO te puedes perder
• Comparte tu lista + por qué cada lugar te emociona
• Planifica rutas para visitarlos
• ¡Investiga horarios y precios!

💡 **Dato curioso:** La Torre de Shanghai es el segundo edificio más alto del mundo con 632 metros.

🏮 **Progreso del viaje:** 7/25 - ¡Vamos por el 28%!""",
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
        "🎵 ¡MÚSICA Y ENTRETENIMIENTO! 🎪",
        """¡Shanghai nunca duerme! ¡Descubramos su vibrante escena musical y de entretenimiento! 🎶

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
        "🏃‍♂️ ¡DEPORTES Y ACTIVIDADES! 🧘‍♀️",
        """¡Shanghai es perfecta para mantenerse activo! ¡Descubramos sus mejores actividades deportivas! 🏃‍♀️

🎯 **RETO DEL DÍA:**
¡DESAFÍO DEPORTIVO ÉPICO! Busca una actividad deportiva de Shanghai que te gustaría probar y haz un video imitándola. ¡Luego grita '¡EN SHANGHAI SERÉ DEPORTISTA!' ¡El más atlético gana! 🏃‍♂️🎬🏆

🧳 **Preparativos de maleta:**
• 👟 Prepara ropa deportiva cómoda
• 🧘‍♀️ Investiga sobre Tai Chi
• 🚴‍♂️ Busca rutas de ciclismo
• 🎯 Planifica actividades matutinas

💡 **Tip del día:** El Tai Chi al amanecer en People's Park es una experiencia única - ¡prueba!

🎥 **Video del día:** Graba un video haciendo ejercicio con música épica y texto: "Día 13 – Deportes y actividades 🏃‍♂️🧘‍♀️"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
        "Las mejores compras son las que cuentan una historia. ¡Cada actividad deportiva será una historia de superación! 🏃‍♂️",
        "🏃‍♂️ **Actividades deportivas:**\n• 🧘‍♀️ Tai Chi en People's Park\n• 🚴‍♂️ Ciclismo por el Bund\n• 🏃‍♀️ Running en Century Park\n• 🧘‍♂️ Yoga en Xintiandi\n• 🏊‍♀️ Natación en hoteles\n• 🎾 Tenis en clubes locales\n\n💡 **Tip del día:** El Tai Chi al amanecer en People's Park es una experiencia única - ¡prueba!",
        "https://www.youtube.com/embed/shanghai-sports-activities",
        "/calendar_enhanced/13.png"
    ),
    (
        "💻 ¡TECNOLOGÍA CHINA! 🚀",
        """¡Shanghai es el Silicon Valley de Asia! ¡Descubramos las innovaciones tecnológicas más increíbles! 🤖

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
        """¡Shanghai nunca duerme! ¡Descubramos su vibrante vida nocturna! 🌙

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
        "🍜 ¡COMIDA CALLEJERA ÉPICA! 🥢",
        """¡100 horas de comida callejera china! ¡Prepárate para la aventura culinaria más intensa! 🍽️

🎯 **RETO DEL DÍA:**
¡DESAFÍO COMIDA CALLEJERA ÉPICO! Busca un plato de comida callejera china que nunca hayas probado y haz un video comiéndolo. ¡Luego grita '¡EN SHANGHAI SERÉ COMILÓN!' ¡El más aventurero gana! 🍜🎬🏆

🧳 **Preparativos de maleta:**
• 🍽️ Prepara estómago aventurero
• 📱 Descarga apps de comida
• 🥢 Practica con palillos
• 🎯 Investiga platos únicos

💡 **Tip del día:** Shanghai tiene más de 50,000 puestos de comida callejera. ¡Imposible probarlos todos!

🎥 **Video del día:** Graba un video probando comida china con música épica y texto: "Día 16 – Comida callejera 🍜🥢"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
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
        "🏗️ ¡ARQUITECTURA MODERNA DE SHANGHAI! 🏙️",
        """¡Shanghai es un museo de arquitectura al aire libre! ¡Descubramos sus rascacielos más impresionantes! 🌆

🎯 **RETO DEL DÍA:**
¡DESAFÍO ARQUITECTÓNICO ÉPICO! Busca el rascacielos más alto de Shanghai y haz un video imitando su forma. ¡Luego grita '¡EN SHANGHAI SERÉ ARQUITECTO!' ¡El más creativo gana! 🏗️🎬🏆

🧳 **Preparativos de maleta:**
• 📸 Prepara cámara para fotos
• 🏗️ Investiga sobre arquitectura
• 🎯 Planifica rutas de edificios
• 📱 Descarga apps de arquitectura

💡 **Tip del día:** La Torre de Shanghai es el segundo edificio más alto del mundo con 632 metros.

🎥 **Video del día:** Graba un video imitando edificios con música épica y texto: "Día 17 – Arquitectura 🏗️🏙️"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
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
        "🌿 ¡PARQUES Y NATURALEZA EN SHANGHAI! 🌸",
        """¡Descubre los oasis verdes de Shanghai! ¡Incluso en la ciudad más moderna hay naturaleza! 🌳

🎯 **RETO DEL DÍA:**
¡DESAFÍO NATURALEZA ÉPICO! Busca información sobre Wuzhen y haz un video imitando el Tai Chi. ¡Luego grita '¡EN SHANGHAI SERÉ ZEN!' ¡El más relajado gana! 🌿🎬🏆

🧳 **Preparativos de maleta:**
• 🧘‍♀️ Prepara ropa cómoda para parques
• 📸 Prepara cámara para naturaleza
• 🌿 Investiga sobre jardines chinos
• 🎯 Planifica rutas de naturaleza

💡 **Tip del día:** Wuzhen es una ciudad acuática de 1,300 años considerada la Venecia de China.

🎥 **Video del día:** Graba un video haciendo Tai Chi con música épica y texto: "Día 18 – Parques y naturaleza 🌿🌸"

🧧 **Extra para el grupo:** 📸 Bonus: Cread un álbum compartido llamado "Rumbo a Shanghai" y subid ahí vuestras fotos del reto.""",
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
        """📋 **Checklist del día:**
• ✅ Haz foto de algo que te recuerde a Shanghai
• ✅ Comparte con el grupo
• ✅ Documenta tu progreso
• ✅ ¡Crea recuerdos únicos!

🍽️ **Gastronomía del día:**
• Comida que te recuerde a China
• Restaurante chino local
• Ingredientes asiáticos
• Té chino tradicional

🏛️ **Lugares del día:**
• 🏮 Tiendas de productos chinos
• 🐉 Estatuas o decoraciones asiáticas
• 🏛️ Museos con arte oriental
• 🌸 Jardines con estilo asiático

📱 **Apps y tecnología:**
• Apps de fotografía
• Google Photos (backup)
• Apps de recuerdos
• Redes sociales

🎭 **Cultura y tradiciones:**
• Simbolismo chino
• Tradiciones locales
• Arte asiático
• Filosofía oriental

💡 **Tip del día:** Los recuerdos se fortalecen cuando los compartes

🎯 **Reto extra:** Crea un álbum digital de preparación para Shanghai""",
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
        """📋 **Checklist del día:**
• ✅ Lista final de maletas
• ✅ Cargadores y adaptadores
• ✅ Medicinas básicas
• ✅ ¡Actitud aventurera!

🍽️ **Gastronomía del día:**
• Snacks para el viaje
• Medicinas para el estómago
• Vitaminas y suplementos
• Comida de emergencia

🏛️ **Lugares del día:**
• 🏥 Farmacia (medicinas)
• 🛒 Tienda de electrónicos (adaptadores)
• 🧳 Tienda de maletas
• 📱 Tienda de móviles (cargadores)

📱 **Apps y tecnología:**
• Apps de viaje
• Cargadores universales
• Adaptadores de enchufe
• Power banks

🎭 **Cultura y tradiciones:**
• Preparación cultural
• Últimas tradiciones locales
• Despedidas familiares
• Emoción por el viaje

💡 **Tip del día:** Haz una lista de verificación - ¡no olvides nada!

🎯 **Reto extra:** Graba un video de tu maleta preparada""",
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
        """📋 **Checklist del día:**
• ✅ Abraza lo desconocido
• ✅ Sé valiente
• ✅ ¡Vive la aventura!
• ✅ Comparte tu emoción

🍽️ **Gastronomía del día:**
• Última comida favorita local
• Comida que extrañarás
• Bebidas especiales
• Postres de despedida

🏛️ **Lugares del día:**
• 🏠 Lugares favoritos de tu ciudad
• 🍽️ Restaurantes que extrañarás
• 🌳 Parques locales
• 🏛️ Lugares con recuerdos

📱 **Apps y tecnología:**
• Apps de video
• Redes sociales
• Apps de motivación
• Calendario de cuenta atrás

🎭 **Cultura y tradiciones:**
• Últimas tradiciones locales
• Despedidas emocionales
• Preparación mental
• ¡Emoción por Shanghai!

💡 **Tip del día:** La aventura comienza con la decisión

🎯 **Reto extra:** Graba un video motivacional para el grupo""",
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
        """📋 **Checklist del día:**
• ✅ ¡Mantén la emoción!
• ✅ Comparte con el grupo
• ✅ ¡Prepara la cuenta atrás final!
• ✅ ¡Disfruta estos últimos días!

🍽️ **Gastronomía del día:**
• Comida de celebración
• Bebidas especiales
• Postres de cuenta atrás
• ¡Últimas comidas locales!

🏛️ **Lugares del día:**
• 🏠 Casa - ¡últimos días!
• 🍽️ Restaurantes favoritos
• 🌳 Lugares especiales
• 🏛️ Lugares con recuerdos

📱 **Apps y tecnología:**
• Apps de cuenta atrás
• Redes sociales
• Apps de emoción
• Calendario final

🎭 **Cultura y tradiciones:**
• Últimas tradiciones locales
• Despedidas emocionales
• Preparación final
• ¡Emoción por Shanghai!

💡 **Tip del día:** ¡Disfruta cada momento de la cuenta atrás!

🎯 **Reto extra:** Crea un video de cuenta atrás épico""",
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
        """📋 **Checklist del día:**
• ✅ Última revisión de maletas
• ✅ Documentos finales
• ✅ Cargadores y electrónicos
• ✅ ¡Disfruta la última noche en casa!

🍽️ **Gastronomía del día:**
• Última cena en casa
• Comida favorita local
• Bebidas especiales
• Postres de despedida

🏛️ **Lugares del día:**
• 🏠 Casa - ¡Última noche!
• 🧳 Maletas preparadas
• 📱 Apps descargadas
• ✈️ Documentos listos

📱 **Apps y tecnología:**
• Alipay configurado
• WeChat listo
• Maps descargados
• Traductor preparado

🎭 **Cultura y tradiciones:**
• Últimas tradiciones locales
• Despedida familiar
• Preparación emocional
• ¡Emoción por Shanghai!

💡 **Tip del día:** ¡Última noche en casa! ¡Disfruta y descansa bien!

🎯 **Reto extra:** Graba un video de despedida antes del viaje""",
        "https://www.youtube.com/embed/b1LkyFaXHtI",
        "/calendar_enhanced/23.png"
    ),
    (
        "🎄 ¡Nochebuena épica! 🏮",
        """¡HOY ES NOCHEBUENA! ¡Cenamos con nuestras familias y mañana... ¡NOS VAMOS A SHANGHAI! 🎄🏮
¡Salimos a las 3 de la madrugada hacia Madrid, esperamos en el aeropuerto y volamos el 25 por la mañana!

**Reto del día:** ¡Hoy cenamos con nuestras familias y mañana... ¡NOS VAMOS A SHANGHAI! 🎄✈️ Comparte una foto de tu cena navideña + tu cara de "¡mañana estoy en el avión!" ¡Que se note la emoción! ¡El más emocionado gana! 🏮🎊🏆

**¿Qué nos espera?** Una cena navideña especial con la familia, despedidas emocionantes, y preparación para la aventura más épica.

**¿Por qué es importante?** Es la última Nochebuena en casa antes de volar a Shanghai. ¡Momento único e irrepetible!

**Dato curioso:** Pasaremos Navidad en el aire, volando hacia Shanghai. ¡Una Navidad literalmente por las nubes!

**¿Sabías que...?** El vuelo sale a las 10 de la mañana del 25. ¡Navidad en el avión!""",
        "¡La aventura más épica de nuestras vidas comienza MAÑANA! ¡Nochebuena + vuelo a Shanghai = ¡NAVIDAD PERFECTA!",
        """📋 **Checklist del día:**
• ✅ Cena navideña con familia
• ✅ Despedidas emocionantes
• ✅ Última revisión de maletas
• ✅ ¡Salida a las 3 AM hacia Madrid!

🍽️ **Gastronomía del día:**
• Cena navideña especial
• Comida familiar tradicional
• Bebidas de celebración
• Postres navideños

🏛️ **Lugares del día:**
• 🏠 Casa familiar - ¡Última cena!
• 🚗 Camino a Madrid (3 AM)
• ✈️ Aeropuerto de Madrid
• 🛫 Preparación para el vuelo

📱 **Apps y tecnología:**
• Apps de vuelo activadas
• Notificaciones de aeropuerto
• Maps para llegar a Madrid
• ¡Todo listo para Shanghai!

🎭 **Cultura y tradiciones:**
• Últimas tradiciones navideñas
• Despedidas familiares
• Emoción por el viaje
• ¡Preparación para la aventura!

💡 **Tip del día:** ¡Disfruta cada momento de la cena familiar!

🎯 **Reto extra:** Graba un video del brindis navideño con la familia""",
        "https://www.youtube.com/embed/9bZkp7q19f0",
        "/calendar_enhanced/24.png"
    ),
    (
        "✈️ ¡DÍA DEL VUELO A SHANGHAI! 🎊",
        """¡HOY VOLAMOS A SHANGHAI! ¡Después de la Nochebuena épica, hoy es el gran día! ¡El avión nos lleva a la aventura más increíble!

**Reto del día:** Haz una foto en el aeropuerto con tu mejor pose de "¡me voy a Shanghai!" ¡Que se note que es el día más emocionante! ¡El más épico gana! ✈️🎊🏆

**¿Qué nos espera?** Un vuelo de 12 horas hacia Shanghai. ¡Pasaremos Navidad literalmente por las nubes!

**¿Por qué es especial?** Es el día que hemos estado esperando durante 25 días. ¡La aventura más épica comienza ahora!

**Dato curioso:** El vuelo cruza 9,000 km y 7 zonas horarias. ¡Vamos a cruzar medio mundo!

**¿Sabías que...?** Llegaremos a Shanghai el 26 por la mañana. ¡Navidad en el aire y llegada épica!""",
        "¡El avión despega y con él nuestros sueños! ¡Shanghai nos espera al otro lado del mundo!",
        """📋 **Checklist del día:**
• ✅ ¡Llegar temprano al aeropuerto!
• ✅ Documentos a mano
• ✅ ¡Actitud aventurera!
• ✅ ¡Disfruta cada momento!

🍽️ **Gastronomía del día:**
• Comida del avión
• Snacks para el vuelo
• Bebidas especiales
• ¡Navidad en el aire!

🏛️ **Lugares del día:**
• ✈️ Aeropuerto de Madrid - ¡DESPEGUE!
• ☁️ Cielos internacionales
• 🌍 Cruce de continentes
• 🛬 Aeropuerto de Shanghai (mañana)

📱 **Apps y tecnología:**
• Apps de vuelo activas
• Entretenimiento del avión
• Maps de Shanghai
• ¡Todo listo para aterrizar!

🎭 **Cultura y tradiciones:**
• Primera impresión de China
• Cultura local
• Tradiciones milenarias
• Costumbres chinas

💡 **Tip del día:** ¡Disfruta el vuelo! ¡Es parte de la aventura!

🎯 **Reto extra:** Graba un video del despegue hacia Shanghai""",
        "https://www.youtube.com/embed/WJd-BopESW0",
        "/calendar_enhanced/25.png"
    ),
    (
        "🏮 ¡Llegamos a Shanghai! ✨",
        """¡FELIZ NAVIDAD EN SHANGHAI! ¡Hemos llegado a la ciudad de los sueños! ¡Que empiece la magia! 🎄

**¡MISIÓN CUMPLIDA!** Hemos llegado a Shanghai después de 25 días de preparación. ¡La aventura más épica comienza ahora! 🚀

**Reto del día:** ¡Primera foto en Shanghai! Haz una foto en el aeropuerto con tu mejor pose de "¡HEMOS LLEGADO!" ¡Que se note la emoción! ¡El más emocionado gana! 🏮🎊🏆

**¿Qué nos espera?** Una ciudad llena de sorpresas, cultura milenaria, tecnología futurista... ¡Shanghai nos espera! 🌟

**¿Por qué es especial?** Este es el momento que hemos estado esperando durante 25 días. ¡Cada preparación ha valido la pena!

**Dato curioso:** Shanghai recibe más de 30 millones de turistas al año. ¡Somos parte de esa estadística!

**¿Sabías que...?** Llegamos el 26 por la mañana después de volar toda la Navidad!""",
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
