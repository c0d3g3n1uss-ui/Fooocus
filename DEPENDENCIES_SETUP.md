# 📦 Instalación de Dependencias - Fooocus Mejorado

## ⚠️ Estado Actual
El proyecto está configurado para **Python 3.10** pero tienes **Python 3.14.3** instalado.
Algunos paquetes no son totalmente compatibles con Python 3.14 en el PyPI estándar.

## ✅ Solución Recomendada: Instalar con Conda

### Opción A: Instalación Rápida (RECOMENDADO)
```bash
# 1. Ejecutar el script de instalación automática
bash install_dependencies.sh

# 2. Activar el entorno
conda activate fooocus

# 3. Verificar instalación
python -c "import torch; print(f'PyTorch {torch.__version__} ✅')"
```

### Opción B: Instalación Manual Step-by-Step

#### 1. Instalar Conda (si no lo tienes)
```bash
# Descargar Miniconda
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o miniconda.sh

# Instalar
bash miniconda.sh -b -p $HOME/miniconda3

# Agregar a PATH
export PATH="$HOME/miniconda3/bin:$PATH"
```

#### 2. Crear Entorno con Python 3.10
```bash
conda create -n fooocus python=3.10 pip -y
conda activate fooocus
```

#### 3. Instalar PyTorch (importante: necesita versión correcta)
```bash
# Para MacOS con CPU (si no tienes GPU NVIDIA)
conda install pytorch torchvision torchaudio -c pytorch -y

# ALTERNATIVA: Para GPU NVIDIA CUDA 11.8
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
```

#### 4. Instalar Dependencias Restantes
```bash
pip install \
    numpy \
    opencv-python \
    Pillow \
    librosa \
    soundfile \
    transformers \
    scipy \
    tqdm \
    pyyaml
```

#### 5. Instalar Requisitos del Proyecto
```bash
pip install -r requirements_versions.txt
```

## 🚀 Uso Posterior

### Cada vez que uses Fooocus:
```bash
# Activar el entorno
conda activate fooocus

# Usar webui normalmente
python webui.py
```

### Deactivar el entorno cuando termines:
```bash
conda deactivate
```

## 📋 Paquetes Requeridos

| Paquete | Versión | Propósito |
|---------|---------|----------|
| `torch` | 2.1.0+ | Deep learning framework |
| `numpy` | 1.26.4+ | Numeric computations |
| `opencv-python` | 4.10.0+ | Video/image processing |
| `Pillow` | 10.5.0+ | Image I/O |
| `librosa` | 0.10+ | Audio processing |
| `soundfile` | 0.12+ | Audio files |
| `transformers` | 5.3.0+ | NLP models (Whisper ASR) |

## ✅ Verificar Instalación

Después de instalar, corre esto:
```bash
python -c "
import torch
import numpy as np
import cv2
from PIL import Image
import librosa
import soundfile as sf
from transformers import pipeline

print('✅ torch:', torch.__version__)
print('✅ numpy:', np.__version__)
print('✅ cv2:', cv2.__version__)
print('✅ PIL:', Image.__version__)
print('✅ librosa:', librosa.__version__)
print('✅ soundfile ready')
print('✅ transformers:', pipeline.__module__)
print('\\n🎉 All dependencies installed!')
"
```

## 🐛 Troubleshooting

### Error: "No module named 'torch'"
→ Verificar que conda activate fooocus está activo

### Error: "Bad CPU type in executable"
→ Usar Miniconda x86_64 en vez de arm64 (línea en el script)

### Error: "CUDA not found"
→ Es ok, el sistema usará CPU automáticamente

### VS Code sigue mostrando errores en rojo
→ Agregar esto a `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.analysis.typeCheckingMode": "off"
}
```

## 📞 Soporte

Para más información:
- Documentación oficial: https://docs.conda.io
- PyTorch: https://pytorch.org/get-started
- Whisper (ASR): https://github.com/openai/whisper

---

**Última actualización:** 14 marzo 2026
**Estado:** Probado en macOS con Python 3.14.3 → Conda + Python 3.10
