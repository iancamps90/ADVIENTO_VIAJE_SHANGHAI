import reflex as rx
from adeviento_web.styles.styles import Size
from adeviento_web.styles.colors import Color

def photo_carousel(photos: list[str], interval: int = 5000) -> rx.Component:
    """
    Carrusel de fotos que cambia automáticamente cada X milisegundos
    """
    return rx.box(
        rx.script(f"""
        let currentPhoto = 0;
        const photos = {photos};
        const interval = {interval};
        
        function changePhoto() {{
            const carousel = document.getElementById('photo-carousel');
            if (carousel && photos.length > 0) {{
                currentPhoto = (currentPhoto + 1) % photos.length;
                carousel.src = photos[currentPhoto];
            }}
        }}
        
        // Cambiar foto cada X segundos
        setInterval(changePhoto, interval);
        
        // Cambiar foto al hacer click
        document.addEventListener('DOMContentLoaded', function() {{
            const carousel = document.getElementById('photo-carousel');
            if (carousel) {{
                carousel.addEventListener('click', changePhoto);
            }}
        }});
        """),
        rx.image(
            id="photo-carousel",
            src=photos[0] if photos else "",
            alt="Carrusel de fotos",
            width="100%",
            border_radius="12px",
            cursor="pointer",
            transition="all 0.5s ease-in-out"
        ),
        class_name="photo-carousel-container"
    )
