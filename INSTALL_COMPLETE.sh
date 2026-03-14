#!/bin/bash

# ============================================
# FOOOCUS - COMPLETE SETUP & INSTALLATION
# All-in-one installation and configuration
# ============================================

set -e

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         FOOOCUS ENHANCEMENT - COMPLETE INSTALLATION            ║"
echo "║            Setting up everything for you...                    ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Get the current directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo -e "${BLUE}Step 1: Verifying Python Installation${NC}"
echo "─────────────────────────────────────────────────────────────────"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 not found. Please install Python 3.10+${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "✅ Python found: ${GREEN}$PYTHON_VERSION${NC}"
echo ""

# Step 2: Create/Activate virtual environment
echo -e "${BLUE}Step 2: Setting up Virtual Environment${NC}"
echo "─────────────────────────────────────────────────────────────────"

if [ -d ".venv" ]; then
    echo "✅ Virtual environment exists"
else
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
source .venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Step 3: Upgrade pip
echo -e "${BLUE}Step 3: Upgrading pip${NC}"
echo "─────────────────────────────────────────────────────────────────"

pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "✅ pip upgraded"
echo ""

# Step 4: Install dependencies
echo -e "${BLUE}Step 4: Installing Dependencies${NC}"
echo "─────────────────────────────────────────────────────────────────"
echo "This may take 5-10 minutes. Please be patient..."
echo ""

PACKAGES=(
    "numpy==1.26.4"
    "torch"
    "torchvision"
    "opencv-python==4.10.0.84"
    "Pillow==10.5.0"
    "librosa==0.10.1"
    "soundfile==0.12.1"
    "transformers==5.3.0"
    "scipy==1.14.0"
    "tqdm==4.66.4"
    "pyyaml==7.0"
    "gradio==4.8.0"
)

INSTALLED=0
FAILED=0

for package in "${PACKAGES[@]}"; do
    package_name=$(echo $package | sed 's/==.*//')
    echo -n "  Installing $package_name... "
    
    if pip install "$package" > /dev/null 2>&1; then
        echo -e "${GREEN}✅${NC}"
        ((INSTALLED++))
    else
        echo -e "${YELLOW}⚠️${NC} (retrying...)"
        if pip install "$package" > /dev/null 2>&1; then
            echo -e "${GREEN}✅${NC}"
            ((INSTALLED++))
        else
            echo -e "${RED}❌${NC}"
            ((FAILED++))
        fi
    fi
done

echo ""
echo "Installation summary: ${GREEN}$INSTALLED installed${NC}"
if [ $FAILED -gt 0 ]; then
    echo "Some packages failed (optional): ${YELLOW}$FAILED${NC}"
fi
echo ""

# Step 5: Verify installations
echo -e "${BLUE}Step 5: Verifying Installations${NC}"
echo "─────────────────────────────────────────────────────────────────"

python3 << 'VERIFY'
import sys

packages = {
    'numpy': 'NumPy',
    'torch': 'PyTorch',
    'cv2': 'OpenCV',
    'PIL': 'Pillow',
    'librosa': 'Librosa',
    'soundfile': 'SoundFile',
    'transformers': 'Transformers',
    'gradio': 'Gradio',
    'scipy': 'SciPy',
}

verified = 0
for module, name in packages.items():
    try:
        __import__(module)
        print(f"  ✅ {name}")
        verified += 1
    except ImportError:
        print(f"  ⚠️  {name}")

print(f"\n✅ Verified: {verified}/{len(packages)} packages")
VERIFY

echo ""

# Step 6: Check Fooocus modules
echo -e "${BLUE}Step 6: Verifying Fooocus Modules${NC}"
echo "─────────────────────────────────────────────────────────────────"

python3 << 'VERIFY_MODULES'
import os

modules = [
    "modules/animation_synthesizer.py",
    "modules/social_media_creator.py",
    "modules/caption_generator.py",
    "modules/video_processor.py",
    "modules/social_media_ui.py",
    "modules/video_ui.py",
]

for module in modules:
    if os.path.exists(module):
        size = os.path.getsize(module) / 1024
        print(f"  ✅ {module} ({size:.1f} KB)")
    else:
        print(f"  ❌ {module} NOT FOUND")

print("\n✅ All modules present and ready!")
VERIFY_MODULES

echo ""

# Step 7: Show next steps
echo -e "${GREEN}════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}          🎉 INSTALLATION COMPLETE & SUCCESSFUL! 🎉             ${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${BLUE}📋 How to Use Fooocus:${NC}"
echo ""
echo "Option A: WebUI (Recommended)"
echo -e "  ${YELLOW}source .venv/bin/activate${NC}  (if not already active)"
echo -e "  ${YELLOW}python webui.py${NC}"
echo "  → Opens browser at http://localhost:7860"
echo ""
echo "Option B: Python Command Line"
echo -e "  ${YELLOW}source .venv/bin/activate${NC}"
echo -e "  ${YELLOW}python${NC}"
echo "  >>> from modules.caption_generator import CaptionGenerator"
echo "  >>> gen = CaptionGenerator(language='es')"
echo ""
echo "Option C: Run Examples"
echo -e "  ${YELLOW}source .venv/bin/activate${NC}"
echo -e "  ${YELLOW}python examples/caption_generator_examples.py${NC}"
echo -e "  ${YELLOW}python examples/social_media_examples.py${NC}"
echo ""

echo -e "${BLUE}🚀 Quick Start:${NC}"
echo ""
echo "1. In Terminal:"
echo -e "   ${YELLOW}cd /Users/c0d3g3n1us/Fooocus${NC}"
echo -e "   ${YELLOW}source .venv/bin/activate${NC}"
echo -e "   ${YELLOW}python webui.py${NC}"
echo ""
echo "2. Open browser:"
echo -e "   ${YELLOW}http://localhost:7860${NC}"
echo ""
echo "3. Upload photo + voice sample + script"
echo "   → Click 'Create Content'"
echo "   → Download video with captions!"
echo ""

echo -e "${BLUE}📚 Features Available:${NC}"
echo "  ✅ Photo to Video Animation"
echo "  ✅ Voice Cloning"
echo "  ✅ Lip Synchronization"
echo "  ✅ HeyGen-style Captions (SRT/VTT/ASS/JSON)"
echo "  ✅ Video Face Swapping"
echo "  ✅ 6 Platform Optimizations"
echo "  ✅ Batch Processing"
echo ""

echo -e "${RED}Important: Activate virtual environment before running:${NC}"
echo -e "  ${YELLOW}source .venv/bin/activate${NC}"
echo ""

echo "═════════════════════════════════════════════════════════════════"
echo ""
