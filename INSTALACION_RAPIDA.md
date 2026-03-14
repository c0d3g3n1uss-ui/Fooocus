# 🔧 GUÍA RÁPIDA DE INSTALACIÓN

**Los paquetes en rojo en VS Code se pueden ignorar por ahora.** Aquí cómo instalarlos en 2 minutos:

## Opción más fácil: Copiar y pegar en Terminal

```bash
# 1. Ve a la carpeta del proyecto
cd ~/Fooocus

# 2. Instala Miniconda si no lo tienes
curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda.sh && bash ~/miniconda.sh -b -p ~/miniconda3 && rm ~/miniconda.sh

# 3. Agrega conda al PATH (IMPORTANTE)
export PATH="~/miniconda3/bin:$PATH"

# 4. Crea un entorno con Python 3.10
~/miniconda3/bin/conda create -n fooocus python=3.10 pip -y

# 5. Activa el entorno
source ~/miniconda3/bin/activate fooocus

# 6. Instala todos los paquetes
pip install torch numpy opencv-python Pillow librosa soundfile transformers scipy tqdm pyyaml gradio accelerate diffusers safetensors

# ✅ ¡Listo!
python --version  # Deberà mostrar Python 3.10
```

## Después de instalar: Cómo usar

**Cada vez que abras un terminal:**
```bash
source ~/miniconda3/bin/activate fooocus
python webui.py
```

**Para salir:**
```bash
conda deactivate
```

---

**En VS Code:**
1. Abre Command Palette (Cmd + Shift + P)
2. Busca "Python: Select Interpreter"
3. Elige el que diga "fooocus" o apunta a `~/miniconda3/envs/fooocus/bin/python`

¡Eso es! Los errores en rojo desaparecerán.
