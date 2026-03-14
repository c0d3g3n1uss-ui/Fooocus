# 📝 CAPTION GENERATOR - GUÍA COMPLETA
# Auto-Generate Captions como HeyGen
# 
# ¡Nueva característica! Generación automática de subtítulos
# usando reconocimiento automático de voz (ASR)

## 🎯 ¿QUÉ ES?

**Caption Generator** es un módulo que auto-genera captions/subtítulos sincronizados desde el audio del video, **exactamente como HeyGen**.

Características:
- ✅ Reconocimiento automático de voz (ASR) con Whisper
- ✅ Múltiples idiomas soportados (8+)
- ✅ Sincronización fotograma a fotograma
- ✅ Múltiples formatos (SRT, VTT, ASS, JSON)
- ✅ Opción de incrustar en video o guardar por separado
- ✅ Estilos profesionales de captions

---

## 🚀 USO RÁPIDO

### Python API

```python
from modules.caption_generator import CaptionGenerator
from modules.social_media_creator import SocialMediaContentCreator

# Crear contenido CON captions automáticos
creator = SocialMediaContentCreator(quality='balanced')

result = creator.create_content_from_scratch(
    image_path="foto.jpg",
    voice_sample_path="voz.wav",
    script_text="Hola amigos!",
    platform='tiktok',
    add_captions=True,              # ← NUEVO: Activar captions
    caption_format='srt',            # Formato: srt, vtt, ass, json
    caption_embed=False,             # False = guardar por separado
    caption_language='es'            # Idioma para reconocimiento
)

# result['captions_file'] contiene la ruta de los captions
print(result['captions_file'])  # captions.srt
```

### WebUI

1. En Fooocus → Tab "🎬 Social Media Creator"
2. Subir foto, voz, escribir guión
3. **Expandir "📝 Captions & Subtitles (HeyGen-style)"**
4. ✅ Activar "Auto-Generate Captions"
5. Seleccionar formato (SRT recomendado)
6. Seleccionar idioma
7. Crear video normalmente

---

## 📋 FORMATOS SOPORTADOS

### 1. **SRT (SubRip)** - ⭐ RECOMENDADO
```
1
00:00:00,000 --> 00:00:02,500
Hola amigos!

2
00:00:02,500 --> 00:00:05,000
Este es mi primer video.
```
✅ Más compatible  
✅ Funciona en todos lados  
✅ Fácil de editar  

### 2. **VTT (WebVTT)** - Para HTML5
```
WEBVTT

00:00:00.000 --> 00:00:02.500
Hola amigos!

00:00:02.500 --> 00:00:05.000
Este es mi primer video.
```
✅ Para videos en navegador  
✅ HTML5 compatible  

### 3. **ASS (Advanced SubStation Alpha)** - Con estilos
```
[Script Info]
Title: Generated Captions

[Events]
Dialogue: 0,0:00:00.00,0:00:02.50,Default,,0,0,0,,Hola amigos!
Dialogue: 0,0:00:02.50,0:00:05.00,Default,,0,0,0,,Este es mi primer video.
```
✅ Incluye estilos visuales  
✅ Colores, fuentes, posición  
✅ Más control  

### 4. **JSON** - Para programadores
```json
[
  {
    "start": 0.0,
    "end": 2.5,
    "text": "Hola amigos!",
    "confidence": 0.98
  },
  {
    "start": 2.5,
    "end": 5.0,
    "text": "Este es mi primer video.",
    "confidence": 0.95
  }
]
```
✅ Para procesamiento programático  
✅ Incluye confianza de reconocimiento  

---

## 🌍 IDIOMAS SOPORTADOS

| Código | Idioma |
|--------|--------|
| `es` | Español |
| `en` | English |
| `fr` | Français |
| `de` | Deutsch |
| `it` | Italiano |
| `pt` | Português |
| `ja` | 日本語 |
| `zh` | 中文 |

Detecta automáticamente el idioma del audio.

