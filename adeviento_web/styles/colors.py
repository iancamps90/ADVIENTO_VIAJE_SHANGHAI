from enum import Enum


class Color(Enum):
    # Paleta Shanghai - Rojo y Dorado chino
    ACCENT = "#DC143C"  # Rojo chino intenso
    PRIMARY = "#1a1a1a"  # Negro profundo
    SECONDARY = "#FFD700"  # Dorado chino
    TERTIARY = "#B8860B"  # Dorado oscuro
    QUATERNARY = "#8B0000"  # Rojo oscuro
    BACKGROUND = "#FFF8DC"  # Crema suave


class TextColor(Enum):
    ACCENT = "#DC143C !important"  # Rojo chino
    PRIMARY = "#FFFFFF"
    SECONDARY = "#1a1a1a"  # Negro
    TERTIARY = "#FFD700"  # Dorado
    QUATERNARY = "#8B0000"  # Rojo oscuro
