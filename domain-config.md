# Configuración del Dominio shanghai.iancamps.dev

## 🚀 Pasos para configurar el dominio en Vercel

### 1. Configurar el dominio en Vercel
```bash
# En el dashboard de Vercel:
# 1. Ve a tu proyecto
# 2. Settings > Domains
# 3. Añade: shanghai.iancamps.dev
# 4. Configura los DNS records según las instrucciones
```

### 2. Variables de entorno necesarias
```bash
# En Vercel Dashboard > Settings > Environment Variables:
META_ACCESS_TOKEN=tu_access_token_de_meta
META_PHONE_NUMBER_ID=tu_phone_number_id
META_VERIFY_TOKEN=shanghai_advent_2025_verify
```

### 3. Configuración de DNS
```
# Añadir estos records en tu proveedor de DNS:
Type: CNAME
Name: shanghai
Value: cname.vercel-dns.com

# O si usas A record:
Type: A
Name: shanghai
Value: 76.76.19.61
```

### 4. Configuración de Meta WhatsApp API

#### Crear aplicación en Meta for Developers:
1. Ve a https://developers.facebook.com/
2. Crea una nueva aplicación
3. Añade el producto "WhatsApp Business API"
4. Obtén tu Access Token y Phone Number ID

#### Configurar webhook:
- **Webhook URL**: `https://shanghai.iancamps.dev/api/webhook`
- **Verify Token**: `shanghai_advent_2025_verify`
- **Webhook Fields**: `messages`, `message_deliveries`, `message_reads`

### 5. Configuración de cron job (opcional)
Para envío automático de mensajes diarios, puedes usar:
- **Vercel Cron Jobs** (si tienes plan Pro)
- **GitHub Actions** con schedule
- **Servicio externo** como cron-job.org

#### Ejemplo de GitHub Action:
```yaml
name: Daily Shanghai Message
on:
  schedule:
    - cron: '0 9 * * *'  # 9:00 AM todos los días
  workflow_dispatch:

jobs:
  send-message:
    runs-on: ubuntu-latest
    steps:
      - name: Send daily message
        run: |
          curl -X GET "https://shanghai.iancamps.dev/api/daily-message"
```

### 6. URLs importantes del proyecto
- **Página principal**: https://shanghai.iancamps.dev/
- **Panel de administración**: https://shanghai.iancamps.dev/admin
- **Panel de WhatsApp**: https://shanghai.iancamps.dev/whatsapp-admin
- **Webhook**: https://shanghai.iancamps.dev/api/webhook
- **Mensaje diario**: https://shanghai.iancamps.dev/api/daily-message

### 7. Testing
```bash
# Probar webhook
curl -X GET "https://shanghai.iancamps.dev/api/webhook?hub.mode=subscribe&hub.verify_token=shanghai_advent_2025_verify&hub.challenge=test"

# Probar mensaje diario
curl -X GET "https://shanghai.iancamps.dev/api/daily-message"

# Probar mensaje específico
curl -X POST "https://shanghai.iancamps.dev/api/daily-message" \
  -H "Content-Type: application/json" \
  -d '{"day": 1}'
```

### 8. Monitoreo
- **Vercel Analytics**: Para métricas de rendimiento
- **Meta Webhook Logs**: Para ver mensajes recibidos
- **Console de Vercel**: Para logs de errores

### 9. Optimizaciones implementadas
- ✅ Animaciones móviles espectaculares
- ✅ Efectos táctiles y de vibración
- ✅ Partículas flotantes y confeti
- ✅ Dragones voladores y farolillos
- ✅ Automatización de mensajes WhatsApp
- ✅ Webhook para respuestas automáticas
- ✅ Panel de administración
- ✅ Optimización para móvil
- ✅ SEO y meta tags
- ✅ Seguridad y headers
