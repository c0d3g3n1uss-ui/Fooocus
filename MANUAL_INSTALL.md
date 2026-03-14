# 🚀 FOOOCUS ENHANCEMENT - MANUAL INSTALLATION GUIDE

## 📋 Paso 1: Verificar Python

Abre Terminal y ejecuta:

```bash
python3 --version
```

Deberías ver: `Python 3.10+` o `Python 3.14.3`

✅ Si ves una versión, continúa al Paso 2

---

## 📋 Paso 2: Ir a la Carpeta de Fooocus

```bash
cd /Users/c0d3g3n1us/Fooocus
```

Verifica que estés en el lugar correcto:
```bash
pwd
```

Deberías ver: `/Users/c0d3g3n1us/Fooocus`

---

## 📋 Paso 3: Crear Ambiente Virtual

```bash
python3 -m venv .venv
```

Esto crea una carpeta `.venv` con el ambiente aislado.

---

## 📋 Paso 4: Activar Ambiente Virtual

**En macOS/Linux:**
```bash
source .venv/bin/activate
```

Deberías ver `(.venv)` al inicio de tu terminal.

**Ejemplo:**
```
(.venv) usuario@Mac Fooocus % 
```

---

## 📋 Paso 5: Instalar Dependencias

Copia y pega este comando (todo de una vez):

```bash
pip install --upgrade pip && pip install numpy torch torchvision opencv-python Pillow librosa soundfile transformers scipy tqdm pyyaml gradio
```

**⏱️ Esto toma 5-15 minutos** (PyTorch es grande)

Espera a que termine. Deberías ver:
```
Successfully installed numpy-1.26.4 torch-2.1.0 ...
```

---

## 📋 Paso 6: Verificar Instalaciones

Ejecuta esto:

```bash
python -c "import torch, numpy, cv2, PIL, librosa, transformers, gradio; print('✅ All packages installed!')"
```

Si ves `✅ All packages installed!` → **¡Continuamos!**

Si ves errores → **Repite el Paso 5**

---

## 🎯 Paso 7: Ejecutar Fooocus WebUI

```bash
python webui.py
```

Verás algo como:
```
 * Running on http://127.0.0.1:7860
 * Press CTRL+C to quit
```

Abre tu navegador y ve a: **http://localhost:7860**

---

## 🎯 Usar Fooocus

### En WebUI:

1. **Upload Photo** → Selecciona una imagen
2. **Voice Sample** → Selecciona un audio (3-10 segundos)
3. **Script** → Escribe lo que quieres que diga
4. **Platform** → TikTok, Instagram, YouTube, etc.
5. **Add Captions** → ✅ Marcar para captions
6. **Caption Format** → SRT (recomendado)
7. **Click "Create"** → ¡Espera!
8. **Download** → Tu video con captions

---

## 💡 Ejemplos por Línea de Comandos

### Ejemplo 1: Generar Captions

```bash
python
>>> from modules.caption_generator import CaptionGenerator
>>> gen = CaptionGenerator(language='es')
>>> captions = gen.extract_captions_from_video('video.mp4')
>>> gen.save_captions(captions, 'output.srt', {})
>>> exit()
```

### Ejemplo 2: Crear Video Completo

```bash
python
>>> from modules.social_media_creator import SocialMediaContentCreator
>>> creator = SocialMediaContentCreator(quality='balanced')
>>> result = creator.create_content_from_scratch(
...     image_path='foto.jpg',
...     voice_sample_path='voz.wav',
...     script_text='¡Hola amigos!',
...     platform='tiktok',
...     add_captions=True
... )
>>> print(result['output_video'])
>>> exit()
```

---

## ❓ Troubleshooting

### ❌ "command not found: python3"
→ Instala Python: https://www.python.org/downloads/

### ❌ "No module named 'torch'"
→ Repite el Paso 5 completo

### ❌ WebUI no se inicia
→ Verifica que `.venv` está activado (ves `(.venv)` en terminal?)

### ❌ "Permission denied: 'webui.py'"
→ Ejecuta: `chmod +x webui.py`

### ❌ "pip: command not found"
→ Usa: `python3 -m pip install ...` en lugar de `pip install ...`

---

## 🎯 Resumen Rápido (Copy-Paste Todo)

```bash
# 1. Ir a carpeta
cd /Users/c0d3g3n1us/Fooocus

# 2. Crear ambiente
python3 -m venv .venv

# 3. Activar
source .venv/bin/activate

# 4. Instalar (COPIA ESTO COMPLETO)
pip install --upgrade pip && pip install numpy torch torchvision opencv-python Pillow librosa soundfile transformers scipy tqdm pyyaml gradio

# 5. Ejecutar
python webui.py

# 6. Abre: http://localhost:7860
```

---

## 🎉 ¿Listo?

Una vez que veas el WebUI:
1. Sube una foto
2. Sube un audio (tu voz)
3. Escribe un script
4. ✅ Marca "Add Captions"
5. Click "Create"!

¡Tu video con captions HeyGen-style será generado automáticamente!

---

**Última actualización:** 14 de marzo de 2026  
**Autor:** GitHub Copilot  
**Estado:** ✅ Listo para producción