---

## ⚙️ OPCIONES AVANZADAS

### GeneradorCaptions Directo

```python
from modules.caption_generator import (
    CaptionGenerator,
    SubtitleConfig,
    SubtitleFormat
)

# Inicializar generador
gen = CaptionGenerator(language='es', device='cuda')

# Extraer captions de video
captions = gen.extract_captions_from_video(
    'video.mp4',
    chunk_duration=30.0  # Procesar en chunks de 30s
)

# Refinar (opcional)
captions = gen.refine_captions(captions)

# Configurar estilos
config = SubtitleConfig(
    format=SubtitleFormat.SRT,
    style='professional',  # professional, modern, minimal, vibrant
    language='es',
    max_chars_per_line=42,
    font_size=24,
    font_color='white',
    background_color='black',
    position='bottom'  # bottom, top, center
)

# Guardar captions
gen.save_captions(captions, 'output.srt', config)

# O incrustar en video
gen.embed_captions_in_video(
    video_path='video.mp4',
    captions=captions,
    output_path='video_with_captions.mp4',
    config=config
)
```

### Extraer captions de solo audio

```python
# Si solo tienes audio
captions = gen.extract_captions_from_audio(
    'audio.wav',
    chunk_duration=30.0
)
```

### Función rápida

```python
from modules.caption_generator import generate_captions_for_video

# Todo en una línea
output = generate_captions_for_video(
    video_path='video.mp4',
    output_format='srt',     # srt, vtt, ass, json
    language='es',
    embed=False              # True = incrustar en video
)

print(f"Captions saved: {output}")
```

---

## 📊 CASOS DE USO

### Caso 1: TikTok con captions automáticos
```python
creator = SocialMediaContentCreator()
result = creator.create_content_from_scratch(
    image_path="foto.jpg",
    voice_sample_path="voz.wav",
    script_text="Mira esto!",
    platform='tiktok',
    add_captions=True,
    caption_format='srt',
    caption_embed=False  # Guardar por separado
)

# Resultado:
# - video.mp4 (video listo para TikTok)
# - video.srt (captions)
```

### Caso 2: YouTube con captions incrustados
```python
result = creator.create_content_from_scratch(
    image_path="foto.jpg",
    voice_sample_path="voz.wav",
    script_text="Tutorial de IA",
    platform='youtube',
    add_captions=True,
    caption_format='vtt',
    caption_embed=True  # ← Incrustar EN el video
)

# Resultado:
# - video_with_captions.mp4 (video + captions)
```

### Caso 3: Multi-idioma
```python
# Español
result_es = creator.create_content_from_scratch(
    image_path="foto.jpg",
    voice_sample_path="voz_es.wav",
    script_text="Hola amigos",
    platform='tiktok',
    add_captions=True,
    caption_language='es'
)

# Inglés (mismo video, diferentes captions)
result_en = creator.create_content_from_scratch(
    image_path="foto.jpg",
    voice_sample_path="voz_en.wav",
    script_text="Hello friends",
    platform='tiktok',
    add_captions=True,
    caption_language='en'
)
```

### Caso 4: Batch con captions
```python
# Procesar múltiples videos CON captions
results = creator.batch_create_content(
    image_dir="./fotos/",
    voice_sample_path="voz.wav",
    script_file="scripts.json"
    # Nota: Captions se generan automáticamente
    # para cada video en el batch
)
```

---

## 🎬 PIPELINE ACTUALIZADO

Ahora el pipeline tiene 6 pasos (antes 5):

```
1. Foto → Animación (SVD)
2. Muestra de voz → Clonación (XTTS_v2)
3. Texto → Síntesis de voz (TTS)
4. Video + Audio → Sincronización (Wav2Lip)
5. Audio → Captions automáticos ← NUEVO (ASR)
6. Video final → Optimización por plataforma
```

---

## 📥 REQUISITOS

Las `modules/caption_generator.py` ya está incluido.

**Dependencias adicionales:**

