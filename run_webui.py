#!/usr/bin/env python3
"""
Direct webui launcher - bypasses launch.py requirements
"""

import os
import sys

# Configure environment
root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, root)
os.chdir(root)

os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"
if "GRADIO_SERVER_PORT" not in os.environ:
    os.environ["GRADIO_SERVER_PORT"] = "7865"

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import gradio as gr

print("[Fooocus] Launching WebUI...")
print(f"[Fooocus] Python: {sys.version}")
print(f"[Fooocus] Working directory: {os.getcwd()}")

# Try to import and run webui_demo
try:
    print("[Fooocus] Importing webui_demo module...")
    from webui_demo import create_demo_interface
    
    print("[Fooocus] Creating demo interface...")
    demo = create_demo_interface()
    
    print("[Fooocus] Launching demo...")
    port = int(os.environ.get("GRADIO_SERVER_PORT", 7865))
    print(f"[Fooocus] ✓ WebUI running at http://localhost:{port}")
    
    demo.launch(
        server_name="localhost",
        server_port=port,
        ssl_keyfile=None,
        ssl_certfile=None,
        show_error=True,
        share=False,
        theme=gr.themes.Soft()
    )
except Exception as e:
    print(f"[ERROR] Failed to launch: {type(e).__name__}: {e}")
    print("\n[Fooocus] Attempting fallback mode...")
    
    try:
        import gradio as gr
        
        # Simple fallback demo
        demo = gr.Interface(
            fn=lambda x: f"Echo: {x}",
            inputs="text",
            outputs="text",
            title="Fooocus - Fallback Mode",
            description="System is in fallback mode due to import issues"
        )
        
        demo.launch(
            server_name="localhost",
            server_port=7865
        )
    except Exception as fallback_err:
        print(f"[ERROR] Fallback also failed: {fallback_err}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
