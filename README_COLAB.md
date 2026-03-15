# 🎨 Fooocus Enhanced - Google Colab Edition

## 📌 Overview

Ejecuta **Fooocus Enhanced** en Google Colab con GPU gratuita (T4/P100) sin instalación local.

### ✨ Ventajas Colab:
- ✅ GPU Gratuita (T4, P100 disponibles)
- ✅ Sin instalación en PC
- ✅ Acceso remoto (comparte link)
- ✅ Almacenamiento en la nube
- ✅ Rápido y fácil

---

## 🚀 ¿Cómo empezar?

### Opción 1: Notebook Completo (Recomendado)

1. **Descarga**: `Fooocus_Enhanced_Colab.ipynb`
2. Abre [Google Colab](https://colab.research.google.com)
3. **File → Upload notebook** → Selecciona el .ipynb descargado
4. Ve a **Runtime → Change runtime type** → Selecciona **GPU**
5. Ejecuta celdas en orden (1→2→3→4→5)
6. Haz clic en el link ngrok cuando aparezca ✅

**Tiempo estimado:** 5-10 minutos (primer run)

---

### Opción 2: Single Cell Quick Start

Copia y pega esto en **UNA celda** de Colab:

```python
# Descarga y ejecuta el script
!curl -s https://raw.githubusercontent.com/tu-usuario/Fooocus/main/colab_quick_start.py | python
```

O manualmente en una celda de Colab:

```python
import subprocess
subprocess.run(["curl", "-s", "https://raw.githubusercontent.com/tu-usuario/Fooocus/main/colab_quick_start.py", "|", "python"], shell=True)
```

---

## 📊 Archivos Disponibles

| Archivo | Descripción | Cuando usarlo |
|---------|-------------|---|
| `Fooocus_Enhanced_Colab.ipynb` | Notebook completo con 5 celdas | Primera vez / setup detallado |
| `colab_quick_start.py` | Script de una línea | Setup rápido |
| `COLAB_SETUP_GUIDE.md` | Guía completa en español | Referencia / troubleshooting |
| `launch_colab.py` | Launcher auto-generado | No tocar, se crea automáticamente |

---

## 🎯 Características

### ✨ Advanced Face Editor (Principal)
- Carga foto facial + referencia de outfit
- 10 estilos profesionales
- Control de calidad (1-10)
- Prompts positivos/negativos
- Generación de imágenes

### 🎬 Video Face-Swapping
- Intercambia rostros en videos
- Detección automática de faces

### 🎙️ Voice Cloning & TTS
- Clona voces
- Síntesis de audio

### 📱 Social Media Creator
- Optimiza para redes sociales
- TikTok, Instagram, YouTube

### 📝 Caption Generator
- Generación automática de títulos
- Multi-idioma

---

## 💻 Requisitos Técnicos

| Requisito | Detalles |
|-----------|---------|
| **Navegador** | Chrome, Firefox, Safari, Edge (cualquiera) |
| **Cuenta** | Google (para Colab) |
| **GPU** | T4 recomendado (P100 si disponible) |
| **RAM** | Colab maneja automáticamente |
| **Conexión** | Internet estable |

---

## 🔗 Cómo acceder después de ejecutar

1. En la salida de Colab verás:
```
[Fooocus] 🔗 Public URL: https://xxxx-xxxx-xxxx.ngrok-free.app
```

2. **Copia ese link**
3. **Abre en navegador** → ¡Listo!
4. Puedes **compartir con otros** ese link

---

## ⏱️ Tiempos de Ejecución

| Paso | Tiempo |
|------|--------|
| Cell 1 (GPU check) | ~30 seg |
| Cell 2 (Install) | ~2-3 min |
| Cell 3 (Clone) | ~1-2 min |
| Cell 4 (Launcher) | ~10 seg |
| Cell 5 (Launch) | ~1 min (first), <10 seg (next) |
| **Total primera vez** | ~7-10 min |
| **Subsecuentes** | ~2-3 min |

---

## 🆘 Troubleshooting

### ❌ "ModuleNotFoundError"
```
✅ Ejecuta toda la Cell 3 (clonado)
✅ Espera a ver "✅ Repository cloned..."
```

### ❌ "CUDA out of memory"
```
✅ Reduce quality slider a 5-6
✅ Runtime → Restart runtime
✅ Usa T4 GPU en lugar de otros
```

### ❌ "ngrok connection failed"
```
✅ Re-ejecuta Cell 5
✅ O reinicia runtime completamente
```

### ❌ "Connection timeout"
```
✅ Mantén Colab abierto mientras usas la app
✅ El servidor solo corre mientras Colab esté activo
```

---

## 💡 Tips Pro

### Para mejor rendimiento:
```python
Quality: 7-8 (balance velocidad/calidad)
GPU: T4 mínimo
Primeras inferencias: Más lentas (cargan modelos)
```

### Para compartir con amigos:
```
1. Copia el link ngrok
2. Comparte: https://xxxx-xxxx-xxxx.ngrok-free.app
3. ¡Ellos pueden usarlo sin tener Colab!
```

### Para personalizar:
```
1. Files → /Fooocus_Enhanced/webui_demo.py (editar)
2. Guarda (Ctrl+S)
3. Re-ejecuta Cell 5
```

---

## 📂 Dónde van los archivos

| Tipo | Ubicación |
|------|-----------|
| **Modelos** | `/content/Fooocus_Enhanced/models/` |
| **Outputs** | `/content/Fooocus_Enhanced/outputs/` |
| **Ediciones facial** | `/content/Fooocus_Enhanced/outputs/facial_edits/` |
| **App code** | `/content/Fooocus_Enhanced/` |

### Descargar resultados:
1. **Files → Navega a outputs/**
2. Click derecho en archivo → **Download**

---

## 📋 Checklist Rápido

- [ ] Tengo cuenta de Google
- [ ] Estoy en https://colab.research.google.com
- [ ] He subido el notebook
- [ ] Cambié runtime a GPU (T4)
- [ ] He ejecutado Cell 1 → GPU check ✓
- [ ] He ejecutado Cell 2 → Install ✓
- [ ] He ejecutado Cell 3 → Clone ✓
- [ ] He ejecutado Cell 4 → Launcher ✓
- [ ] He ejecutado Cell 5 → Server running ✓
- [ ] He copiado el link ngrok
- [ ] Abrí el link en navegador
- [ ] ¡Estoy usando Fooocus! 🎉

---

## 🔄 Comparación: Local vs Colab

```
┌─────────────────┬──────────────────┬──────────────────┐
│ Característica  │      Local       │      Colab       │
├─────────────────┼──────────────────┼──────────────────┤
│ GPU             │ Depende del PC   │ T4/P100 Gratis   │
│ Instalación     │ 30+ minutos      │ 5-10 minutos     │
│ Uptime          │ Mientras corre   │ ~12h sesión      │
│ Velocidad       │ Variable         │ Consistente      │
│ Compartir       │ VPN/Tunnel       │ Link ngrok       │
│ Costo           │ Electricidad     │ GRATIS           │
│ Modelos caché   │ Disco duro       │ Colab storage    │
│ Portabilidad    │ Mismo PC         │ Cualquier lugar  │
└─────────────────┴──────────────────┴──────────────────┘
```

---

## 🚨 Limitaciones Conocidas

- **Máximo 12h** por sesión (después reconecta)
- **GPU compartida** a veces reduce velocidad
- **Almacenamiento**: ~50GB total
- **GPU limitada** si muchos usuarios en T4
- **Sesión se reinicia** si no hay actividad

---

## ✉️ Soporte

Si encuentras problemas:

1. Revisa los **logs en Colab** (mitad inferior)
2. **Runtime → Restart runtime**
3. Re-ejecuta from Cell 1
4. Verifica que **GPU esté habilitado**

---

## 🎓 Más Información

- **COLAB_SETUP_GUIDE.md** - Guía completa
- **webui_demo.py** - Code fuente de interface
- **GitHub** - [c0d3g3n1us/Fooocus](https://github.com/c0d3g3n1us/Fooocus)

---

## 🎉 ¡Empezar Ya!

1. Descarga: `Fooocus_Enhanced_Colab.ipynb`
2. Sube a Colab
3. Ejecuta celdas (1→5)
4. ¡Disfruta! 🚀

---

**Creado por:** c0d3g3n1us  
**Basado en:** Fooocus Fork  
**Actualizado:** Marzo 2026