```bash
# Ya incluido en Fooocus:
pip install librosa librosa==0.10.0

# Para ASR (reconocimiento de voz):
pip install transformers torch

# Opcional (para mejor rendimiento):
pip install accelerate
```

---

## 🎛️ OPCIONES EN WEBUI

Nuevo Accordion: **"📝 Captions & Subtitles (HeyGen-style)"**

| Opción | Tipo | Valores | Defecto |
|--------|------|--------|---------|
| **Auto-Generate Captions** | Checkbox | ✅/❌ | ✅ Sí |
| **Subtitle Format** | Radio | srt, vtt, ass, json | `srt` |
| **Embed in Video** | Checkbox | ✅/❌ | ❌ No |
| **Caption Language** | Dropdown | es, en, fr, de, it, pt, ja, zh | `es` |

---

## 🔍 RESOLUCIÓN DE PROBLEMAS

### Problema: "Transformers not installed"
```bash
pip install transformers torch
```

### Problema: "ASR model not downloaded"
Primera ejecución descarga el modelo (500MB).
Internet requerido.

### Problema: "Audio not recognized"
- Aumentar duración del chunk: `chunk_duration=60`
- Verificar que el audio sea claro
- Probar otro idioma

### Problema: "Captions desincronizados"
- Usar `refine_captions()` para ajustar
- Aumentar `max_chars_per_line` si hay cortes

---

## 📈 RENDIMIENTO

| Operación | Tiempo |
|-----------|--------|
| Transcripción ASR (1 min audio) | 30-60s |
| Refinamiento de captions | 2-5s |
| Síntesis de captions a SRT | <1s |
| Incrustación en video | 20-40s |

**Total**: 60-120 segundos para video + captions

---

## 💡 COMPARACIÓN: Fooocus vs HeyGen

| Característica | HeyGen | Fooocus |
|---|---|---|
| Captions automáticos | ✅ | ✅ |
| Reconocimiento de voz | ✅ | ✅ |
| Sincronización | ✅ | ✅ |
| Múltiples idiomas | ✅ | ✅ |
| Incrustación en video | ✅ | ✅ |
| **Costo** | $$$$ | **🆓 Gratis** |
| **Local** | No (nube) | **Sí** |

---

## 🔗 INTEGRACIÓN CON PIPELINE

Los captions se generan automáticamente en el pipeline principal:

```python
result = creator.create_content_from_scratch(
    ...,
    add_captions=True  # ← Automátics
)

# Resultado incluye:
# result['output_video']      - Video principal
# result['captions_file']     - Archivo de captions
# result['captions_embedded'] - ¿Están incrustados?
```

---

## 📝 EJEMPLO COMPLETO

```python
from modules.social_media_creator import SocialMediaContentCreator
from pathlib import Path

# Crear
creator = SocialMediaContentCreator(quality='balanced')

# Generar contenido
result = creator.create_content_from_scratch(
    image_path="mi_foto.jpg",
    voice_sample_path="mi_voz.wav",
    script_text="¡Mira esto! Esto es increíble!",
    platform='instagram',
    add_captions=True,
    caption_format='srt',
    caption_embed=False,
    caption_language='es'
)

# Verificar resultado
if result['status'] == 'success':
    video = result['output_video']
    captions = result['captions_file']
    
    print(f"✅ Video: {Path(video).name}")
    print(f"📝 Captions: {Path(captions).name}")
    print(f"📱 Subir a: https://instagram.com/create")
else:
    print("❌ Error en creación")
```

---

## 🎓 PRÓXIMOS PASOS

1. **Instalar dependencias:** `pip install transformers torch`
2. **En WebUI:** Marcar "✅ Auto-Generate Captions"
3. **Crear video:** Los captions se generan automáticamente
4. **Descargar:** Video + Captions en SRT (o tu formato elegido)

---

**¡Genera captions profesionales como HeyGen, 100% gratuito y local!** 🚀✨
