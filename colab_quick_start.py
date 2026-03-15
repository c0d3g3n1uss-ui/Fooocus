#!/usr/bin/env python3
"""
QUICK START: Fooocus Enhanced on Google Colab
Copy-paste this into a Colab cell for instant setup
"""

# ============================================================
# 🚀 QUICK COLAB LAUNCHER - Single Cell Setup
# ============================================================
# Just paste this entire code block into ONE Colab cell and run!
# It handles everything: install, clone, and launch

import os
import subprocess

def colab_quick_start():
    print("=" * 70)
    print("🎨 FOOOCUS ENHANCED - COLAB QUICK START")
    print("=" * 70)
    print()
    
    # Step 1: Install dependencies
    print("📦 [1/4] Installing dependencies...")
    subprocess.run(
        ["pip", "install", "-q", "pyngrok", "pygit2==1.15.1", "gradio==6.9.0"],
        capture_output=True
    )
    print("     ✅ Dependencies installed\n")
    
    # Step 2: Clone repository
    print("📁 [2/4] Cloning Fooocus Enhanced...")
    workspace = "/content/Fooocus_Enhanced"
    
    if os.path.exists(workspace):
        subprocess.run(["rm", "-rf", workspace], capture_output=True)
    
    result = subprocess.run(
        ["git", "clone", "https://github.com/c0d3g3n1us/Fooocus.git", workspace],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"     ✅ Repository cloned to {workspace}\n")
    else:
        print(f"     ❌ Clone failed: {result.stderr}\n")
        return False
    
    os.chdir(workspace)
    
    # Step 3: Create launcher
    print("⚙️  [3/4] Setting up launcher...")
    
    launcher_code = '''
import os, sys, subprocess, gradio as gr
from webui_demo import create_demo_interface

os.environ["GRADIO_SERVER_PORT"] = "7865"
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

print("[Fooocus] Creating interface...")
demo = create_demo_interface()

try:
    import pyngrok
    from pyngrok import ngrok
    tunnel = ngrok.connect(7865, "http")
    print(f"\\n[Fooocus] 🔗 PUBLIC URL: {tunnel.public_url}")
    print("[Fooocus] ✅ Keep this tab open!\\n")
except:
    print("[Fooocus] ngrok not available - using local only\\n")

demo.launch(server_name="0.0.0.0", server_port=7865, share=False, theme=gr.themes.Soft())
'''
    
    with open("launch_colab_quick.py", "w") as f:
        f.write(launcher_code)
    
    print("     ✅ Launcher ready\n")
    
    # Step 4: Launch server
    print("🚀 [4/4] Starting Fooocus Enhanced...\n")
    print("-" * 70)
    
    subprocess.run(["python", "launch_colab_quick.py"])

# Run it!
if __name__ == "__main__":
    colab_quick_start()
