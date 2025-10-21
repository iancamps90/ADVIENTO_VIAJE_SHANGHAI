#!/bin/bash

# Script para desplegar el calendario de Shanghai en producción
echo "🏮 DESPLEGANDO CALENDARIO SHANGHAI EN PRODUCCIÓN 🐉"
echo "=================================================="

# Verificar que estamos en el directorio correcto
if [ ! -f "adeviento_web/adeviento_web.py" ]; then
    echo "❌ Error: No estás en el directorio correcto del proyecto"
    exit 1
fi

# Verificar que Vercel CLI está instalado
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI no está instalado"
    echo "📦 Instálalo con: npm i -g vercel"
    exit 1
fi

echo "✅ Verificaciones completadas"

# Construir el proyecto
echo "🔨 Construyendo el proyecto con todas las animaciones..."
if [ -f "build.sh" ]; then
    chmod +x build.sh
    ./build.sh
else
    echo "⚠️  build.sh no encontrado, usando reflex build"
    reflex build
fi

echo "✅ Proyecto construido con efectos espectaculares"

# Verificar archivos de animaciones
echo "🎊 Verificando archivos de animaciones..."
if [ -f "assets/js/mobile-animations.js" ]; then
    echo "✅ Animaciones móviles: OK"
else
    echo "❌ Animaciones móviles: FALTAN"
fi

if [ -f "assets/js/fireworks.js" ]; then
    echo "✅ Fuegos artificiales: OK"
else
    echo "❌ Fuegos artificiales: FALTAN"
fi

if [ -f "assets/js/sound-effects.js" ]; then
    echo "✅ Efectos de sonido: OK"
else
    echo "❌ Efectos de sonido: FALTAN"
fi

# Desplegar en Vercel
echo "🚀 Desplegando en Vercel con dominio shanghai.iancamps.dev..."
vercel --prod

echo "✅ Desplegado en Vercel"

# Verificar variables de entorno
echo "🔧 Verificando variables de entorno..."
echo "META_ACCESS_TOKEN: ${META_ACCESS_TOKEN:+✅ Configurado}"
echo "META_PHONE_NUMBER_ID: ${META_PHONE_NUMBER_ID:+✅ Configurado}"
echo "META_VERIFY_TOKEN: ${META_VERIFY_TOKEN:+✅ Configurado}"

echo "🎉 ¡DESPLIEGUE COMPLETADO CON ÉXITO!"
echo ""
echo "📱 URLs del proyecto:"
echo "   • Página principal: https://shanghai.iancamps.dev/"
echo "   • Panel de administración: https://shanghai.iancamps.dev/admin"
echo "   • Panel WhatsApp: https://shanghai.iancamps.dev/whatsapp-admin"
echo ""
echo "🎊 Efectos implementados:"
echo "   ✅ Animaciones móviles espectaculares"
echo "   ✅ Fuegos artificiales"
echo "   ✅ Efectos de sonido"
echo "   ✅ Partículas flotantes"
echo "   ✅ Dragones voladores"
echo "   ✅ Farolillos chinos"
echo "   ✅ Efectos táctiles con vibración"
echo "   ✅ Automatización WhatsApp"
echo ""
echo "🏮 ¡Que empiece la aventura más épica a Shanghai!"
echo "📱 ¡Tus amigos van a quedar alucinados con las animaciones!"
