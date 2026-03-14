# ============================================
# VIDEO FACE SWAP - WEBUI INTEGRATION
# Senior Development Enhancement (V1.0)
# ============================================

import os
from pathlib import Path

try:
    import gradio as gr  # type: ignore
except ImportError:
    gr = None  # type: ignore

from modules.video_processor import (
    process_video_face_swap
)


def create_video_swap_interface():
    """
    Creates Gradio UI for video face swapping.
    Integrates with Fooocus WebUI.
    Returns None if Gradio is not installed.
    """
    
    if gr is None:
        print("[WEBUI] ⚠️  Gradio not installed. Video Face Swap interface unavailable.")
        return None
    
    with gr.Blocks(title="Video Face Swap - Professional Edition") as video_swap_ui:
        gr.Markdown("# 🎬 Professional Video Face Swap (Senior V1.0)")
        gr.Markdown(
            """
            ### Advanced Video Face Morphing with Motion Preservation
            
            **Features:**
            - ✅ Change face & physiognomy while preserving natural movement
            - ✅ Optical flow-based motion tracking
            - ✅ Smooth blending & quality preservation
            - ✅ Support for any video format (MP4, AVI, MOV, etc.)
            - ✅ Batch processing for efficiency
            
            **Workflow:**
            1. Upload video file (any format)
            2. Upload target face image
            3. Configure quality & blend settings
            4. Process → Download result
            """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### Input")
                
                video_input = gr.File(
                    label="Upload Video",
                    type="filepath",
                    accept_video=True,
                    info="Select video file (MP4, AVI, MOV, MKV, etc.)"
                )
                
                target_face_input = gr.Image(
                    label="Target Face",
                    type="filepath",
                    info="Upload source face to swap onto video"
                )
                
                with gr.Group():
                    gr.Markdown("#### Quality Settings")
                    
                    quality_preset = gr.Radio(
                        choices=["balanced", "ultra_quality", "speed"],
                        value="balanced",
                        label="Quality Preset",
                        info="balanced: Best ratio | ultra_quality: Maximum detail | speed: Fastest"
                    )
                    
                    blend_strength = gr.Slider(
                        minimum=0.0,
                        maximum=1.0,
                        value=0.95,
                        step=0.05,
                        label="Blend Strength",
                        info="How much of target face to show (0=original, 1=full swap)"
                    )
                    
                    preserve_motion = gr.Checkbox(
                        value=True,
                        label="Preserve Motion",
                        info="Use optical flow to maintain natural movement"
                    )
                
                with gr.Group():
                    gr.Markdown("#### Advanced Options")
                    
                    start_frame = gr.Number(
                        value=0,
                        label="Start Frame",
                        info="Frame number to begin processing"
                    )
                    
                    end_frame = gr.Number(
                        value=-1,
                        label="End Frame",
                        info="-1 for entire video"
                    )
                    
                    output_format = gr.Radio(
                        choices=["mp4", "avi", "mov"],
                        value="mp4",
                        label="Output Format",
                        info="Video format for result"
                    )
            
            with gr.Column(scale=1):
                gr.Markdown("### Processing")
                
                process_btn = gr.Button(
                    value="🚀 Process Video",
                    variant="primary",
                    size="lg"
                )
                
                progress_output = gr.Textbox(
                    label="Progress",
                    interactive=False,
                    lines=8,
                    max_lines=12,
                    placeholder="Processing status will appear here..."
                )
                
                gr.Markdown("### Output")
                
                video_output = gr.File(
                    label="Download Result",
                    interactive=False,
                    info="Your processed video will appear here"
                )
                
                with gr.Group():
                    gr.Markdown("#### Video Information")
                    video_info = gr.Textbox(
                        label="Video Details",
                        interactive=False,
                        lines=5,
                        placeholder="Video info will appear after upload..."
                    )
        
        # Event handlers
        def on_video_upload(video_file):
            """Handle video file upload"""
            if video_file is None:
                return "❌ No video uploaded", ""
            
            try:
                from modules.video_processor import VideoMetadata
                
                meta = VideoMetadata(video_file)
                info_text = meta.info()
                meta.release()
                
                return f"✅ Video loaded: {Path(video_file).name}", info_text
            except Exception as e:
                return f"❌ Error loading video: {str(e)}", ""
        
        def on_target_face_upload(image):
            """Handle target face upload"""
            if image is None:
                return "❌ No face image uploaded"
            return f"✅ Target face loaded"
        
        def on_process_click(video_file, target_face, quality, blend, preserve_motion_enabled, 
                            start_frame_num, end_frame_num, output_fmt):
            """Process video with face swap"""
            
            # Validation
            if not video_file:
                return "❌ Please upload a video file", None
            if target_face is None:
                return "❌ Please upload a target face image", None
            
            try:
                progress_text = "🔄 Initializing video processor...\n"
                
                # Convert gradio image to filepath if needed
                target_face_path = target_face if isinstance(target_face, str) else target_face.name
                
                # Generate output path
                base_name = Path(video_file).stem
                output_path = f"{base_name}_swapped_senior_v1.{output_fmt}"
                
                progress_text += f"📹 Processing: {Path(video_file).name}\n"
                progress_text += f"👤 Target face: {Path(target_face_path).name}\n"
                progress_text += f"⚙️  Quality: {quality}\n"
                progress_text += f"🎨 Blend: {blend*100:.0f}%\n"
                progress_text += f"🎬 Motion preserve: {preserve_motion_enabled}\n"
                progress_text += "-" * 50 + "\n"
                
                # Process video
                end_frame_actual = None if end_frame_num < 0 else int(end_frame_num)
                
                success = process_video_face_swap(
                    video_path=video_file,
                    target_face_path=target_face_path,
                    output_path=output_path,
                    quality_level=quality,
                    blend_strength=blend
                )
                
                if success and os.path.exists(output_path):
                    progress_text += "✅ Processing complete!\n"
                    progress_text += f"📁 Output: {output_path}\n"
                    progress_text += f"📊 Size: {os.path.getsize(output_path) / (1024*1024):.2f} MB"
                    
                    return progress_text, output_path
                else:
                    progress_text += "❌ Processing failed. Check logs."
                    return progress_text, None
                    
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}\n\nCheck console for details."
                return error_msg, None
        
        # Connect events
        video_input.upload(
            fn=on_video_upload,
            inputs=video_input,
            outputs=[progress_output, video_info]
        )
        
        target_face_input.upload(
            fn=on_target_face_upload,
            inputs=target_face_input,
            outputs=progress_output
        )
        
        process_btn.click(
            fn=on_process_click,
            inputs=[
                video_input,
                target_face_input,
                quality_preset,
                blend_strength,
                preserve_motion,
                start_frame,
                end_frame,
                output_format
            ],
            outputs=[progress_output, video_output]
        )
    
    return video_swap_ui


# Export for integration - only create if Gradio is available
try:
    video_face_swap_interface = create_video_swap_interface()
    if video_face_swap_interface is not None:
        print("[WEBUI] Video Face Swap Interface Created - Senior V1.0")
    else:
        video_face_swap_interface = None
except Exception as e:
    print(f"[WEBUI] ⚠️  Error creating Video Face Swap interface: {e}")
    video_face_swap_interface = None
