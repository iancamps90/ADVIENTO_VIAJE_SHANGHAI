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
            max_width=rx.breakpoints(
                initial="300px",
                xs="350px", 
                sm="400px",
                md="450px",
                lg="500px",
                xl="500px"
            ),
            border_radius="8px",
            cursor="pointer",
            transition="all 0.5s ease-in-out",
            _hover={
                "transform": "scale(1.02)",
                "box_shadow": f"0 8px 16px {Color.QUATERNARY.value}"
            }
        ),
        width="100%",
        text_align="center"
    )
