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
        "🗓 Faltan 30 días para Shanghái 🇨🇳",
        "🎉 ¡Empieza la cuenta atrás!\nHoy arranca la misión \"Shanghái 2025\".\nReto del día: cambia tu fondo de pantalla por algo relacionado y mándalo al grupo.\n🔥 Empieza la motivación.",
        "La aventura comienza con un solo paso. ¡Y ese paso es hoy! 🚀",
        "• 📄 Revisa tu pasaporte (debe tener 6+ meses de validez)\n• 📱 Descarga apps útiles: Google Translate, Maps\n• 🎒 Empieza a hacer lista de maletas",
        "https://www.youtube.com/embed/dQw4w9WgXcQ",
        "/1.png"
    ),
    (
        "🗓 Faltan 29 días para Shanghái 💳",
        "Momento de ser responsables: toca descargar Alipay y activar el Tour Pass.\nComparte pantallazo cuando lo tengas listo.",
        "La preparación es la clave del éxito. ¡Cada app descargada es un paso más cerca! 🔑",
        "• 🧥 Ropa de invierno (temperaturas 0-10°C)\n• 🔌 Adaptadores de corriente (tipo A/C)\n• 💊 Medicinas básicas\n• 🔋 Cargadores y powerbank",
        "",
        "/2.png"
    ),
    (
        "Frase motivacional del día 💪",
        "La distancia se mide en historias que vas a vivir, no en kilómetros. ¡Shanghai nos espera! 🏮",
        "Cada paso que damos nos acerca más a nuestros sueños. ¡Shanghai nos espera!",
        "• Visualiza el viaje perfecto\n• Comparte tu emoción con el grupo\n• ¡Mantén la actitud positiva!",
        "",
        "/3.png"
    ),
    (
        "Documentos importantes 📄",
        "¡No olvides revisar tu pasaporte! Debe tener al menos 6 meses de validez. ¡Mejor prevenir! ✈️",
        "La preparación es la clave del éxito en cualquier aventura.",
        "• Pasaporte con 6+ meses de validez\n• Copias de documentos importantes\n• Seguro de viaje\n• Reservas de vuelo y hotel",
        "",
        "/4.png"
    ),
    (
        "Curiosidad de Shanghai 🏙️",
        "¿Sabías que Shanghai significa 'Sobre el mar'? ¡La ciudad más poblada de China nos espera! 🌊",
        "El conocimiento enriquece cada experiencia de viaje.",
        "• Shanghai = 上海 (Sobre el mar)\n• Población: 24+ millones\n• Fundada en 1074\n• Centro financiero de Asia",
        "https://www.youtube.com/embed/9bZkp7q19f0",
        "/5.png"
    ),
    (
        "Frase del día 🌟",
        "Cada día nos acerca a una nueva aventura. ¡Mantén la emoción viva! 🎯",
        "La emoción es el combustible de los grandes viajes.",
        "• Comparte tu emoción en redes\n• Cuenta los días con ilusión\n• ¡Prepara tu cámara!",
        "",
        "/6.png"
    ),
    (
        "Comida china que probar 🥢",
        "¡Prepárate para el dim sum, el pato laqueado y los fideos de Shanghai! ¡Tu paladar te lo agradecerá! 🍜",
        "La comida es el lenguaje universal que conecta culturas.",
        "• Dim Sum (小笼包)\n• Pato laqueado (北京烤鸭)\n• Fideos de Shanghai (上海面条)\n• Hot Pot (火锅)",
        "",
        "/7.png"
    ),
    (
        "Lugares imperdibles 🏮",
        "El Bund, Yu Garden, Shanghai Tower... ¡Tantos lugares mágicos por descubrir! 📸",
        "Cada lugar tiene una historia que contar.",
        "• El Bund (外滩) - Vista del skyline\n• Yu Garden (豫园) - Jardín clásico\n• Shanghai Tower - Rascacielos\n• Tianzifang - Barrio artístico",
        "https://www.youtube.com/embed/dQw4w9WgXcQ",
        "/8.png"
    ),
    (
        "Frase motivacional 💫",
        "Los viajes son la única inversión que te hace más rico. ¡Shanghai nos enriquecerá! 💎",
        "Los recuerdos son la única riqueza que nadie puede quitarte.",
        "• Invierte en experiencias\n• Documenta cada momento\n• ¡Vive intensamente!",
        "",
        "/9.png"
    ),
    (
        "¿Listos para el vuelo? ✈️",
        "¡Solo quedan 15 días! ¿Ya tienes todo listo para el vuelo? ¡La aventura está cada vez más cerca! 🎉",
        "La preparación es la mitad del éxito.",
        "• Check-in online 24h antes\n• Llegar 3h antes al aeropuerto\n• Documentos a mano\n• ¡Actitud aventurera!",
        "",
        "/10.png"
    ),
    (
        "Cultura china 🇨🇳",
        "¡Aprende a decir 'Ni hao' (hola) y 'Xie xie' (gracias)! ¡Los locales lo apreciarán! 🗣️",
        "El respeto por la cultura local abre puertas y corazones.",
        "• Ni hao (你好) - Hola\n• Xie xie (谢谢) - Gracias\n• Zai jian (再见) - Adiós\n• Bu ke qi (不客气) - De nada",
        "",
        "/11.png"
    ),
    (
        "Frase del día 🌈",
        "La vida es una aventura, atrévete a vivirla. ¡Shanghai será nuestro capítulo más emocionante! 📖",
        "Cada día es una página nueva en el libro de tu vida.",
        "• Escribe tu historia\n• Sé el protagonista\n• ¡Vive sin arrepentimientos!",
        "",
        "/12.png"
    ),
    (
        "Compras en Shanghai 🛍️",
        "¡Nanjing Road y Xintiandi te esperan! ¡Prepárate para las mejores compras de tu vida! 💳",
        "Las mejores compras son las que cuentan una historia.",
        "• Nanjing Road - Calle comercial\n• Xintiandi - Zona trendy\n• Mercados locales\n• ¡Regatea como un pro!",
        "",
        "/13.png"
    ),
    (
        "Transporte en la ciudad 🚇",
        "¡El metro de Shanghai es súper eficiente! ¡Descarga la app Metro Shanghai! 📱",
        "Moverse como un local es la mejor forma de conocer una ciudad.",
        "• App Metro Shanghai\n• Taxi con Didi\n• Bicicletas compartidas\n• ¡Explora caminando!",
        "",
        "/14.png"
    ),
    (
        "¡Mitad del camino! 🎯",
        "¡Ya estamos a mitad del camino! ¡Solo quedan 10 días para la aventura más épica! 🚀",
        "El punto medio es donde la emoción alcanza su pico.",
        "• ¡Mantén la emoción!\n• Comparte con el grupo\n• ¡Prepara la cuenta atrás final!",
        "https://www.youtube.com/embed/jNQXAC9IVRw",
        "/15.png"
    ),
    (
        "Frase motivacional ⭐",
        "No cuentes los días, haz que los días cuenten. ¡Cada día nos acerca a Shanghai! ⏰",
        "El tiempo es el recurso más valioso que tenemos.",
        "• Vive cada día intensamente\n• Aprovecha cada momento\n• ¡Haz que cuente!",
        "",
        "/16.png"
    ),
    (
        "Nochevieja en Shanghai 🎊",
        "¡Vamos a celebrar el Año Nuevo en Shanghai! ¡Será una nochevieja inolvidable! 🎆",
        "Celebrar en un lugar nuevo es crear recuerdos únicos.",
        "• Fuegos artificiales en el Bund\n• Cena especial\n• ¡Brindis con vista al skyline!\n• ¡Fotos épicas!",
        "",
        "/17.png"
    ),
    (
        "Fotos épicas 📸",
        "¡Prepárate para las fotos más increíbles! ¡Shanghai es un paraíso para Instagram! 📷",
        "Una foto vale más que mil palabras, pero un recuerdo vale más que mil fotos.",
        "• Bund al atardecer\n• Skyline nocturno\n• Yu Garden clásico\n• ¡Selfies en la Torre!",
        "",
        "/18.png"
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
        "Última noche en casa 🌙",
        "¡Mañana volamos! ¡Disfruta tu última noche en casa, porque mañana... ¡SHANGHAI! ✈️",
        "La última noche es la más emocionante de todas.",
        "• Descansa bien\n• Revisa todo una vez más\n• ¡Disfruta la emoción!",
        "",
        "/23.png"
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
        "¡Llegamos a Shanghai! 🏮",
        "¡FELIZ NAVIDAD EN SHANGHAI! ¡Hemos llegado a la ciudad de los sueños! ¡Que empiece la magia! ✨🎄",
        "¡Hemos llegado! Ahora comienza la verdadera aventura.",
        "• ¡Bienvenidos a Shanghai!\n• Primera foto en el aeropuerto\n• ¡Explora la ciudad!\n• ¡Disfruta cada momento!",
        "https://www.youtube.com/embed/dQw4w9WgXcQ",
        "/25.png"
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
