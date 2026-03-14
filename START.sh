#!/bin/bash

# ============================================
# FOOOCUS - FAST START (Copy-Paste Everything)
# ============================================

# Paso 1: Ir a la carpeta
cd /Users/c0d3g3n1us/Fooocus

# Paso 2: Crear ambiente virtual
python3 -m venv .venv 2>/dev/null

# Paso 3: Activar
source .venv/bin/activate

# Paso 4: Actualizar pip
pip install --upgrade pip setuptools wheel >/dev/null 2>&1

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║     Installing Fooocus Enhancement - Please wait...        ║"
echo "║     This will take 5-15 minutes (downloading PyTorch)      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Paso 5: Instalar dependencias
pip install \
  numpy==1.26.4 \
  torch \
  torchvision \
  opencv-python==4.10.0.84 \
  Pillow==10.5.0 \
  librosa==0.10.1 \
  soundfile==0.12.1 \
  transformers==5.3.0 \
  scipy==1.14.0 \
  tqdm==4.66.4 \
  pyyaml==7.0 \
  gradio==4.8.0

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║            ✅ Installation Complete!                       ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "Verifying packages..."
echo ""

python3 << 'VERIFY'
packages = ['numpy', 'torch', 'cv2', 'PIL', 'librosa', 'soundfile', 'transformers', 'gradio']
ok = 0
for p in packages:
    try:
        __import__(p)
        print(f"  ✅ {p}")
        ok += 1
    except:
        print(f"  ❌ {p}")
print(f"\n✅ {ok}/{len(packages)} packages ready!")
VERIFY

echo ""
echo "🚀 RUNNING FOOOCUS WebUI..."
echo ""
echo "When you see 'Running on http://127.0.0.1:7860'"
echo "Open that URL in your browser!"
echo ""
echo "────────────────────────────────────────────────────────────"
echo ""

python webui.py
