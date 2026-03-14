"""Minimal modern Diffusers bridge for Fooocus.

This module provides a lightweight wrapper around HuggingFace Diffusers pipelines.
It is designed to be optional: Fooocus can still run without it.

Usage:
  - Enable via config key `use_diffusers_engine=True` and set `diffusers_model_id`.
  - This will use a small, best-effort pipeline so users can run modern SD/SDXL models.

Note: This is intended as an *upgrade path*. The existing Fooocus pipeline remains
unchanged and is used when Diffusers is unavailable or disabled.
"""

import os
import threading
from typing import Optional, List, Dict

import torch

try:
    from diffusers import (  # type: ignore
        StableDiffusionPipeline,
        StableDiffusionXLImg2ImgPipeline,
        StableDiffusionXLPipeline,
        DPMSolverMultistepScheduler,
        LMSDiscreteScheduler,
        EulerDiscreteScheduler,
        DDIMScheduler,
    )
    DIFFUSERS_AVAILABLE = True
except Exception:
    DIFFUSERS_AVAILABLE = False


# Cache loaded pipelines to avoid re-downloading or reinitializing repeatedly.
_PIPELINES: Dict[str, object] = {}
_PIPELINES_LOCK = threading.Lock()


def _get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def _get_scheduler(name: str):
    name = (name or "").lower()
    if name in ["dpmsolver", "dpmsolver_multistep", "dpmsolver+", "dpmsolver_multistep"]:
        return DPMSolverMultistepScheduler
    if name in ["euler", "euler_discrete"]:
        return EulerDiscreteScheduler
    if name in ["lms", "lms_discrete"]:
        return LMSDiscreteScheduler
    if name in ["ddim"]:
        return DDIMScheduler
    # fallback
    return DPMSolverMultistepScheduler


def _build_pipeline(model_id: str, scheduler_name: str, device: torch.device, torch_dtype: Optional[torch.dtype]):
    """Load or reuse a Diffusers pipeline."""
    global _PIPELINES

    key = f"{model_id}:{scheduler_name}:{device}:{torch_dtype}"
    with _PIPELINES_LOCK:
        if key in _PIPELINES:
            return _PIPELINES[key]

        if not DIFFUSERS_AVAILABLE:
            raise RuntimeError("diffusers is not installed. Install it to use the Diffusers engine.")

        scheduler_cls = _get_scheduler(scheduler_name)

        # Use a generic StableDiffusion pipeline; it should work for most models.
        # For SDXL models, users can provide an SDXL model id (e.g. stabilityai/stable-diffusion-xl-base-1.0).
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            scheduler=scheduler_cls.from_pretrained(model_id),
            torch_dtype=torch_dtype,
            safety_checker=None,
        )

        pipe = pipe.to(device)
        pipe.enable_attention_slicing()
        pipe.enable_model_cpu_offload() if device.type == "cuda" else None
        _PIPELINES[key] = pipe
        return pipe


def generate(
    prompt: str,
    negative_prompt: Optional[str] = None,
    model_id: str = None,
    scheduler_name: str = "dpmsolver",
    width: int = 1024,
    height: int = 1024,
    steps: int = 20,
    guidance_scale: float = 7.5,
    seed: Optional[int] = None,
    device: Optional[str] = None,
    torch_dtype: Optional[torch.dtype] = None,
) -> List:
    """Generate images via Diffusers.

    Returns a list of NumPy images in W,H,C uint8 format (RGB).
    """

    if not DIFFUSERS_AVAILABLE:
        raise RuntimeError("Diffusers is not available in the current environment.")

    if model_id is None:
        raise ValueError("model_id must be provided to use diffusers engine.")

    if device is None:
        device = _get_device().type

    torch_device = torch.device(device)

    if torch_dtype is None:
        torch_dtype = torch.float16 if torch_device.type == "cuda" else torch.float32

    pipe = _build_pipeline(model_id=model_id, scheduler_name=scheduler_name, device=torch_device, torch_dtype=torch_dtype)

    generator = None
    if seed is not None:
        generator = torch.Generator(device=torch_device).manual_seed(seed)

    output = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        width=width,
        height=height,
        num_inference_steps=steps,
        guidance_scale=guidance_scale,
        generator=generator,
    )

    images = output.images
    import numpy as np

    results = []
    for img in images:
        if hasattr(img, "convert"):
            img = img.convert("RGB")
        arr = np.array(img, dtype=np.uint8)
        results.append(arr)

    return results
