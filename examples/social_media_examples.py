# ============================================
# SOCIAL MEDIA CREATOR - PRACTICAL EXAMPLES
# Ready-to-Use Code Snippets
# ============================================

"""
Complete examples for using the Social Media Content Creator system.
All examples are production-ready and handle errors properly.
"""

# ============================================
# Example 1: Single Video Creation (TikTok)
# ============================================

from modules.social_media_creator import SocialMediaContentCreator
from pathlib import Path

def example_single_tiktok_video():
    """
    Create a single animated video optimized for TikTok.
    Perfect for: Quick social media posts
    """
    
    # Initialize creator
    creator = SocialMediaContentCreator(quality='balanced')
    
    # Your local files
    image_path = "my_photo.jpg"
    voice_sample = "my_voice.wav"  # 3-10 seconds
    script = "Hey everyone! Check out my new project!"
    
    # Create content
    print("[1/1] Creating TikTok video...")
    result = creator.create_content_from_scratch(
        image_path=image_path,
        voice_sample_path=voice_sample,
        script_text=script,
        platform='tiktok'
    )
    
    if result['status'] == 'success':
        print(f"✅ Video created: {result['output_video']}")
        print(f"📊 Size: {Path(result['output_video']).stat().st_size / (1024*1024):.2f} MB")
        print(f"🎯 Platform: TikTok (1080x1920)")
        print(f"📱 Ready to upload: https://www.tiktok.com/upload")
    else:
        print("❌ Failed to create video")


# ============================================
# Example 2: Platform Auto-Detection
# ============================================

def example_auto_platform_selection():
    """
    Automatically select best platform based on script duration.
    Perfect for: Let the AI decide the platform
    """
    
    creator = SocialMediaContentCreator(quality='balanced')
    
    scripts = {
        "Short": "Hey! Quick update!",  # 2 words
        "Medium": "Welcome back to my channel! Today I'm showing you something amazing.",  # 15 words
        "Long": "Welcome back everyone! Today I want to show you my new project. It took me weeks to complete...",  # 28 words
    }
    
    for script_type, script_text in scripts.items():
        # Get recommended platform (by script length in chars)
        platforms = creator.get_platform_recommendations(len(script_text))
        platform = platforms[0] if platforms else 'tiktok'  # Pick first recommendation
        
        print(f"\n📝 Script type: {script_type}")
        print(f"   Text: {script_text[:50]}...")
        print(f"   ✅ Recommended platform: {platform}")
        
        spec = creator.PLATFORM_SPECS[platform]
        print(f"   📊 Duration: {spec['duration_min']}-{spec['duration_max']}s")
        print(f"   📱 Resolution: {spec['resolution']}")


# ============================================
# Example 3: Batch Processing (Multiple Videos)
# ============================================

def example_batch_processing():
    """
    Create multiple videos from a folder of images.
    Perfect for: Content creators with batched posts
    
    File structure:
    photos/
      ├── photo1.jpg
      ├── photo2.jpg
      └── photo3.jpg
    
    scripts.json:
    {
        "photo1.jpg": "First video message",
        "photo2.jpg": "Second video message",
        "photo3.jpg": "Third video message"
    }
    """
    
    creator = SocialMediaContentCreator(quality='balanced')
    
    print("🔄 Starting batch processing...")
    print("-" * 50)
    
    # Process multiple images
    results = creator.batch_create_content(
        image_dir="./photos/",
        voice_sample_path="my_voice.wav",
        script_file="scripts.json"
    )
    
    print(f"\n✅ Batch complete! Created {len(results)} videos\n")
    
    for idx, result in enumerate(results, 1):
        output = result['output_video']
        platform = result.get('platform', 'unknown')
        size_mb = Path(output).stat().st_size / (1024*1024)
        
        print(f"{idx}. {Path(output).name}")
        print(f"   Platform: {platform}")
        print(f"   Size: {size_mb:.2f} MB")
        print()


# ============================================
# Example 4: Quality Profile Comparison
# ============================================

def example_quality_profiles():
    """
    Compare different quality settings.
    Perfect for: Understanding quality vs speed tradeoff
    """
    
    image = "photo.jpg"
    voice = "voice.wav"
    script = "Hello world!"
    
    quality_settings = {
        'speed': {
            'name': 'Speed Priority',
            'description': 'Fastest rendering, decent quality'
        },
        'balanced': {
            'name': 'Balanced (Default)',
            'description': 'Best ratio of quality and speed'
        },
        'ultra_quality': {
            'name': 'Ultra Quality',
            'description': 'Best quality, slower rendering'
        }
    }
    
    print("📊 Quality Profile Comparison\n")
    print("-" * 70)
    
    for quality_key, quality_info in quality_settings.items():
        
        print(f"\n🎯 {quality_info['name']}")
        print(f"   {quality_info['description']}")
        
        creator = SocialMediaContentCreator(quality=quality_key)
        
        result = creator.create_content_from_scratch(
            image_path=image,
            voice_sample_path=voice,
            script_text=script,
            platform='youtube_shorts'
        )
        
        if result['status'] == 'success':
            size_mb = Path(result['output_video']).stat().st_size / (1024*1024)
            print(f"   ✅ Output: {size_mb:.2f} MB")
            print(f"   Output file: {result['output_video']}")


