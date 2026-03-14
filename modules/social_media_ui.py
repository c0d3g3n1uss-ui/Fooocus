# ============================================
# SOCIAL MEDIA CREATOR - WEBUI INTEGRATION
# Professional Content Creation Interface
# ============================================

import os
from pathlib import Path
from typing import Tuple, Optional, Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import gradio as gr  # type: ignore
else:
    try:
        import gradio as gr  # type: ignore
    except ImportError:
        gr = None  # type: ignore

try:
    from modules.social_media_creator import SocialMediaContentCreator
except (ImportError, ModuleNotFoundError):
    SocialMediaContentCreator = None  # type: ignore


def create_social_media_ui() -> Optional[Any]:
    """
    Creates Gradio UI for professional social media content creation.
    Integrates with Fooocus WebUI.
    """
    
    if SocialMediaContentCreator is None or gr is None:
        return gr.Markdown("❌ Social Media Creator module not available") if gr else None
    
    with gr.Blocks(title="Social Media Content Creator - Professional Edition") as social_ui:
        gr.Markdown("# 🎬 Professional Social Media Content Creator (Senior V1.0)")
        gr.Markdown(
            """
            ### Create Animated Videos with Your Own Voice
            
            **Complete Workflow:**
            1. 📸 Upload a photo
            2. 🎤 Record your voice (or upload audio)
            3. ✍️ Write your script
            4. 🚀 Generate & optimize for any platform
            
            **Supported Platforms:**
            - ✅ TikTok (vertical, 3-10s)
            - ✅ Instagram Reels (vertical, 3-60s)
            - ✅ YouTube Shorts (vertical, 15-60s)
            - ✅ YouTube (horizontal, full-length)
            - ✅ Facebook (3-120s)
            - ✅ Twitter/X (up to 140s)
            
            **Features:**
            - 🎨 AI photo animation (Grok/Sora-style)
            - 🗣️ Voice cloning from your sample
            - 👄 Automatic lip-sync
            - ⚙️ Platform-optimized rendering
            """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### Input")
                
                # Image upload
                image_input = gr.Image(
                    label="📸 Photo to Animate",
                    type="filepath",
                    info="Upload photo to animate (JPG, PNG, WebP)"
                )
                
                # Voice sample
                voice_sample = gr.Audio(
                    label="🎤 Voice Sample",
                    type="filepath",
                    info="Record or upload voice sample (3-10 seconds)"
                )
                
                # Script input
                script_text = gr.Textbox(
                    label="✍️ Script/Dialog",
                    placeholder="Enter what you want the character to say...",
                    lines=5,
                    max_lines=10,
                    info="What should the animated character say?"
                )
                
                # Platform selection
                platform_select = gr.Radio(
                    choices=["tiktok", "instagram", "youtube_shorts", "youtube", "facebook", "twitter"],
                    value="tiktok",
                    label="🎯 Target Platform",
                    info="Select platform to optimize video for"
                )
                
                # Quality preset
                quality_preset = gr.Radio(
                    choices=["balanced", "ultra_quality", "speed"],
                    value="balanced",
                    label="⚙️ Quality",
                    info="balanced: Best ratio | ultra: Maximum quality | speed: Fastest"
                )
                
            with gr.Column(scale=1):
                gr.Markdown("### Processing")
                
                create_btn = gr.Button(
                    value="🚀 Create Content",
                    variant="primary",
                    size="lg"
                )
                
                progress_output = gr.Textbox(
                    label="📊 Progress",
                    interactive=False,
                    lines=10,
                    max_lines=15,
                    placeholder="Processing status..."
                )
                
                gr.Markdown("### Output")
                
                video_output = gr.File(
                    label="📹 Download Video",
                    interactive=False,
                    info="Your ready-to-upload video"
                )
                
                with gr.Group():
                    gr.Markdown("#### Platform Info")
                    platform_info = gr.Textbox(
                        label="Video Specs",
                        interactive=False,
                        lines=4,
                        placeholder="Platform requirements..."
                    )
                    
                    upload_link = gr.Markdown(
                        "Upload links will appear here after generation"
                    )
        
        # Advanced options (collapsed)
        with gr.Accordion("⚙️ Advanced Options", open=False):
            with gr.Row():
                with gr.Column():
                    voice_emotion = gr.Radio(
                        choices=["neutral", "excited", "calm", "energetic", "dramatic"],
                        value="excited",
                        label="Voice Emotion",
                        info="How should the voice sound?"
                    )
                    
                    speech_speed = gr.Slider(
                        minimum=0.5,
                        maximum=2.0,
                        value=1.0,
                        step=0.1,
                        label="Speech Speed",
                        info="1.0 = normal speed"
                    )
                
                with gr.Column():
                    animation_duration = gr.Slider(
                        minimum=3,
                        maximum=30,
                        value=8,
                        step=1,
                        label="Animation Duration (seconds)",
                        info="How long should the animation be?"
                    )
                    
                    blend_strength = gr.Slider(
                        minimum=0.7,
                        maximum=1.0,
                        value=0.95,
                        step=0.05,
                        label="Face Blend",
                        info="How realistic should the face look?"
                    )
        
        # Captions & Subtitles (HeyGen-style)
        with gr.Accordion("📝 Captions & Subtitles (HeyGen-style)", open=False):
            gr.Markdown(
                """
                ### Auto-Generate Captions from Speech
                Like HeyGen, automatically generate professional captions
                from the audio using AI speech recognition.
                """
            )
            
            with gr.Row():
                with gr.Column():
                    enable_captions = gr.Checkbox(
                        value=True,
                        label="✅ Auto-Generate Captions",
                        info="Enable automatic caption generation like HeyGen"
                    )
                    
                    caption_format = gr.Radio(
                        choices=["srt", "vtt", "ass", "json"],
                        value="srt",
                        label="📋 Subtitle Format",
                        info="srt: Most compatible | vtt: HTML5 | ass: Styled | json: Data"
                    )
                
                with gr.Column():
                    caption_embed = gr.Checkbox(
                        value=False,
                        label="🎬 Embed in Video",
                        info="Embed captions directly in video instead of saving separately"
                    )
                    
                    caption_language = gr.Dropdown(
                        choices=["es", "en", "fr", "de", "it", "pt", "ja", "zh"],
                        value="es",
                        label="🌍 Caption Language",
                        info="Language for speech recognition"
                    )
        
        # Batch processing section
        with gr.Accordion("📦 Batch Processing (Multiple Videos)", open=False):
            gr.Markdown(
                """
                Create videos from multiple photos automatically.
                Requires:
                1. Folder with images
                2. Single voice sample
                3. JSON file with scripts
                """
            )
            
            with gr.Row():
                image_dir = gr.Textbox(
                    label="Image Directory",
                    placeholder="Path to folder with images...",
                    info="Folder containing .jpg/.png files"
                )
                
                script_json = gr.File(
                    label="Scripts JSON",
                    file_count="single",
                    file_types=[".json"],
                    info="JSON with scripts for each image"
                )
            
            batch_btn = gr.Button("🔄 Batch Create")
            batch_output = gr.Textbox(
                label="Batch Results",
                interactive=False,
                lines=8,
                placeholder="Batch results..."
            )
        
        # Event handlers
        def on_image_upload(image):
            """Handle image upload"""
            if image is None:
                return "❌ No image uploaded"
            return f"✅ Image loaded: {Path(image).name}"
        
        def on_voice_upload(audio):
            """Handle voice sample upload"""
            if audio is None:
                return "❌ No voice uploaded"
            return f"✅ Voice sample loaded"
        
        def on_platform_change(platform: str) -> Tuple[str, str]:
            """Update platform info"""
            if SocialMediaContentCreator is None:
                return "Creator not available", ""
            
            creator = SocialMediaContentCreator(quality="balanced")
            spec = creator.PLATFORM_SPECS.get(platform, {})
            
            info = f"""
            **{spec.get('description', '')}**
            • Resolution: {spec.get('resolution', 'N/A')}
            • Duration: {spec.get('duration_min')}-{spec.get('duration_max')}s
            • Bitrate: {spec.get('bitrate', 'N/A')}
            • Format: {spec.get('format', 'N/A')}
            """
            
            upload_links = {
                'tiktok': '📱 Upload to: https://www.tiktok.com/upload',
                'instagram': '📱 Upload to: https://www.instagram.com/create',
                'youtube_shorts': '▶️ Upload to: https://www.youtube.com/shorts/create',
                'youtube': '▶️ Upload to: https://www.youtube.com/upload',
                'facebook': '👍 Upload to: https://www.facebook.com/video/',
                'twitter': '𝕏 Upload to: https://twitter.com/compose/tweet'
            }
            
            return info, upload_links.get(platform, "")
        
        def on_create_click(image: Optional[str], voice_sample: Optional[str], script: str, platform: str, quality: str,
                          emotion: str, speed: float, duration: int, blend: float,
                          enable_captions: bool, caption_format: str, caption_embed: bool,
                          caption_language: str) -> Tuple[str, Optional[str]]:
            """Process content creation"""
            
            if not image:
                return "❌ Please upload an image", None
            if not voice_sample:
                return "❌ Please upload a voice sample", None
            if not script or len(script) < 5:
                return "❌ Please write a script (minimum 5 characters)", None
            
            if SocialMediaContentCreator is None:
                return "❌ Social Media Creator not available", None
            
            try:
                progress = "🔄 Initializing content creator...\n"
                
                creator = SocialMediaContentCreator(quality=quality)
                
                progress += f"📸 Image: {Path(image).name}\n"
                progress += f"🎤 Voice: Uploaded sample\n"
                progress += f"✍️ Script: '{script[:50]}{'...' if len(script) > 50 else ''}'\n"
                progress += f"🎯 Platform: {platform}\n"
                progress += f"⚙️ Quality: {quality}\n"
                progress += f"📝 Captions: {'✅ Yes (' + caption_format + ')' if enable_captions else '❌ No'}\n"
                progress += "-" * 50 + "\n"
                progress += "🔄 Processing...\n"
                
                # Create content with captions
                result = creator.create_content_from_scratch(
                    image_path=image,
                    voice_sample_path=voice_sample,
                    script_text=script,
                    platform=platform,
                    add_captions=enable_captions,
                    caption_format=caption_format,
                    caption_embed=caption_embed,
                    caption_language=caption_language
                )
                
                if result and result.get('status') == 'success':
                    output_file = result.get('output_video')
                    captions_file = result.get('captions_file')
                    
                    if output_file:
                        progress += "✅ Content creation complete!\n"
                        progress += f"📹 Output: {Path(output_file).name}\n"
                        if captions_file:
                            progress += f"📝 Captions: {Path(captions_file).name}\n"
                        progress += f"📊 Platform: {platform}\n"
                        progress += f"💾 Size: {os.path.getsize(output_file) / (1024*1024):.2f} MB\n"
                        progress += "\n🎉 Ready to upload to your platform!"
                        
                        return progress, output_file
                
                return "❌ Content creation failed. Check console.", None
                    
            except Exception as e:
                return f"❌ Error: {str(e)}", None
        
        def on_batch_create(image_dir_path: Optional[str], script_json_file: Optional[str]) -> str:
            """Process batch creation"""
            if not image_dir_path or not script_json_file:
                return "❌ Please provide image directory and script JSON"
            
            if SocialMediaContentCreator is None:
                return "❌ Social Media Creator not available"
            
            try:
                progress = f"🔄 Batch processing started...\n"
                progress += f"📁 Image directory: {image_dir_path}\n"
                progress += f"📄 Scripts: {Path(script_json_file).name}\n"
                progress += "-" * 50 + "\n"
                
                creator = SocialMediaContentCreator()
                
                # Extract voice sample from main inputs (use default if available)
                voice_file = "default_voice.wav"  # Placeholder
                
                results = creator.batch_create_content(
                    image_dir=image_dir_path,
                    voice_sample_path=voice_file,
                    script_file=script_json_file
                )
                
                progress += f"✅ Batch complete!\n"
                progress += f"📊 Videos created: {len(results)}\n"
                
                for idx, result in enumerate(results, 1):
                    output_video = result.get('output_video')
                    if output_video:
                        progress += f"\n{idx}. Platform: {result.get('platform')}\n"
                        progress += f"   Output: {Path(output_video).name}\n"
                
                return progress
                
            except Exception as e:
                return f"❌ Batch error: {str(e)}"
        
        # Connect events
        image_input.upload(
            fn=on_image_upload,
            inputs=image_input,
            outputs=progress_output
        )
        
        voice_sample.upload(
            fn=on_voice_upload,
            inputs=voice_sample,
            outputs=progress_output
        )
        
        platform_select.change(
            fn=on_platform_change,
            inputs=platform_select,
            outputs=[platform_info, upload_link]
        )
        
        create_btn.click(
            fn=on_create_click,
            inputs=[
                image_input,
                voice_sample,
                script_text,
                platform_select,
                quality_preset,
                voice_emotion,
                speech_speed,
                animation_duration,
                blend_strength,
                enable_captions,
                caption_format,
                caption_embed,
                caption_language
            ],
            outputs=[progress_output, video_output]
        )
        
        batch_btn.click(
            fn=on_batch_create,
            inputs=[image_dir, script_json],
            outputs=batch_output
        )
        
        # Initialize with default platform info
        default_platform_info, default_upload_link = on_platform_change("tiktok")
        platform_info.value = default_platform_info
        upload_link.value = default_upload_link
    
    return social_ui


# Export for integration
social_media_creator_interface = create_social_media_ui()

print("[WEBUI] Social Media Creator Interface Created - Senior V1.0")
