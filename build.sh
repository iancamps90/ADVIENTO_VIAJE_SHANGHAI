#!/bin/bash

# Script de build para Vercel
echo "🚀 Iniciando build para Vercel..."

# Instalar dependencias
echo "📦 Instalando dependencias..."
python3 -m pip install -r requirements.txt

# Exportar la aplicación Reflex
echo "🔨 Exportando aplicación Reflex..."
python3 -m reflex export --frontend-only

# Crear directorio de salida si no existe
mkdir -p web/_static

# Copiar assets a la carpeta de salida
echo "📁 Copiando assets..."
cp -r assets/* web/_static/ 2>/dev/null || true
cp -r public/* web/_static/ 2>/dev/null || true

echo "✅ Build completado!"