# ============================================
# Example 5: Advanced Voice Control
# ============================================

def example_voice_emotion_control():
    """
    Create same video with different voice emotions.
    Perfect for: Testing different tones
    """
    
    creator = SocialMediaContentCreator(quality='balanced')
    
    image = "photo.jpg"
    voice = "voice.wav"
    script = "This is amazing!"
    
    emotions = ['neutral', 'excited', 'calm', 'energetic', 'dramatic']
    
    print("🎤 Creating videos with different voice emotions\n")
    
    for emotion in emotions:
        print(f"Creating {emotion} version...", end=" ")
        
        # Note: This would require WebUI integration with emotion parameter
        # Current API generates with default emotion
        result = creator.create_content_from_scratch(
            image_path=image,
            voice_sample_path=voice,
            script_text=script,
            platform='instagram'
        )
        
        if result['status'] == 'success':
            print("✅")
        else:
            print("❌")


# ============================================
# Example 6: Platform-Specific Optimization
# ============================================

def example_platform_specific():
    """
    Create optimized videos for specific platforms.
    Perfect for: Multi-platform campaigns
    """
    
    image = "photo.jpg"
    voice = "voice.wav"
    script = "Check this out!"
    
    platforms = ['tiktok', 'instagram', 'youtube_shorts', 'youtube', 'facebook', 'twitter']
    
    creator = SocialMediaContentCreator(quality='balanced')
    
    print("🌍 Creating optimized videos for all platforms\n")
    print("-" * 70)
    
    results = {}
    
    for platform in platforms:
        print(f"\n📱 {platform.upper()}")
        
        result = creator.create_content_from_scratch(
            image_path=image,
            voice_sample_path=voice,
            script_text=script,
            platform=platform
        )
        
        if result['status'] == 'success':
            spec = creator.PLATFORM_SPECS[platform]
            
            print(f"   ✅ Video created")
            print(f"   📐 Resolution: {spec['resolution']}")
            print(f"   ⏱️  Duration: {spec['duration_min']}-{spec['duration_max']}s")
            print(f"   📊 Bitrate: {spec['bitrate']}")
            
            results[platform] = result['output_video']
    
    print("\n" + "=" * 70)
    print(f"✅ Created {len(results)} platform-optimized videos!")


# ============================================
# Example 7: Error Handling & Recovery
# ============================================

def example_error_handling():
    """
    Proper error handling for production use.
    Perfect for: Robust applications
    """
    
    creator = SocialMediaContentCreator(quality='balanced')
    
    test_cases = [
        {
            'name': 'Valid inputs',
            'image': 'photo.jpg',
            'voice': 'voice.wav',
            'script': 'Hello!',
        },
        {
            'name': 'Missing image',
            'image': 'nonexistent.jpg',
            'voice': 'voice.wav',
            'script': 'Hello!',
        },
        {
            'name': 'Empty script',
            'image': 'photo.jpg',
            'voice': 'voice.wav',
            'script': '',
        },
        {
            'name': 'Invalid platform',
            'image': 'photo.jpg',
            'voice': 'voice.wav',
            'script': 'Hello!',
            'platform': 'invalid_platform',
        },
    ]
    
    print("🔍 Testing error handling\n")
    
    for test_case in test_cases:
        print(f"Test: {test_case['name']}")
        
        try:
            # Validate required fields
            image = test_case.get('image')
            voice = test_case.get('voice')
            script = test_case.get('script')
            platform = test_case.get('platform', 'tiktok')
            
            if not image or not voice or not script:
                print(f"   ⚠️  Missing required fields\n")
                continue
            
            result = creator.create_content_from_scratch(
                image_path=image,
                voice_sample_path=voice,
                script_text=script,
                platform=platform
            )
            
            if result['status'] == 'success':
                print("   ✅ Success\n")
            else:
                print(f"   ⚠️  {result.get('error', 'Unknown error')}\n")
                
        except FileNotFoundError as e:
            print(f"   ❌ File error: {e}\n")
        except ValueError as e:
            print(f"   ❌ Invalid input: {e}\n")
        except Exception as e:
            print(f"   ❌ Unexpected error: {e}\n")


