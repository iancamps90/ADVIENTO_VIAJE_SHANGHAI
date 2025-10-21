# 🏮 Calendario de Adviento Shanghai 2025 🐉

¡Un calendario de adviento espectacular para preparar el viaje más épico a Shanghai! Con animaciones móviles flipantes y automatización de mensajes WhatsApp.

## ✨ Características Principales

### 📱 Animaciones Móviles Espectaculares
- **Partículas flotantes** con colores chinos y navideños
- **Efectos de confeti** en días especiales
- **Dragones voladores** 🐉 que cruzan la pantalla
- **Farolillos chinos flotantes** 🏮
- **Efectos táctiles** con vibración del dispositivo
- **Ondas expansivas** al tocar elementos
- **Estrellas brillantes** ⭐ que aparecen aleatoriamente
- **Efectos de shake y zoom** para interacciones

### 🤖 Automatización de Mensajes WhatsApp
- **Envío automático** de mensajes diarios
- **Respuestas automáticas** a comandos
- **Panel de administración** completo
- **Webhook** para recibir mensajes
- **Integración con Meta API**

### 🎨 Diseño Temático
- **Tema chino-navideño** con colores dorados y rojos
- **Efectos de nieve** mejorados
- **Caracteres chinos flotantes** (龙, 福, 喜, 财)
- **Responsive design** optimizado para móvil
- **Animaciones suaves** y fluidas

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/shanghai-advent-calendar.git
cd shanghai-advent-calendar
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar números de amigos
Edita `adeviento_web/config/whatsapp_config.py`:
```python
FRIENDS_PHONE_NUMBERS = [
    "34612345678",  # Amigo 1 - Reemplaza con el número real
    "34612345679",  # Amigo 2 - Reemplaza con el número real  
    "34612345680",  # Amigo 3 - Reemplaza con el número real
    "34612345681",  # Amigo 4 - Reemplaza con el número real
]
```

### 4. Configurar Meta WhatsApp API

#### Crear aplicación en Meta for Developers:
1. Ve a https://developers.facebook.com/
2. Crea una nueva aplicación
3. Añade el producto "WhatsApp Business API"
4. Obtén tu Access Token y Phone Number ID

#### Configurar webhook:
- **Webhook URL**: `https://shanghai.iancamps.dev/api/webhook`
- **Verify Token**: `shanghai_advent_2025_verify`
- **Webhook Fields**: `messages`, `message_deliveries`, `message_reads`

### 5. Desplegar en Vercel

#### Configurar variables de entorno en Vercel:
```bash
META_ACCESS_TOKEN=tu_access_token_de_meta
META_PHONE_NUMBER_ID=tu_phone_number_id
META_VERIFY_TOKEN=shanghai_advent_2025_verify
```

#### Configurar dominio:
1. En Vercel Dashboard > Settings > Domains
2. Añade: `shanghai.iancamps.dev`
3. Configura los DNS records según las instrucciones

## 📱 Uso del Calendario

### Para los Amigos:
1. **Visita**: https://shanghai.iancamps.dev/
2. **Toca los días** para ver las sorpresas
3. **Disfruta las animaciones** espectaculares
4. **Recibe mensajes** automáticos cada día

### Para el Administrador:
1. **Panel principal**: https://shanghai.iancamps.dev/admin
2. **Panel WhatsApp**: https://shanghai.iancamps.dev/whatsapp-admin
3. **Enviar mensajes** manualmente
4. **Monitorear** el estado del servicio

## 🎯 Días Especiales con Efectos Únicos

- **Día 1**: Explosión de bienvenida con confeti y dragón
- **Día 15**: Mitad del camino - múltiples explosiones
- **Día 24**: Víspera del viaje - efectos épicos
- **Día 25**: ¡Llegamos a Shanghai! - celebración final

## 🤖 Comandos de WhatsApp

Los amigos pueden escribir estos comandos al bot:
- `ayuda` - Muestra comandos disponibles
- `día` - Muestra el día actual
- `progreso` - Muestra el progreso del viaje
- `shanghai` - Información sobre el viaje

## 🔧 API Endpoints

### Webhook de WhatsApp
```
GET/POST https://shanghai.iancamps.dev/api/webhook
```

### Mensaje diario
```
GET https://shanghai.iancamps.dev/api/daily-message
POST https://shanghai.iancamps.dev/api/daily-message
Body: {"day": 1}
```

## 📊 Automatización

### GitHub Actions
El proyecto incluye un workflow que envía mensajes automáticamente:
- **Horario**: Todos los días a las 9:00 AM (Madrid)
- **Solo en diciembre 2025**
- **Ejecución manual** disponible

### Cron Job Alternativo
```bash
# Ejecutar todos los días a las 9:00 AM
0 9 * * * curl -X GET "https://shanghai.iancamps.dev/api/daily-message"
```

## 🎨 Personalización

### Añadir nuevos efectos:
1. Edita `assets/js/mobile-animations.js`
2. Añade tu función de animación
3. Llámala desde `window.ShanghaiAnimations`

### Modificar contenido:
1. Edita `adeviento_web/views/calendar.py`
2. Modifica el array `_shanghai_days`
3. Añade nuevos días o cambia el contenido

### Cambiar colores:
1. Edita `assets/css/main.css`
2. Modifica las variables CSS en `:root`
3. Ajusta los colores chinos y navideños

## 🚀 Optimizaciones Implementadas

- ✅ **Animaciones móviles** espectaculares
- ✅ **Efectos táctiles** con vibración
- ✅ **Partículas flotantes** y confeti
- ✅ **Dragones voladores** y farolillos
- ✅ **Automatización WhatsApp** completa
- ✅ **Webhook** para respuestas automáticas
- ✅ **Panel de administración** intuitivo
- ✅ **Optimización móvil** avanzada
- ✅ **SEO** y meta tags
- ✅ **Seguridad** y headers
- ✅ **Responsive design** perfecto

## 📱 Compatibilidad

- ✅ **iOS Safari** - Optimizado
- ✅ **Android Chrome** - Optimizado
- ✅ **Desktop** - Funciona perfectamente
- ✅ **Tablets** - Responsive design

## 🎊 ¡Disfruta del Viaje!

Este calendario está diseñado para crear la máxima emoción y expectación para el viaje a Shanghai. ¡Cada día una nueva sorpresa, cada animación una nueva experiencia!

**¡Que empiece la aventura más épica del año!** 🏮✈️🇨🇳

---

*Desarrollado con ❤️ para el viaje más increíble a Shanghai 2025*
