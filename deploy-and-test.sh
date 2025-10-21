#!/bin/bash

# Script para desplegar y probar el calendario de Shanghai
echo "🏮 DESPLEGANDO CALENDARIO DE ADVIENTO SHANGHAI 🐉"
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
echo "🔨 Construyendo el proyecto..."
if [ -f "build.sh" ]; then
    chmod +x build.sh
    ./build.sh
else
    echo "⚠️  build.sh no encontrado, usando reflex build"
    reflex build
fi

echo "✅ Proyecto construido"

# Desplegar en Vercel
echo "🚀 Desplegando en Vercel..."
vercel --prod

echo "✅ Desplegado en Vercel"

# Verificar variables de entorno
echo "🔧 Verificando variables de entorno..."
echo "META_ACCESS_TOKEN: ${META_ACCESS_TOKEN:+✅ Configurado}"
echo "META_PHONE_NUMBER_ID: ${META_PHONE_NUMBER_ID:+✅ Configurado}"
echo "META_VERIFY_TOKEN: ${META_VERIFY_TOKEN:+✅ Configurado}"

# Probar la API
echo "🧪 Probando la API..."
python test-api.py

echo "🎉 ¡Despliegue completado!"
echo ""
echo "📱 URLs importantes:"
echo "   • Página principal: https://shanghai.iancamps.dev/"
echo "   • Panel WhatsApp: https://shanghai.iancamps.dev/whatsapp-admin"
echo "   • Webhook: https://shanghai.iancamps.dev/api/webhook"
echo ""
echo "🔧 Para probar WhatsApp:"
echo "   1. Ve a /whatsapp-admin"
echo "   2. Haz clic en 'Mensaje de Prueba'"
echo "   3. Revisa tu WhatsApp (34615784663)"
echo ""
echo "🏮 ¡Que empiece la aventura a Shanghai!"
