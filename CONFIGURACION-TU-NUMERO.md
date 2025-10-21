# 📱 Configuración para tu número: 34615784663

## ✅ Ya configurado:
- ✅ Tu número añadido a la lista de amigos
- ✅ Variables de entorno configuradas en Vercel
- ✅ Scripts de prueba creados

## 🚀 Pasos para probar:

### 1. Desplegar el proyecto
```bash
# Ejecutar el script de despliegue
chmod +x deploy-and-test.sh
./deploy-and-test.sh
```

### 2. Probar desde el panel de administración
1. Ve a: https://shanghai.iancamps.dev/whatsapp-admin
2. Haz clic en "Mensaje de Prueba"
3. Revisa tu WhatsApp (34615784663)

### 3. Probar desde línea de comandos
```bash
# Probar localmente
python test-whatsapp.py

# Probar API remota
python test-api.py
```

### 4. Probar webhook de Meta
1. Ve a tu aplicación en Meta for Developers
2. Configura el webhook:
   - **URL**: `https://shanghai.iancamps.dev/api/webhook`
   - **Verify Token**: `shanghai_advent_2025_verify`
3. Haz clic en "Verify and Save"

## 🧪 Mensaje de prueba que recibirás:

```
🧪 Mensaje de Prueba - Calendario Shanghai 🏮

¡Hola! Este es un mensaje de prueba para verificar que la configuración de WhatsApp funciona correctamente.

Si recibes este mensaje, ¡todo está listo para el calendario de adviento! ✨

Características del calendario:
• 🎊 Animaciones móviles espectaculares
• 🐉 Dragones voladores y farolillos chinos
• 📱 Efectos táctiles con vibración
• 🎯 25 días de sorpresas para Shanghai
• 🤖 Mensajes automáticos diarios

¡Que empiece la aventura más épica del año! 🚀

#ShanghaiAdvent2025 #ViajeShanghai2025
```

## 🔧 Comandos que puedes probar:

Envía estos mensajes a tu bot de WhatsApp:
- `ayuda` - Muestra comandos disponibles
- `día` - Muestra el día actual
- `progreso` - Muestra el progreso del viaje
- `shanghai` - Información sobre el viaje

## 📊 URLs de prueba:

- **Panel principal**: https://shanghai.iancamps.dev/
- **Panel WhatsApp**: https://shanghai.iancamps.dev/whatsapp-admin
- **Webhook**: https://shanghai.iancamps.dev/api/webhook
- **Mensaje diario**: https://shanghai.iancamps.dev/api/daily-message

## 🎯 Próximos pasos:

1. **Probar el envío** con tu número
2. **Añadir números de tus amigos** en `whatsapp_config.py`
3. **Configurar envío automático** diario
4. **Personalizar mensajes** si quieres

## 🚨 Si algo no funciona:

1. **Verifica variables de entorno** en Vercel
2. **Revisa logs** en Vercel Dashboard
3. **Comprueba configuración** en Meta for Developers
4. **Ejecuta scripts de prueba** para diagnosticar

¡Tu número ya está configurado y listo para recibir mensajes! 🎉
