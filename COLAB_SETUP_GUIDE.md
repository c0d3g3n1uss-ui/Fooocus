# 🎨 Fooocus Enhanced - Colab Setup Guide

## ¿Por qué usar Colab?

✅ **GPU Gratuita** - T4/P100 (perfecto para generación de imágenes)  
✅ **Sin instalación local** - Todo en la nube  
✅ **Acceso remoto** - Comparte el link con otros  
✅ **Persistencia** - Los modelos se guardan en caché  

---

## 📋 Instrucciones Rápidas

### Paso 1: Preparar el runtime
1. Abre [Google Colab](https://colab.research.google.com/)
2. Ve a **Runtime → Change runtime type**
3. Selecciona:
   - **Hardware accelerator**: GPU
   - **GPU type**: T4 (o P100 si disponible)
4. Haz clic en **Save**

### Paso 2: Subir el notebook
1. Descarga: `Fooocus_Enhanced_Colab.ipynb` (en el repo)
2. En Colab: **File → Upload notebook**
3. Selecciona el archivo descargado

### Paso 3: Ejecutar celdas en orden
```
1. Cell 1️⃣  → Verificar GPU ⏱️ 30 seg
2. Cell 2️⃣  → Instalar dependencias ⏱️ 2-3 min
3. Cell 3️⃣  → Clonar repositorio ⏱️ 1-2 min
4. Cell 4️⃣  → Crear launcher ⏱️ 10 seg
5. Cell 5️⃣  → LANZAR SERVIDOR ⏱️ soporte continuo
```

### Paso 4: Acceder
Cuando veas el mensaje:
```
[Fooocus] 🔗 Public URL: https://xxxx-xxxx-xxxx.ngrok-free.app
```

Abre ese link en tu navegador y ¡listo! 🎉

---

## 🎯 Características Disponibles

### ✨ Advanced Face Editor (Principal)
**Subir → Editar → Descargar**

1. **Carga facial** (foto del rostro)
2. **Conjunto/outfit** (opcional - referencia de cuerpo)
3. **Estilo** (FullHD, Hiperrealista, Anime, etc.)
4. **Prompts** (positivo y negativo)
5. **Calidad** (slider 1-10)
6. **Generar** → Imagen procesada

### 🎬 Video Face-Swapping
- Intercambia rostros en videos
- Detección automática

### 🎙️ Voice Cloning & TTS
- Clona voces de audio
- Síntesis de texto a voz

### 📱 Social Media Generator
- Contenido optimizado para redes
- TikTok, Instagram, YouTube

### 📝 Caption Generator
- Generación automática de títulos
- Multi-idioma

---

## 🔧 Solución de Problemas

### ❌ "ModuleNotFoundError: No module named 'webui_demo'"
**Solución:** Ejecuta Cell 3 completamente. Espera a que vea "✅ Repository cloned..."

### ❌ "CUDA out of memory"
**Solución:** 
- Reduce el slider de Quality a 5-6
- Reinicia el runtime (Runtime → Restart runtime)
- Usa GPU T4 en lugar de otros

### ❌ "Tunnel connection failed"
**Solución:**
- Re-ejecuta Cell 5
- O reinicia el runtime completamente

### ❌ "Connection timeout"
**Solución:**
- Mantén la pestaña de Colab abierta
- El servidor solo corre mientras Colab esté activo

---

## 💡 Tips Profesionales

### Para mejor rendimiento:
```python
# Usa Quality 7-8 para balance velocidad/calidad
# Usa GPU T4 como mínimo
# Primeras inferencias son más lentas (cargan modelos)
```

### Para compartir con otros:
```
1. Copia el link ngrok
2. Comparte: https://xxxx-xxxx-xxxx.ngrok-free.app
3. ¡No necesitan Colab!
```

### Para usar modelos específicos:
```
# Edita en Cell 5 el diccionario de estilos:
styles = {
    "FullHD Professional": {...},
    "Tu estilo": {...},  # ← Agrega aquí
}
```

---

## 📂 Estructura de Archivos en Colab

```
/content/Fooocus_Enhanced/
├── webui_demo.py          ← Interface principal
├── run_webui.py           ← Launcher local
├── launch_colab.py        ← Launcher para Colab (auto-generado)
├── models/                ← Modelos descargados
├── outputs/               ← Imágenes generadas
│   └── facial_edits/      ← Ediciones de rostros
└── ...otros archivos
```

---

## 🚀 Uso Avanzado

### Modificar el código en tiempo real:
1. En Colab: **Files → Browse files** (lado izquierdo)
2. Navega a `/content/Fooocus_Enhanced/webui_demo.py`
3. Haz doble clic para editar
4. Guarda (Ctrl/Cmd + S)
5. Re-ejecuta Cell 5

### Descargar resultados:
1. **Files → /content/Fooocus_Enhanced/outputs/**
2. Haz clic derecho en archivo → **Download**

### Parar el servidor:
- **Runtime → Interrupt execution** (cuadrado rojo ⏹️)
- O cierra la pestaña

---

## 📊 Comparación: Local vs Colab

| Característica | Local | Colab |
|---|---|---|
| GPU | Depende del PC | T4/P100 gratis |
| Instalación | 30+ min | 5-10 min |
| Uptime | Mientras corre | ~12h sesión |
| Velocidad | Varía | Consistente |
| Compartir | VPN/Tunnel | Link directo |
| Costo | Electricidad | Gratis |

---

## ⚠️ Limitaciones de Colab

- **Sesión máxima**: ~12 horas (después reconecta)
- **GPU compartida**: A veces reduce velocidad
- **Límite de almacenamiento**: ~50GB
- **Sin GPU**: Si muchos usuarios con T4 disponible

---

## 🤝 Soporte

Si encuentras problemas:

1. Revisa los logs en Colab (mitad inferior)
2. Reinicia el runtime: **Runtime → Restart runtime**
3. Re-ejecuta from Cell 1
4. Verifica que GPU está habilitado

---

## 📝 Próximos Pasos

1. ✅ Ejecuta el notebook en Colab
2. ✅ Prueba la interface de edición facial
3. ✅ Genera algunas imágenes de prueba
4. ✅ Descarga los resultados
5. ✅ Comparte feedback

**¡Que disfrutes! 🎉**

---

**Creado por:** c0d3g3n1us  
**Basado en:** Fooocus Fork  
**Última actualización:** Marzo 2026
