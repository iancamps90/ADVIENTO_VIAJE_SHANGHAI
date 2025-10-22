import reflex as rx
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import Color

def special_effects_script() -> rx.Component:
    """Script para efectos especiales en días importantes"""
    return rx.script("""
    // Efectos especiales para días importantes
    function triggerSpecialEffects(dayNumber) {
        const effects = {
            1: () => {
                // Día 1: Explosión de bienvenida
                if (window.ShanghaiAnimations) {
                    window.ShanghaiAnimations.createConfettiExplosion();
                    setTimeout(() => {
                        window.ShanghaiAnimations.createFlyingDragon();
                    }, 1000);
                }
            },
            15: () => {
                // Día 15: Mitad del camino - Efecto especial
                if (window.ShanghaiAnimations) {
                    for (let i = 0; i < 3; i++) {
                        setTimeout(() => {
                            window.ShanghaiAnimations.createConfettiExplosion(
                                Math.random() * window.innerWidth,
                                Math.random() * window.innerHeight
                            );
                        }, i * 500);
                    }
                }
            },
            24: () => {
                // Día 24: Víspera del viaje - Efecto épico
                if (window.ShanghaiAnimations) {
                    // Múltiples explosiones de confeti
                    for (let i = 0; i < 5; i++) {
                        setTimeout(() => {
                            window.ShanghaiAnimations.createConfettiExplosion(
                                Math.random() * window.innerWidth,
                                Math.random() * window.innerHeight
                            );
                        }, i * 300);
                    }
                    
                    // Dragones voladores
                    setTimeout(() => {
                        for (let i = 0; i < 3; i++) {
                            setTimeout(() => {
                                window.ShanghaiAnimations.createFlyingDragon();
                            }, i * 1000);
                        }
                    }, 2000);
                }
            },
            25: () => {
                // Día 25: ¡Llegamos a Shanghai! - Efecto final épico
                if (window.ShanghaiAnimations) {
                    // Explosión masiva de confeti
                    for (let i = 0; i < 10; i++) {
                        setTimeout(() => {
                            window.ShanghaiAnimations.createConfettiExplosion(
                                Math.random() * window.innerWidth,
                                Math.random() * window.innerHeight
                            );
                        }, i * 200);
                    }
                    
                    // Múltiples dragones
                    setTimeout(() => {
                        for (let i = 0; i < 5; i++) {
                            setTimeout(() => {
                                window.ShanghaiAnimations.createFlyingDragon();
                            }, i * 800);
                        }
                    }, 1000);
                    
                    // Estrellas brillantes
                    setTimeout(() => {
                        for (let i = 0; i < 10; i++) {
                            setTimeout(() => {
                                window.ShanghaiAnimations.createShiningStar();
                            }, i * 500);
                        }
                    }, 3000);
                }
            }
        };
        
        if (effects[dayNumber]) {
            effects[dayNumber]();
        }
    }
    
    // Detectar cuando se abre un día especial
    document.addEventListener('DOMContentLoaded', function() {
        const currentPath = window.location.pathname;
        const dayMatch = currentPath.match(/\/day\/(\d+)/);
        
        if (dayMatch) {
            const dayNumber = parseInt(dayMatch[1]);
            setTimeout(() => {
                triggerSpecialEffects(dayNumber);
            }, 1000);
        }
    });
    """)

def celebration_banner(day_number: int) -> rx.Component:
    """Banner de celebración para días especiales"""
    if day_number not in [1, 15, 24, 25]:
        return rx.fragment()
    
    messages = {
        1: "🎊 ¡BIENVENIDOS A LA AVENTURA! 🎊",
        15: "🎯 ¡MITAD DEL CAMINO! ¡SIGAMOS! 🎯",
        24: "✈️ ¡MAÑANA VOLAMOS A SHANGHAI! ✈️",
        25: "🏮 ¡FELIZ NAVIDAD EN SHANGHAI! 🏮"
    }
    
    colors = {
        1: "#FFD700",
        15: "#DC143C", 
        24: "#228B22",
        25: "#FFD700"
    }
    
    return rx.box(
        rx.text(
            messages[day_number],
            font_size=rx.breakpoints(
                initial="1.2em",
                xs="1.4em",
                sm="1.6em",
                md="1.8em",
                lg="2em",
                xl="2em"
            ),
            font_weight="bold",
            color=colors[day_number],
            text_align="center",
            text_shadow="2px 2px 4px rgba(0,0,0,0.8)",
            class_name="celebration-text"
        ),
        padding=Size.BIG.value,
        background=f"linear-gradient(135deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.6) 100%)",
        border_radius="12px",
        border=f"3px solid {colors[day_number]}",
        box_shadow=f"0 0 20px {colors[day_number]}",
        width="100%",
        margin_bottom=Size.BIG.value,
        class_name="celebration-banner"
    )

