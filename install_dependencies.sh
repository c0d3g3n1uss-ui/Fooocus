#!/bin/bash

# ============================================
# FOOOCUS DEPENDENCIES INSTALLATION SCRIPT
# Automatic setup with Conda
# ============================================

set -e

echo "🚀 Fooocus Dependency Installer"
echo "=================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 1. Check if Conda is already installed
echo -e "${BLUE}Checking for Conda installation...${NC}"
if command -v conda &> /dev/null; then
    echo -e "${GREEN}✅ Conda found!${NC}"
    CONDA_PATH=$(which conda)
else
    echo -e "${YELLOW}⚠️  Conda not found. Installing Miniconda...${NC}"
    
    # Detect system architecture
    if [[ $(uname -m) == "arm64" ]]; then
        MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh"
    else
        MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
    fi
    
    echo "Downloading Miniconda..."
    curl -L "$MINICONDA_URL" -o ~/miniconda_installer.sh
    
    echo "Installing Miniconda (this may take a minute)..."
    bash ~/miniconda_installer.sh -b -p $HOME/miniconda3
    
    rm ~/miniconda_installer.sh
    
    # Add conda to PATH
    export PATH="$HOME/miniconda3/bin:$PATH"
    
    echo -e "${GREEN}✅ Miniconda installed!${NC}"
fi

echo ""

# 2. Initialize conda for shell
echo -e "${BLUE}Initializing Conda for current shell...${NC}"
eval "$(conda shell.bash hook)"

echo ""

# 3. Check if environment exists, create if not
if conda env list | grep -q "^fooocus "; then
    echo -e "${YELLOW}🔄 Fooocus environment already exists, updating...${NC}"
    EXISTING="true"
else
    echo -e "${BLUE}Creating fooocus environment with Python 3.10...${NC}"
    conda create -n fooocus python=3.10 pip -y
    EXISTING="false"
fi

echo ""

# 4. Activate environment
echo -e "${BLUE}Activating fooocus environment...${NC}"
conda activate fooocus

echo ""

# 5. Install PyTorch
echo -e "${BLUE}Installing PyTorch (this may take 2-3 minutes)...${NC}"
echo "   → Setting up deep learning framework"

# Try to detect if system has GPU
if command -v nvidia-smi &> /dev/null; then
    echo "   → NVIDIA GPU detected, installing CUDA support"
    conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
else
    echo "   → No NVIDIA GPU detected, installing CPU version"
    conda install pytorch torchvision torchaudio -c pytorch -y
fi

echo -e "${GREEN}✅ PyTorch installed!${NC}"

echo ""

# 6. Install other dependencies
echo -e "${BLUE}Installing additional dependencies...${NC}"
pip install --quiet \
    numpy \
    opencv-python \
    Pillow \
    librosa \
    soundfile \
    transformers \
    scipy \
    tqdm \
    pyyaml \
    gradio \
    accelerate \
    diffusers \
    safetensors

echo -e "${GREEN}✅ All packages installed!${NC}"

echo ""

# 7. Install project requirements
if [ -f "requirements_versions.txt" ]; then
    echo -e "${BLUE}Installing project-specific requirements...${NC}"
    pip install --quiet -r requirements_versions.txt 2>/dev/null || true
    echo -e "${GREEN}✅ Project requirements installed!${NC}"
fi

echo ""

# 8. Verify installation
echo -e "${BLUE}Verifying installation...${NC}"
python << 'VERIFY_EOF'
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
        print(f"  ❌ {name} - FAILED")
        errors.append(name)

if errors:
    print(f"\n⚠️  {len(errors)} package(s) failed to import")
    sys.exit(1)
else:
    print("\n✅ All packages verified!")
VERIFY_EOF

echo ""
echo -e "${GREEN}═════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🎉 Installation Complete!${NC}"
echo -e "${GREEN}═════════════════════════════════════════════════${NC}"
echo ""

echo "Next steps:"
echo "1. In the future, activate the environment with:"
echo -e "   ${YELLOW}conda activate fooocus${NC}"
echo ""
echo "2. Verify Python version:"
echo -e "   ${YELLOW}python --version${NC}"
echo ""
echo "3. Run Fooocus:"
echo -e "   ${YELLOW}python webui.py${NC}"
echo ""
echo "4. To deactivate when done:"
echo -e "   ${YELLOW}conda deactivate${NC}"
echo ""
