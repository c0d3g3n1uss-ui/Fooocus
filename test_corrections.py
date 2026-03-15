#!/usr/bin/env python3
"""Test script to verify code corrections"""

import sys
import os

print("=" * 60)
print("TESTING CORRECTED FILES")
print("=" * 60)
print(f"\nPython version: {sys.version}")
print(f"Python executable: {sys.executable}\n")

# Test 1: Check imports
print("1. Checking module imports...")
deps_status = {}

try:
    import gradio
    deps_status['gradio'] = gradio.__version__
    print(f"   ✓ gradio {gradio.__version__}")
except ImportError:
    deps_status['gradio'] = 'MISSING'
    print("   ✗ gradio: NOT INSTALLED")

try:
    import torch
    deps_status['torch'] = torch.__version__
    print(f"   ✓ torch {torch.__version__}")
except ImportError:
    deps_status['torch'] = 'MISSING'
    print("   ✗ torch: NOT INSTALLED (required for Fooocus)")

try:
    import PIL
    deps_status['PIL'] = PIL.__version__
    print(f"   ✓ PIL {PIL.__version__}")
except:
    deps_status['PIL'] = 'MISSING'

# Test 2: Verify corrected files load
print("\n2. Testing corrected files...")
files_to_test = [
    'build_launcher.py',
    'experiments_mask_generation.py',
    'entry_with_update.py',
    'experiments_expansion.py',
    'experiments_face.py',
    'experiments_interrogate.py'
]

passed = []
failed = []

for fname in files_to_test:
    try:
        with open(fname, 'r') as f:
            compile(f.read(), fname, 'exec')
        print(f"   ✓ {fname}")
        passed.append(fname)
    except SyntaxError as e:
        print(f"   ✗ {fname}: {e}")
        failed.append(fname)

# Test 3: Try loading webui (partial test)
print("\n3. Testing webui.py...")
try:
    with open('webui.py', 'r') as f:
        code = f.read()
    compile(code, 'webui.py', 'exec')
    print("   ✓ webui.py syntax is valid")
    
    # Count changes
    show_progress_count = code.count("show_progress='hidden'") + code.count("show_progress='full'")
    print(f"     - Fixed show_progress parameters: {show_progress_count} occurrences")
except SyntaxError as e:
    print(f"   ✗ webui.py: {e}")
    failed.append('webui.py')

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Files passed: {len(passed)}/{len(files_to_test)}")
print(f"Files failed: {len(failed)}/{len(files_to_test)}")

if failed:
    print(f"\n❌ Failed files: {', '.join(failed)}")
    sys.exit(1)
else:
    print("\n✅ All corrected files have valid Python syntax!")

print("\nDependencies Status:")
if deps_status.get('torch') == 'MISSING':
    print("⚠️  WARNING: torch is not installed")
    print("   Fooocus requires PyTorch to run.")
    print("   Install with: pip install torch")
else:
    print("✓ All critical dependencies available")

print("\nNext steps:")
print("1. Install dependencies: pip install -r requirements_versions.txt")
print("2. Run: python webui.py")
print("=" * 60)
