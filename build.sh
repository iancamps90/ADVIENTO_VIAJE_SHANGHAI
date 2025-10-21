#!/bin/bash

# Script de build para Vercel
echo "🚀 Iniciando build para Vercel..."

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

# Exportar la aplicación Reflex
echo "🔨 Exportando aplicación Reflex..."
python -m reflex export --frontend-only

# Copiar assets a la carpeta de salida
echo "📁 Copiando assets..."
cp -r assets/* web/_static/ 2>/dev/null || true
cp -r public/* web/_static/ 2>/dev/null || true

echo "✅ Build completado!"
