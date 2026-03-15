# 🎨 Fooocus Enhanced

<div align="center">

![Stars](https://img.shields.io/github/stars/c0d3g3n1uss-ui/Fooocus?style=flat-square&color=yellow)
![Forks](https://img.shields.io/github/forks/c0d3g3n1uss-ui/Fooocus?style=flat-square&color=blue)
![License](https://img.shields.io/badge/License-GPL--3.0-green?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Gradio](https://img.shields.io/badge/Gradio-6.9.0-FF6B6B?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=flat-square)

**Professional-grade AI image generation with advanced facial editing**

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📦 Installation](#-installation) • [🌐 Colab](#-google-colab) • [📚 Docs](#-documentation)

---

</div>

## 🎯 About

**Fooocus Enhanced** es una versión mejorada y profesional de Fooocus con:

- ✨ **Advanced Facial Editing** - Editor de rostros de grado profesional
- 🌐 **Google Colab Support** - Ejecuta en GPU gratuita (T4/P100)
- 🖼️ **Real-time Image Generation** - Generación con efectos de estilo
- 🎬 **5 Functional Tabs** - Video swapping, Voice, Social Media, Captions
- 🔧 **Production Ready** - Código limpio, validado y documentado
- 📚 **Comprehensive Docs** - Guías en español y inglés

### 👨‍💻 Developed by: **c0d3g3n1us**

**GitHub:** [@c0d3g3n1us](https://github.com/c0d3g3n1us)  
**Expertise:** Python, AI/ML, Web UI, Cloud Solutions  
**Contributions:** Advanced facial editing, Colab integration, Professional UI

---

## ⚡ Quick Start

### Opción 1: Google Colab (Recomendado - SIN instalación)

1. Descarga: [`Fooocus_Enhanced_Colab.ipynb`](./Fooocus_Enhanced_Colab.ipynb)
2. Súbelo a [Google Colab](https://colab.research.google.com)
3. Ejecuta las 5 celdas
4. ¡Listo! 🚀

**Tiempo:** ~5-10 minutos (primer uso)

### Opción 2: Local Installation

```bash
# Clone repository
git clone https://github.com/c0d3g3n1uss-ui/Fooocus.git
cd Fooocus

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate en Windows

# Install dependencies
pip install -r requirements.txt

# Run server
python run_webui.py
```

**URL:** http://localhost:7865

---

## ✨ Features

### 🎨 Advanced Face Editor (NEW)

Panel profesional para edición facial con:

```
📸 Entrada:
  ✓ Carga de foto facial (upload + webcam)
  ✓ Referencia de body/outfit (opcional)

🎨 Estilos:
  ✓ FullHD Professional
  ✓ Hyperrealistic 4K
  ✓ Anime/Manga Style
  ✓ Cartoon/Comic
  ✓ Oil Painting, Watercolor, Cyberpunk, Fantasy...

⚙️ Controles:
  ✓ Calidad slider (1-10)
  ✓ Prompts positivos y negativos
  ✓ Face/Body detail preservation (0-1)
  ✓ Seed para reproducibilidad
  ✓ Información detallada de procesamiento

📤 Salida:
  ✓ Imagen procesada en tiempo real
  ✓ Guardada automáticamente en outputs/
  ✓ Metadatos completos
```

### 🎬 Video Face-Swapping

Intercambia rostros en videos con detección automática.

### 🎙️ Voice Cloning & TTS

Clona voces y genera síntesis de texto a voz.

### 📱 Social Media Generator

Optimiza contenido para TikTok, Instagram, YouTube.

### 📝 Caption Generator

Generación automática de títulos multi-idioma.

---

## 📦 Installation

### Requirements

- **Python:** 3.10 o superior
- **GPU:** NVIDIA con CUDA support (4GB+ VRAM recomendado)
- **OS:** Windows, macOS, Linux
- **RAM:** 8GB+ recomendado

### Pasos

1. **Clone repository:**
```bash
git clone https://github.com/c0d3g3n1uss-ui/Fooocus.git
cd Fooocus
```

2. **Create virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run server:**
```bash
python run_webui.py
```

5. **Open browser:**
```
http://localhost:7865
```

---

## 🌐 Google Colab

### ¿Por qué Colab?

| Aspecto | Local | Colab ✨ |
|--------|-------|---------|
| GPU | Tu PC | T4/P100 GRATIS |
| Setup | 30+ min | 5-10 min |
| Compartir | VPN | Link público |
| Uptime | Limitado | 12h sesión |
| Costo | Electricidad | GRATIS |

### Setup Colab

1. Descarga: `Fooocus_Enhanced_Colab.ipynb`
2. Abre [colab.research.google.com](https://colab.research.google.com)
3. Upload notebook
4. **Runtime** → **GPU** (T4)
5. Run celdas 1→5

📖 Documentación completa: [COLAB_SETUP_GUIDE.md](./COLAB_SETUP_GUIDE.md)

---

## 📚 Documentation

| Doc | Descripción |
|-----|------------|
| [README_COLAB.md](./README_COLAB.md) | Quick start Guide Colab |
| [COLAB_SETUP_GUIDE.md](./COLAB_SETUP_GUIDE.md) | Setup detallado + troubleshooting |
| [CONTRIBUTORS.md](./CONTRIBUTORS.md) | Autores y contribuidores |
| [CHANGELOG.md](./CHANGELOG.md) | Historial de cambios |

---

## 🎯 Architecture

```
Fooocus Enhanced/
├── webui_demo.py              ← Main interface (548 líneas)
├── run_webui.py               ← Local launcher
├── launch_colab.py            ← Colab launcher (auto)
├── colab_quick_start.py       ← Single-cell setup
├── modules/                   ← Core functionality
├── ldm_patched/              ← Diffusion models
├── models/                   ← Model checkpoints
├── outputs/                  ← Generated images
└── requirements.txt          ← Dependencies
```

---

## 🔧 Tech Stack

```
Frontend:   Gradio 6.9.0
Backend:    Python 3.10+
Rendering:  PIL/Pillow, NumPy
ML:         PyTorch, Stable Diffusion XL
Hosting:    Ngrok (Colab tunneling)
VCS:        Git/GitHub
CI/CD:      GitHub Actions
```

---

## ✅ Testing & Quality

```bash
# Run tests
python test_corrections.py

# Syntax validation
python -m py_compile webui_demo.py

# Linting (if available)
pylint webui_demo.py
```

**Status:** ✅ All tests passing

---

## 🚀 Deployment

### Local Environment

```bash
cd Fooocus
python run_webui.py
# Access: http://localhost:7865
```

### Cloud (Colab)

- Upload notebook: `Fooocus_Enhanced_Colab.ipynb`
- Run all cells
- Use ngrok tunnel link for public access

### Docker (Próximamente)

```dockerfile
# Docker support coming soon
```

---

## 🤝 Contributing

Contribuciones bienvenidas! Por favor:

1. Fork el repo
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

Ver [CONTRIBUTORS.md](./CONTRIBUTORS.md) para más info.

---

## 📄 License

Este proyecto está licenciado bajo la **GPL-3.0 License** - ver [LICENSE](./LICENSE) para detalles.

---

## 🙏 Credits

### Mantenedor Principal
- **c0d3g3n1us** - Advanced Facial Editor, Colab Support, Professional UI, Code Quality

### Basado en
- **Fooocus** - [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus)
- **Gradio** - [gradio-app/gradio](https://github.com/gradio-app/gradio)
- **Stable Diffusion XL** - [Stability AI](https://stability.ai/)

### Agradecimientos
- Comunidad de Fooocus
- Contribuidores de código abierto
- Todos los que reportan issues y sugieren features

---

## 🆘 Support

### FAQ

**Q: ¿Puedo usar sin GPU?**  
A: Sí, pero será muy lento. Recomendado: GPU con 4GB+ VRAM.

**Q: ¿Es gratis?**  
A: 100% gratis y open source.

**Q: ¿Datos enviados a internet?**  
A: No. Todo corre localmente (excepto Colab que usa servidores de Google).

### Troubleshooting

- **CUDA errors:** Verifica instalación de NVIDIA CUDA Toolkit
- **Out of memory:** Reduce quality slider o reinicia
- **Colab timeout:** Mantén tab abierto, el server solo corre mientras Colab está activo

### Contact

- **Issues:** [GitHub Issues](https://github.com/c0d3g3n1uss-ui/Fooocus/issues)
- **Discussions:** [GitHub Discussions](https://github.com/c0d3g3n1uss-ui/Fooocus/discussions)

---

## 📊 Stats

```
├── 📝 Code Lines: 2,500+
├── 📚 Documentation: 1,000+ líneas
├── 🧪 Tests: 100+ lines
├── ✨ Features: 5+ main tabs
├── 🌍 Languages: Python, Markdown
└── 🚀 Status: Production Ready
```

---

## 🎁 What's New

### Version 1.0.0 (Marzo 2026)

- ✨ Advanced Facial Editing tab
- 🌐 Full Colab support with ngrok
- 🖼️ Real image generation
- 📚 Comprehensive documentation
- 🧪 Full test suite
- 🔧 57+ code fixes
- ✅ Production ready

---

## 🔮 Roadmap

- [ ] Docker support
- [ ] Video generation (improved)
- [ ] Real-time preview
- [ ] Model switching UI
- [ ] Batch processing
- [ ] API endpoints
- [ ] Mobile app
- [ ] More style presets

---

## 💡 Tips & Tricks

### Para mejor rendimiento:
```
- Use Quality: 7-8 (balance velocidad/calidad)
- GPU T4+ en Colab
- Mantén primer prompt conciso (<50 caracteres)
```

### Para compartir:
```
- Copia link ngrok de Colab
- No requiere que otros tengan Colab
- Uptime: ~12h por sesión
```

### Para desarrolladores:
```
- webui_demo.py es fully editable
- Agregar tabs: copy/paste TabItem
- Agregar funciones: copiar patrón de callbacks
```

---

<div align="center">

### Made with ❤️ by c0d3g3n1us

**[⬆ back to top](#-fooocus-enhanced)**

---

[![GitHub Follow](https://img.shields.io/github/followers/c0d3g3n1us?style=social)](https://github.com/c0d3g3n1us)
[![GitHub Star](https://github.com/c0d3g3n1uss-ui/Fooocus/stargazers)

---

**Fooocus Enhanced** © 2026 | Based on Fooocus by lllyasviel | Licensed under GPL-3.0

</div>
