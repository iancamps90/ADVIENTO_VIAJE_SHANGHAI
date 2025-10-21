import reflex as rx
from adeviento_web.utils.date_utils import is_day_unlocked, get_days_until_unlock


def day(number: int, text: str = "", url: str = "", is_available: bool = True) -> rx.Component:
    """Componente para cada día del calendario con estado de disponibilidad"""
    
    # Verificar si el día está desbloqueado
    day_unlocked = is_day_unlocked(number)
    days_until_unlock = get_days_until_unlock(number)
    
    if day_unlocked and is_available:
        # Día disponible - clickeable
        return rx.box(
            rx.link(
                rx.vstack(
                    # Imagen del día
                    rx.image(
                        src=f"/calendar_enhanced/{number}.png",
                        alt=text,
                        class_name="day-image",
                        loading="lazy"
                    ),
                    # Número del día
                    rx.text(
                        number,
                        class_name="day-number"
                    ),
                    # Indicador de disponible
                    rx.text(
                        "✨",
                        class_name="day-icon"
                    ),
                    width="100%",
                    height="100%",
                    position="relative",
                    class_name="day-available"
                ),
                href=f"/day/{number}",
                external=False,
                width="100%",
                height="100%"
            ),
            class_name="day-card available"
        )
    else:
        # Día bloqueado - no clickeable
        return rx.box(
            rx.vstack(
                # Imagen del día (gris)
                rx.image(
                    src=f"/calendar_enhanced/{number}.png",
                    alt=f"Día {number} - Próximamente",
                    class_name="day-image-locked",
                    loading="lazy"
                ),
                # Número del día
                rx.text(
                    number,
                    class_name="day-number locked"
                ),
                # Candado
                rx.text(
                    "🔒",
                    class_name="day-icon locked"
                ),
                # Texto con días restantes
                rx.text(
                    f"En {days_until_unlock} días" if days_until_unlock > 0 else "Próximamente",
                    class_name="day-locked-text"
                ),
                width="100%",
                height="100%",
                position="relative"
            ),
            class_name="day-card locked"
        )
