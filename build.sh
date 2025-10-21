#!/bin/bash

# Script de build para el Calendario de Adviento Shanghai
echo "🏮 Construyendo Calendario de Adviento Shanghai 2025 🐉"

# Verificar que estamos en el directorio correcto
if [ ! -f "adeviento_web/adeviento_web.py" ]; then
    echo "❌ Error: No estás en el directorio correcto del proyecto"
    exit 1
fi

# Crear directorio público si no existe
mkdir -p public

# Copiar archivos estáticos
echo "📁 Copiando archivos estáticos..."
cp -r assets public/ 2>/dev/null || echo "⚠️  No se encontró directorio assets"

# Crear archivo index.html básico
echo "📄 Creando index.html..."
cat > public/index.html << 'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendario de Adviento Shanghai 2025</title>
    <meta name="description" content="¡Calendario de adviento personalizado para nuestro viaje a Shanghai! Del 1 al 25 de diciembre de 2025, cada día una nueva sorpresa para calentar el viaje.">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        h1 {
            font-size: 3em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .subtitle {
            font-size: 1.2em;
            margin-bottom: 40px;
            opacity: 0.9;
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }
        .feature {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        .feature h3 {
            margin-top: 0;
            color: #FFD700;
        }
        .loading {
            font-size: 1.1em;
            margin-top: 30px;
        }
        .spinner {
            border: 4px solid rgba(255,255,255,0.3);
            border-top: 4px solid #FFD700;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏮 Calendario de Adviento Shanghai 2025 🐉</h1>
        <p class="subtitle">¡25 días. 25 sorpresas para el viaje más épico!</p>
        
        <div class="features">
            <div class="feature">
                <h3>🎥 Videos Reales</h3>
                <p>Videos de YouTube integrados para cada día</p>
            </div>
            <div class="feature">
                <h3>🎊 Animaciones Espectaculares</h3>
                <p>Efectos móviles, fuegos artificiales y dragones</p>
            </div>
            <div class="feature">
                <h3>📱 Contenido Interactivo</h3>
                <p>Retos, tips y contenido detallado</p>
            </div>
            <div class="feature">
                <h3>🤖 WhatsApp Automático</h3>
                <p>Mensajes diarios automáticos a tus amigos</p>
            </div>
        </div>
        
        <div class="loading">
            <div class="spinner"></div>
            <p>🚀 Cargando la experiencia más épica...</p>
            <p><small>Si no se carga automáticamente, recarga la página</small></p>
        </div>
    </div>
    
    <script>
        // Redirigir después de 3 segundos
        setTimeout(() => {
            window.location.reload();
        }, 3000);
    </script>
</body>
</html>
EOF

echo "✅ Build completado exitosamente"
echo "📁 Archivos generados en: public/"
echo "🎊 ¡Calendario listo para desplegar!"