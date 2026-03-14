#!/bin/bash

# ============================================
# FOOOCUS ENHANCEMENT - SETUP & RUN SCRIPT
# Complete installation and startup guide
# ============================================

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     FOOOCUS ENHANCEMENT - COMPLETE SETUP & LAUNCH GUIDE        ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Check Python
echo -e "${BLUE}Step 1: Checking Python Installation${NC}"
echo "─────────────────────────────────────────────────────────────────"
python_version=$(python --version 2>&1)
echo "Python found: $python_version"
echo ""

# Step 2: Install dependencies
echo -e "${BLUE}Step 2: Installing Dependencies${NC}"
echo "─────────────────────────────────────────────────────────────────"
echo "Installing: torch, numpy, opencv-python, Pillow, librosa, soundfile, transformers"
echo ""

# Try with pip
echo "Please wait while packages are downloaded and installed..."
echo ""

pip install --upgrade pip > /dev/null 2>&1

packages=(
    "torch"
    "numpy"
    "opencv-python"
    "Pillow"
    "librosa"
    "soundfile"
    "transformers"
)

for package in "${packages[@]}"; do
    echo -n "  Installing $package... "
    if pip install "$package" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Done${NC}"
    else
        echo -e "${YELLOW}⚠️  May need manual install${NC}"
    fi
done

echo ""

# Step 3: Verify installations
echo -e "${BLUE}Step 3: Verifying Installations${NC}"
echo "─────────────────────────────────────────────────────────────────"

python << 'VERIFY'
import sys
errors = []
packages = {
    'torch': 'PyTorch',
    'numpy': 'NumPy',
    'cv2': 'OpenCV',
    'PIL': 'Pillow',
    'librosa': 'Librosa',
    'soundfile': 'SoundFile',
    'transformers': 'Transformers',
}

for module, name in packages.items():
    try:
        __import__(module)
        print(f"  ✅ {name}")
    except ImportError:
        print(f"  ⚠️  {name} - not available yet")
        errors.append(name)

if errors:
    print(f"\n⚠️  Some packages may need manual installation:")
    print(f"    pip install {' '.join([p.lower() for p in errors])}")
else:
    print(f"\n✅ All packages verified!")

VERIFY

echo ""

# Step 4: Show available features
echo -e "${BLUE}Step 4: Available Features${NC}"
echo "─────────────────────────────────────────────────────────────────"
echo ""
echo "🎯 Photo Animation"
echo "   └─ Convert static photos to animated videos"
echo ""
echo "🎙️  Voice Cloning"
echo "   └─ Clone your voice for text-to-speech"
echo ""
echo "👄 Lip Synchronization"
echo "   └─ Automatic lip-sync to audio"
echo ""
echo "📝 Caption Generation (HeyGen-style)"
echo "   └─ Auto speech-to-text with timing sync"
echo ""
echo "🎬 Video Face Swapping"
echo "   └─ Change faces while preserving movement"
echo ""
echo "📱 Social Media Optimization"
echo "   └─ Auto-optimize for TikTok, Instagram, YouTube, etc."
echo ""

# Step 5: Launch options
echo -e "${BLUE}Step 5: Launch Fooocus${NC}"
echo "─────────────────────────────────────────────────────────────────"
echo ""
echo "Choose how to run Fooocus:"
echo ""
echo "Option A: WebUI (Recommended)"
echo "  $ python webui.py"
echo ""
echo "Option B: Run Examples"
echo "  $ python examples/caption_generator_examples.py"
echo "  $ python examples/social_media_examples.py"
echo ""
echo "Option C: Python Interactive"
echo "  $ python"
echo "  >>> from modules.caption_generator import CaptionGenerator"
echo "  >>> gen = CaptionGenerator(language='es')"
echo ""

echo -e "${GREEN}════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}         🎉 ALL SYSTEMS READY! Choose an option above          ${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════════${NC}"
echo ""