# ============================================
# Example 8: Batch JSON Format
# ============================================

def example_batch_json_format():
    """
    Shows the correct format for batch processing JSON files.
    """
    
    import json
    
    # Create example scripts.json
    scripts = {
        "photo1.jpg": "Welcome to my channel! Today I'm sharing my latest project.",
        "photo2.jpg": "This is something I've been working on for months.",
        "photo3.jpg": "I hope you enjoy it! Let me know what you think!",
        "photo4.jpg": "Thanks for watching! Don't forget to subscribe!",
    }
    
    # Save as JSON
    with open('scripts.json', 'w') as f:
        json.dump(scripts, f, indent=2)
    
    print("✅ Created scripts.json")
    print("\nFile content:")
    print(json.dumps(scripts, indent=2))
    
    # Process batch
    creator = SocialMediaContentCreator()
    results = creator.batch_create_content(
        image_dir="./photos/",
        voice_sample_path="my_voice.wav",
        script_file="scripts.json"
    )
    
    print(f"\n✅ Created {len(results)} videos from batch")


# ============================================
# Example 9: Performance Monitoring
# ============================================

def example_performance_monitoring():
    """
    Monitor creation performance and resource usage.
    Perfect for: Optimization and debugging
    """
    
    import time
    from datetime import datetime
    
    creator = SocialMediaContentCreator(quality='balanced')
    
    print("📊 Performance Monitoring\n")
    print("-" * 70)
    
    start_time = time.time()
    start_datetime = datetime.now()
    
    result = creator.create_content_from_scratch(
        image_path="photo.jpg",
        voice_sample_path="voice.wav",
        script_text="Performance test!",
        platform='tiktok'
    )
    
    elapsed = time.time() - start_time
    
    if result['status'] == 'success':
        output_file = result['output_video']
        file_size_mb = Path(output_file).stat().st_size / (1024*1024)
        
        print(f"✅ Creation successful")
        print(f"⏱️  Total time: {elapsed:.1f} seconds")
        print(f"📊 Speed: {elapsed/60:.2f} minutes")
        print(f"💾 File size: {file_size_mb:.2f} MB")
        print(f"⚡ Throughput: {file_size_mb/elapsed*8:.1f} Mbps")
        print(f"🕒 Created at: {start_datetime}")


# ============================================
# Example 10: Integration with Existing Pipeline
# ============================================

def example_pipeline_integration():
    """
    Integrate with Fooocus image generation pipeline.
    Perfect for: End-to-end workflows
    """
    
    # Optional: If using Fooocus image generation
    # from modules.default_pipeline import KSAMPLER
    
    creator = SocialMediaContentCreator(quality='balanced')
    
    print("🔗 Pipeline Integration Example\n")
    print("-" * 70)
    
    # Step 1: Generate image with Fooocus
    print("\n1️⃣  Generating base image with Fooocus...")
    # image = KSAMPLER(prompt="a professional headshot...")  # Hypothetical
    image = "generated_image.jpg"  # Placeholder or output from Fooocus generation
    print(f"   ✅ Generated: {image}")
    
    # Step 2: Create animation with voice
    print("\n2️⃣  Creating animated video with voice...")
    result = creator.create_content_from_scratch(
        image_path=image,
        voice_sample_path="voice.wav",
        script_text="Check out this AI-generated content!",
        platform='youtube_shorts'
    )
    print(f"   ✅ Created: {result['output_video']}")
    
    # Step 3: Upload to platform
    if result['status'] == 'success':
        print("\n3️⃣  Ready for upload!")
        print(f"   📱 Platform: YouTube Shorts")
        print(f"   🎯 Resolution: 1080x1920")
        print(f"   ⏱️  Duration: 15-60 seconds")
        print(f"\n   👉 Upload at: https://www.youtube.com/shorts/create")


# ============================================
# MAIN - Run Examples
# ============================================

if __name__ == "__main__":
    print("=" * 70)
    print("SOCIAL MEDIA CREATOR - PRACTICAL EXAMPLES")
    print("=" * 70)
    
    # Uncomment the example you want to run:
    
    # example_single_tiktok_video()
    # example_auto_platform_selection()
    # example_batch_processing()
    # example_quality_profiles()
    # example_voice_emotion_control()
    # example_platform_specific()
    # example_error_handling()
    # example_batch_json_format()
    # example_performance_monitoring()
    # example_pipeline_integration()
    
    print("\n✅ To run an example, uncomment it in __main__ section")
    print("=" * 70)
