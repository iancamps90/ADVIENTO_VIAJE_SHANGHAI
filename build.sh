#!/bin/bash

# Script de build para Vercel
echo "🚀 Iniciando build para Vercel..."

# Instalar dependencias
pip install -r requirements.txt

# Exportar la aplicación Reflex
reflex export --frontend-only

echo "✅ Build completado!"
