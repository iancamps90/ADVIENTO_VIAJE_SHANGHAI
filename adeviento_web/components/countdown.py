import reflex as rx
from datetime import datetime, timezone
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import TextColor, Color


class CountdownState(rx.State):
    """Estado para el countdown timer"""
    
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
    is_trip_day: bool = False
    
    def update_countdown(self):
        """Actualiza el countdown cada segundo"""
        # Fecha objetivo: 25 de diciembre de 2025
        target_date = datetime(2025, 12, 25, 0, 0, 0, tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        
        # Calcular la diferencia
        time_diff = target_date - now
        
        if time_diff.total_seconds() <= 0:
            # ¡Ya es el día del viaje!
            self.days = 0
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.is_trip_day = True
        else:
            # Calcular días, horas, minutos y segundos
            total_seconds = int(time_diff.total_seconds())
            self.days = total_seconds // 86400
            self.hours = (total_seconds % 86400) // 3600
            self.minutes = (total_seconds % 3600) // 60
            self.seconds = total_seconds % 60
            self.is_trip_day = False


def countdown_timer() -> rx.Component:
    """Componente de countdown timer para el viaje a Shanghai"""
    
    return rx.box(
        rx.vstack(
            # Título del countdown
            rx.heading(
                "Cuenta atrás para Shanghai",
                size={
    "initial": "6",
    "xs": "7",
    "sm": "8",
    "md": "9",
    "lg": "9",
    "xl": "9"
},
                color="white",
                class_name="chinese-text",
                text_align="center",
                text_shadow="3px 3px 6px rgba(0,0,0,0.8)"
            ),
            
            # Mensaje dinámico
            rx.cond(
                CountdownState.is_trip_day,
                rx.vstack(
                    rx.text(
                        "¡HOY ES EL DÍA!",
                        font_size="2em",
                        font_weight="bold",
                        color=TextColor.ACCENT.value,
                        class_name="red-pulse"
                    ),
                    rx.text(
                        "¡Nos vamos a Shanghai!",
                        font_size="1.2em",
                        color=TextColor.TERTIARY.value
                    ),
                    align="center",
                    spacing="2"
                ),
                rx.vstack(
                    rx.text(
                        "Días hasta el viaje más épico del año",
                        font_size=Size.MEDIUM.value,
                        color="white",
                        text_align="center",
                        text_shadow="2px 2px 4px rgba(0,0,0,0.8)"
                    ),
                    rx.text(
                        "Shanghai nos espera",
                        font_size=Size.MEDIUM.value,
                        color="#FFD700",
                        text_align="center",
                        text_shadow="2px 2px 4px rgba(0,0,0,0.8)"
                    ),
                    align="center",
                    spacing="2"
                )
            ),
            
            # Display del countdown
            rx.cond(
                CountdownState.is_trip_day,
                # Si es el día del viaje
                rx.box(
                    rx.text(
                        "¡FELIZ NAVIDAD EN SHANGHAI!",
                        font_size="1.5em",
                        font_weight="bold",
                        color=TextColor.SECONDARY.value,
                        text_align="center",
                        class_name="golden-glow"
                    ),
                    padding=Size.BIG.value,
                    background=f"linear-gradient(135deg, {Color.ACCENT.value}, {Color.SECONDARY.value})",
                    border_radius="12px",
                    border=f"3px solid {Color.SECONDARY.value}",
                    width="100%"
                ),
                # Countdown normal
                rx.hstack(
                    # Días
                    rx.vstack(
                        rx.box(
                            rx.text(
                                CountdownState.days,
                                font_size={
    "initial": "1.5em",
    "xs": "1.8em",
    "sm": "2em",
    "md": "2.2em",
    "lg": "2.5em",
    "xl": "2.5em"
},
                                font_weight="bold",
                                color=TextColor.PRIMARY.value,
                                class_name="golden-glow countdown-number",
                                data_countdown="days"
                            ),
                            padding={
    "initial": "0.8em",
    "xs": "1em",
    "sm": "1.2em",
    "md": "1.5em",
    "lg": "2em",
    "xl": "2em"
},
                            background=f"linear-gradient(135deg, {Color.ACCENT.value}, {Color.QUATERNARY.value})",
                            border_radius="8px",
                            border=f"2px solid {Color.SECONDARY.value}",
                            min_width={
    "initial": "60px",
    "xs": "65px",
    "sm": "70px",
    "md": "75px",
    "lg": "80px",
    "xl": "80px"
},
                            text_align="center",
                            class_name="countdown-box"
                        ),
                        rx.text(
                            "DÍAS",
                            font_size={
    "initial": "0.6em",
    "xs": "0.7em",
    "sm": "0.8em",
    "md": "0.9em",
    "lg": "1em",
    "xl": "1em"
},
                            font_weight="bold",
                            color=TextColor.SECONDARY.value,
                            class_name="countdown-label"
                        ),
                        align="center",
                        spacing="1"
                    ),
                    
                    # Horas
                    rx.vstack(
                        rx.box(
                            rx.text(
                                CountdownState.hours,
                                font_size={
    "initial": "1.5em",
    "xs": "1.8em",
    "sm": "2em",
    "md": "2.2em",
    "lg": "2.5em",
    "xl": "2.5em"
},
                                font_weight="bold",
                                color=TextColor.PRIMARY.value,
                                class_name="golden-glow countdown-number",
                                data_countdown="hours"
                            ),
                            padding={
    "initial": "0.8em",
    "xs": "1em",
    "sm": "1.2em",
    "md": "1.5em",
    "lg": "2em",
    "xl": "2em"
},
                            background=f"linear-gradient(135deg, {Color.ACCENT.value}, {Color.QUATERNARY.value})",
                            border_radius="8px",
                            border=f"2px solid {Color.SECONDARY.value}",
                            min_width={
    "initial": "60px",
    "xs": "65px",
    "sm": "70px",
    "md": "75px",
    "lg": "80px",
    "xl": "80px"
},
                            text_align="center",
                            class_name="countdown-box"
                        ),
                        rx.text(
                            "HORAS",
                            font_size={
    "initial": "0.6em",
    "xs": "0.7em",
    "sm": "0.8em",
    "md": "0.9em",
    "lg": "1em",
    "xl": "1em"
},
                            font_weight="bold",
                            color=TextColor.SECONDARY.value,
                            class_name="countdown-label"
                        ),
                        align="center",
                        spacing="1"
                    ),
                    
                    # Minutos
                    rx.vstack(
                        rx.box(
                            rx.text(
                                CountdownState.minutes,
                                font_size={
    "initial": "1.5em",
    "xs": "1.8em",
    "sm": "2em",
    "md": "2.2em",
    "lg": "2.5em",
    "xl": "2.5em"
},
                                font_weight="bold",
                                color=TextColor.PRIMARY.value,
                                class_name="golden-glow countdown-number",
                                data_countdown="minutes"
                            ),
                            padding={
    "initial": "0.8em",
    "xs": "1em",
    "sm": "1.2em",
    "md": "1.5em",
    "lg": "2em",
    "xl": "2em"
},
                            background=f"linear-gradient(135deg, {Color.ACCENT.value}, {Color.QUATERNARY.value})",
                            border_radius="8px",
                            border=f"2px solid {Color.SECONDARY.value}",
                            min_width={
    "initial": "60px",
    "xs": "65px",
    "sm": "70px",
    "md": "75px",
    "lg": "80px",
    "xl": "80px"
},
                            text_align="center",
                            class_name="countdown-box"
                        ),
                        rx.text(
                            "MIN",
                            font_size={
    "initial": "0.6em",
    "xs": "0.7em",
    "sm": "0.8em",
    "md": "0.9em",
    "lg": "1em",
    "xl": "1em"
},
                            font_weight="bold",
                            color=TextColor.SECONDARY.value,
                            class_name="countdown-label"
                        ),
                        align="center",
                        spacing="1"
                    ),
                    
                    # Segundos
                    rx.vstack(
                        rx.box(
                            rx.text(
                                CountdownState.seconds,
                                font_size={
    "initial": "1.5em",
    "xs": "1.8em",
    "sm": "2em",
    "md": "2.2em",
    "lg": "2.5em",
    "xl": "2.5em"
},
                                font_weight="bold",
                                color=TextColor.PRIMARY.value,
                                class_name="golden-glow countdown-number",
                                data_countdown="seconds"
                            ),
                            padding={
    "initial": "0.8em",
    "xs": "1em",
    "sm": "1.2em",
    "md": "1.5em",
    "lg": "2em",
    "xl": "2em"
},
                            background=f"linear-gradient(135deg, {Color.ACCENT.value}, {Color.QUATERNARY.value})",
                            border_radius="8px",
                            border=f"2px solid {Color.SECONDARY.value}",
                            min_width={
    "initial": "60px",
    "xs": "65px",
    "sm": "70px",
    "md": "75px",
    "lg": "80px",
    "xl": "80px"
},
                            text_align="center",
                            class_name="countdown-box"
                        ),
                        rx.text(
                            "SEG",
                            font_size={
    "initial": "0.6em",
    "xs": "0.7em",
    "sm": "0.8em",
    "md": "0.9em",
    "lg": "1em",
    "xl": "1em"
},
                            font_weight="bold",
                            color=TextColor.SECONDARY.value,
                            class_name="countdown-label"
                        ),
                        align="center",
                        spacing="1"
                    ),
                    
                    spacing={
    "initial": "1",
    "xs": "2",
    "sm": "2",
    "md": "3",
    "lg": "3",
    "xl": "3"
},
                    justify="center",
                    flex_wrap="wrap",
                    width="100%",
                    class_name="countdown-hstack"
                )
            ),
            
            # Información adicional
            rx.cond(
                CountdownState.is_trip_day,
                rx.text(
                    "¡Que empiece la aventura más épica del año!",
                    font_size=Size.MEDIUM.value,
                    color=TextColor.TERTIARY.value,
                    text_align="center",
                    margin_top=Size.BIG.value
                ),
                rx.text(
                    "Cada segundo nos acerca a la aventura más épica del año",
                    font_size=Size.MEDIUM.value,
                    color="white",
                    text_align="center",
                    margin_top=Size.BIG.value,
                    text_shadow="2px 2px 4px rgba(0,0,0,0.8)"
                )
            ),
            
            align="center",
            spacing="4",
            width="100%"
        ),
        
        # Estilos del contenedor
        padding={
    "initial": "1.5em",
    "xs": "2em",
    "sm": "2.5em",
    "md": "3em",
    "lg": "4em",
    "xl": "4em"
},
        background=f"linear-gradient(135deg, {Color.ACCENT.value}, {Color.SECONDARY.value}, {Color.QUATERNARY.value})",
        border_radius="16px",
        border=f"3px solid {Color.SECONDARY.value}",
        box_shadow=f"0 8px 16px {Color.QUATERNARY.value}",
        class_name="chinese-card fade-in countdown-container",
        width="100%"
    )


def countdown_script() -> rx.Component:
    """Script para actualizar el countdown cada segundo"""
    return rx.script(src="/js/countdown.js")