def progress_bar(current_day: int) -> rx.Component:
    """Barra de progreso del calendario"""
    progress = (current_day / 25) * 100
    
    return rx.box(
        rx.vstack(
            rx.text(
                f"Progreso del viaje: {current_day}/25 días",
                font_size=Size.MEDIUM.value,
                color="#FFFFFF",
                text_align="center"
            ),
            rx.box(
                rx.box(
                    width=f"{progress}%",
                    height="100%",
                    background="linear-gradient(90deg, #DC143C 0%, #FFD700 100%)",
                    border_radius="10px",
                    transition="width 0.5s ease-in-out",
                    box_shadow="0 0 10px rgba(255,215,0,0.5)"
                ),
                width="100%",
                height="20px",
                background="rgba(0,0,0,0.3)",
                border_radius="10px",
                border="2px solid #FFD700",
                overflow="hidden"
            ),
            align="center",
            spacing="2"
        ),
        width="100%",
        padding=Size.MEDIUM.value,
        background="rgba(0,0,0,0.5)",
        border_radius="8px",
        border="1px solid #FFD700",
        margin_bottom=Size.BIG.value
    )

def countdown_enhanced() -> rx.Component:
    """Countdown mejorado con efectos visuales"""
    return rx.box(
        rx.vstack(
            rx.text(
                "⏰ Tiempo restante para Shanghai",
                font_size=Size.MEDIUM.value,
                color="#FFD700",
                font_weight="bold",
                text_align="center"
            ),
            rx.hstack(
                rx.box(
                    rx.text(
                        id="countdown-days",
                        data_countdown="days",
                        font_size=rx.breakpoints(
                            initial="1.5em",
                            xs="1.8em",
                            sm="2em",
                            md="2.2em",
                            lg="2.5em",
                            xl="2.5em"
                        ),
                        font_weight="bold",
                        color="#DC143C",
                        class_name="countdown-number"
                    ),
                    rx.text(
                        "DÍAS",
                        font_size=Size.SMALL.value,
                        color="#FFFFFF",
                        class_name="countdown-label"
                    ),
                    align="center",
                    spacing="1",
                    padding=Size.MEDIUM.value,
                    background="rgba(0,0,0,0.7)",
                    border_radius="8px",
                    border="2px solid #DC143C",
                    class_name="countdown-box"
                ),
                rx.box(
                    rx.text(
                        id="countdown-hours",
                        data_countdown="hours",
                        font_size=rx.breakpoints(
                            initial="1.5em",
                            xs="1.8em",
                            sm="2em",
                            md="2.2em",
                            lg="2.5em",
                            xl="2.5em"
                        ),
                        font_weight="bold",
                        color="#DC143C",
                        class_name="countdown-number"
                    ),
                    rx.text(
                        "HORAS",
                        font_size=Size.SMALL.value,
                        color="#FFFFFF",
                        class_name="countdown-label"
                    ),
                    align="center",
                    spacing="1",
                    padding=Size.MEDIUM.value,
                    background="rgba(0,0,0,0.7)",
                    border_radius="8px",
                    border="2px solid #DC143C",
                    class_name="countdown-box"
                ),
                rx.box(
                    rx.text(
                        id="countdown-minutes",
                        data_countdown="minutes",
                        font_size=rx.breakpoints(
                            initial="1.5em",
                            xs="1.8em",
                            sm="2em",
                            md="2.2em",
                            lg="2.5em",
                            xl="2.5em"
                        ),
                        font_weight="bold",
                        color="#DC143C",
                        class_name="countdown-number"
                    ),
                    rx.text(
                        "MIN",
                        font_size=Size.SMALL.value,
                        color="#FFFFFF",
                        class_name="countdown-label"
                    ),
                    align="center",
                    spacing="1",
                    padding=Size.MEDIUM.value,
                    background="rgba(0,0,0,0.7)",
                    border_radius="8px",
                    border="2px solid #DC143C",
                    class_name="countdown-box"
                ),
                rx.box(
                    rx.text(
                        id="countdown-seconds",
                        data_countdown="seconds",
                        font_size=rx.breakpoints(
                            initial="1.5em",
                            xs="1.8em",
                            sm="2em",
                            md="2.2em",
                            lg="2.5em",
                            xl="2.5em"
                        ),
                        font_weight="bold",
                        color="#DC143C",
                        class_name="countdown-number"
                    ),
                    rx.text(
                        "SEG",
                        font_size=Size.SMALL.value,
                        color="#FFFFFF",
                        class_name="countdown-label"
                    ),
                    align="center",
                    spacing="1",
                    padding=Size.MEDIUM.value,
                    background="rgba(0,0,0,0.7)",
                    border_radius="8px",
                    border="2px solid #DC143C",
                    class_name="countdown-box"
                ),
                spacing="2",
                justify="center",
                flex_wrap="wrap",
                class_name="countdown-hstack"
            ),
            align="center",
            spacing="3"
        ),
        width="100%",
        padding=Size.BIG.value,
        background="linear-gradient(135deg, rgba(0,0,0,0.8) 0%, rgba(220,20,60,0.3) 100%)",
        border_radius="12px",
        border="2px solid #FFD700",
        box_shadow="0 0 20px rgba(255,215,0,0.3)",
        class_name="countdown-container"
    )
