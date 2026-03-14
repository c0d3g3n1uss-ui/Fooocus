# ============================================
# CAPTION GENERATOR EXAMPLES
# Auto-generate captions like HeyGen
# ============================================

from modules.caption_generator import (
    CaptionGenerator,
    SubtitleConfig,
    SubtitleFormat,
    CaptionStyle,
    generate_captions_for_video
)
from modules.social_media_creator import SocialMediaContentCreator
from pathlib import Path


def example_1_basic_captioning():
    """
    Example 1: Basic caption generation from video
    Perfect for: Simple caption needs
    """
    print("📝 Example 1: Basic Caption Generation\n")
    
    generator = CaptionGenerator(language='es')
    
    # Extract captions from video
    captions = generator.extract_captions_from_video(
        video_path="my_video.mp4",
        chunk_duration=30.0
    )
    
    if captions:
        print(f"✅ Extracted {len(captions)} captions\n")
        
        # Show first few captions
        for i, caption in enumerate(captions[:3]):
            print(f"{i+1}. [{caption.start_time:.1f}s - {caption.end_time:.1f}s]")
            print(f"   {caption.text}\n")
    else:
        print("❌ No captions extracted")


def example_2_save_srt_format():
    """
    Example 2: Save captions in SRT format (most compatible)
    Perfect for: YouTube, Vimeo, general use
    """
    print("📝 Example 2: Save as SRT (Most Compatible)\n")
    
    generator = CaptionGenerator(language='es')
    captions = generator.extract_captions_from_video("video.mp4")
    
    if captions:
        captions = generator.refine_captions(captions)
        
        config = SubtitleConfig(
            format=SubtitleFormat.SRT,
            language='es'
        )
        
        # Save to SRT file
        success = generator.save_captions(
            captions=captions,
            output_path="captions.srt",
            config=config
        )
        
        if success:
            print("✅ Captions saved to captions.srt")
            print("\nSample SRT content:")
            print(generator.captions_to_srt(captions[:2]))


def example_3_embed_captions_in_video():
    """
    Example 3: Embed captions directly in video (like HeyGen)
    Perfect for: Social media (don't need separate files)
    """
    print("📝 Example 3: Embed Captions in Video\n")
    
    generator = CaptionGenerator(language='es')
    captions = generator.extract_captions_from_video("original_video.mp4")
    
    if captions:
        captions = generator.refine_captions(captions)
        
        config = SubtitleConfig(
            format=SubtitleFormat.SRT,
            style=CaptionStyle.PROFESSIONAL,  # HeyGen-style
            position='bottom',
            font_size=24,
            background_opacity=0.7
        )
        
        # Embed in video
        success = generator.embed_captions_in_video(
            video_path="original_video.mp4",
            captions=captions,
            output_path="video_with_captions.mp4",
            config=config
        )
        
        if success:
            print("✅ Video with embedded captions created")
            print("📹 Output: video_with_captions.mp4")


def example_4_multiple_formats():
    """
    Example 4: Generate captions in multiple formats
    Perfect for: Different video platforms
    """
    print("📝 Example 4: Multiple Formats\n")
    
    generator = CaptionGenerator(language='es')
    captions = generator.extract_captions_from_video("video.mp4")
    
    if captions:
        captions = generator.refine_captions(captions)
        
        formats = {
            'srt': SubtitleFormat.SRT,
            'vtt': SubtitleFormat.VTT,
            'ass': SubtitleFormat.ASS,
            'json': SubtitleFormat.JSON
        }
        
        print("Generating captions in all formats:\n")
        
        for format_name, format_type in formats.items():
            config = SubtitleConfig(format=format_type, language='es')
            output_file = f"captions.{format_name}"
            
            generator.save_captions(captions, output_file, config)
            size = Path(output_file).stat().st_size
            
            print(f"✅ {format_name.upper():<5} → {output_file} ({size} bytes)")


def example_5_multi_language():
    """
    Example 5: Generate captions in multiple languages
    Perfect for: International content
    """
    print("📝 Example 5: Multi-Language Captions\n")
    
    languages = {
        'es': 'Español',
        'en': 'English',
        'fr': 'Français'
    }
    
    for lang_code, lang_name in languages.items():
        print(f"🌍 Generating {lang_name} captions...")
        
        generator = CaptionGenerator(language=lang_code)
        captions = generator.extract_captions_from_video("video.mp4")
        
        if captions:
            captions = generator.refine_captions(captions)
            
            config = SubtitleConfig(
                format=SubtitleFormat.SRT,
                language=lang_code
            )
            
            output_file = f"captions_{lang_code}.srt"
            generator.save_captions(captions, output_file, config)
            
            print(f"   ✅ Saved: {output_file}\n")


def example_6_social_media_with_captions():
    """
    Example 6: Create social media content WITH auto captions
    Perfect for: Professional content creation
    """
    print("📝 Example 6: Social Media Content with Captions\n")
    
    creator = SocialMediaContentCreator(quality='balanced')
    
    # Create with captions
    result = creator.create_content_from_scratch(
        image_path="photo.jpg",
        voice_sample_path="voice.wav",
        script_text="¡Mira esto! Es increíble!",
        platform='tiktok',
        add_captions=True,              # Enable captions
        caption_format='srt',
        caption_embed=False,             # Save separately
        caption_language='es'
    )
    
    if result['status'] == 'success':
        print("✅ Content creation complete!\n")
        print(f"📹 Video: {result['output_video']}")
        print(f"📝 Captions: {result['captions_file']}")
        print(f"📱 Ready for: {result['spec']['description']}")


def example_7_batch_with_captions():
    """
    Example 7: Batch processing with automatic captions
    Perfect for: Content creators with multiple videos
    """
    print("📝 Example 7: Batch Processing with Captions\n")
    
    creator = SocialMediaContentCreator()
    
    # Create scripts.json
    scripts = {
        "photo1.jpg": "Primer video! Espero que te guste.",
        "photo2.jpg": "Así genero contenido con IA.",
        "photo3.jpg": "Sígueme para más!"
    }
    
    import json
    with open('scripts.json', 'w', encoding='utf-8') as f:
        json.dump(scripts, f, ensure_ascii=False)
    
    # Batch create with captions
    results = creator.batch_create_content(
        image_dir="./photos/",
        voice_sample_path="my_voice.wav",
        script_file="scripts.json"
        # Note: Captions are generated automatically
    )
    
    print(f"✅ Created {len(results)} videos with captions\n")
    
    for i, result in enumerate(results, 1):
        video = result.get('output_video', 'N/A')
        captions = result.get('captions_file', 'N/A')
        print(f"{i}. Video: {Path(video).name}")
        print(f"   Captions: {Path(captions).name}\n")


def example_8_quick_caption_generation():
    """
    Example 8: Quick one-liner for caption generation
    Perfect for: Fast processing
    """
    print("📝 Example 8: Quick Caption Generation\n")
    
    # One-liner caption generation
    output = generate_captions_for_video(
        video_path="video.mp4",
        output_format='srt',
        language='es',
        embed=False
    )
    
    if output:
        print(f"✅ Captions generated: {output}")
    else:
        print("❌ Generation failed")


def example_9_caption_styling():
    """
    Example 9: Advanced caption styling (ASS format)
    Perfect for: Professional-looking captions
    """
    print("📝 Example 9: Caption Styling\n")
    
    generator = CaptionGenerator(language='es')
    captions = generator.extract_captions_from_video("video.mp4")
    
    if captions:
        captions = generator.refine_captions(captions)
        
        # Professional styling
        config = SubtitleConfig(
            format=SubtitleFormat.ASS,
            style=CaptionStyle.PROFESSIONAL,
            font_size=28,
            font_color='white',
            background_color='black',
            background_opacity=0.8,
            position='bottom',
            max_chars_per_line=45
        )
        
        generator.save_captions(captions, "captions_styled.ass", config)
        print("✅ Styled captions (ASS format): captions_styled.ass")


def example_10_heygen_comparison():
    """
    Example 10: Show that Fooocus captions match HeyGen quality
    Perfect for: Understanding capabilities
    """
    print("📝 Example 10: HeyGen-Style Caption Generation\n")
    print("=" * 60)
    print("FOOOCUS CAPTION GENERATOR vs HEYGEN")
    print("=" * 60)
    
    comparison = {
        'Feature': ('HeyGen', 'Fooocus'),
        'Auto-generation': ('✅', '✅'),
        'Synchronization': ('✅', '✅'),
        'Multi-language': ('✅', '✅'),
        'Embed in video': ('✅', '✅'),
        'Multiple formats': ('✅', '✅'),
        'Styling options': ('⭐⭐⭐', '⭐⭐⭐⭐'),
        'Cost': ('$$$', '🆓 Free'),
        'Local processing': ('❌', '✅'),
    }
    
    for feature, (heygen, fooocus) in comparison.items():
        print(f"{feature:.<30} HeyGen: {heygen:>7}  Fooocus: {fooocus:>7}")
    
    print("\n" + "=" * 60)
    print("✅ Fooocus has feature parity with HeyGen + more!")
    print("=" * 60)


# ============================================
# MAIN - Run Examples
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("CAPTION GENERATOR - PRACTICAL EXAMPLES")
    print("=" * 60 + "\n")
    
    # Uncomment the example you want to run:
    
    # example_1_basic_captioning()
    # example_2_save_srt_format()
    # example_3_embed_captions_in_video()
    # example_4_multiple_formats()
    # example_5_multi_language()
    # example_6_social_media_with_captions()
    # example_7_batch_with_captions()
    # example_8_quick_caption_generation()
    # example_9_caption_styling()
    # example_10_heygen_comparison()
    
    print("\n✅ To run an example, uncomment it in __main__ section")
    print("=" * 60)
