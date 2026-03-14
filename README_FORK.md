# Fooocus Enhanced Fork by c0d3g3n1us

## 👤 About This Fork

**Developer/Maintainer**: **c0d3g3n1us**

This is an enhanced fork of the original [Fooocus](https://github.com/lllyasviel/Fooocus) project by [lllyasviel](https://github.com/lllyasviel), featuring professional-grade additions for modern AI content creation.

---

## 🌟 What's New in This Fork

### Video & Animation Features
- **Video Face Swapping** - Replace faces in videos while preserving natural motion
- **Photo-to-Video Animation** - Transform static images into smooth video clips using Stable Video Diffusion
- **Motion-Aware Processing** - Advanced algorithms for realistic facial movement

### Voice & Audio
- **Voice Cloning** - Clone any voice using Coqui XTTS_v2
- **Lip Synchronization** - Automatic lip-sync with Wav2Lip technology
- **Multi-language TTS** - Generate speech in multiple languages

### Social Media Integration
- **Content Creator** - Generate complete social media videos from scripts + images
- **Platform Optimization** - Auto-format for TikTok, Instagram, YouTube Shorts, Reels
- **Professional Captions** - HeyGen-style automatic subtitles with Whisper ASR
- **Batch Processing** - Create multiple videos in one pipeline

### Caption Technology
- **Automatic Speech Recognition** - Powered by OpenAI's Whisper
- **Multiple Formats** - SRT, VTT, ASS, JSON subtitle support
- **Professional Styling** - 5 built-in caption styles for different aesthetics
- **Smart Positioning** - Configurable text placement and formatting

---

## 📊 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Image Gen** | Stable Diffusion XL | High-quality base images |
| **Video** | Stable Video Diffusion (SVD) | Animation from images |
| **Face Swap** | RetinaFace + InsightFace | Face detection & replacement |
| **Voice Clone** | Coqui XTTS_v2 | Voice synthesis & cloning |
| **Lip Sync** | Wav2Lip | Audio-visual synchronization |
| **Subtitles** | OpenAI Whisper | Automatic speech recognition |
| **Processing** | OpenCV, LibROSA, ffmpeg | Media pipeline |
| **UI** | Gradio | Web interface |
| **Framework** | Python 3.10+ | Core implementation |

---

## 📦 Installation

### Quick Start
```bash
cd /Users/c0d3g3n1us/Fooocus
bash START.sh
```

### Automated Setup
```bash
bash INSTALL_COMPLETE.sh
```

### Manual Installation
See [MANUAL_INSTALL.md](MANUAL_INSTALL.md) for detailed step-by-step instructions.

---

## 🎯 Project Goals

This fork aims to provide:

✅ **Free Alternative** to paid services like HeyGen, Sora, and commercial AI video tools
✅ **All-in-One Platform** for AI image and video generation
✅ **Professional Quality** output suitable for social media
✅ **Local Processing** - No cloud dependency, complete privacy
✅ **Easy to Use** - Minimal technical knowledge required
✅ **Open Source** - Community-driven development

---

## 💡 Usage Examples

### Generate a Social Media Video
```python
from modules.social_media_creator import SocialMediaContentCreator

creator = SocialMediaContentCreator()
result = creator.create_content_from_scratch(
    image_path="photo.jpg",
    script="Check out this amazing video!",
    voice_name="en_female_1",
    platform="tiktok",
    add_captions=True
)
```

### Generate Captions for Video
```python
from modules.caption_generator import generate_captions_for_video

captions = generate_captions_for_video(
    video_path="video.mp4",
    output_path="captions.srt",
    language="es"
)
```

### Swap Faces in Video
```python
from modules.video_processor import process_video_for_face_swap

process_video_for_face_swap(
    video_path="input.mp4",
    face_image="new_face.jpg",
    output_path="output.mp4"
)
```

See [examples/](examples/) folder for 20+ practical examples.

---

## 📚 Documentation

- [00_LEEME_PRIMERO.md](00_LEEME_PRIMERO.md) - Complete overview and getting started
- [QUICK_START.md](QUICK_START.md) - Fast installation and usage
- [MANUAL_INSTALL.md](MANUAL_INSTALL.md) - Detailed step-by-step setup
- [CAPTIONS_GUIDE.md](CAPTIONS_GUIDE.md) - Caption generation guide
- [SOCIAL_MEDIA_CREATOR_README.md](SOCIAL_MEDIA_CREATOR_README.md) - Social media features
- [VIDEO_FACESWAP_GUIDE.md](VIDEO_FACESWAP_GUIDE.md) - Face swapping tutorial
- [OPTIMIZATION_GUIDE.md](OPTIMIZATION_GUIDE.md) - Performance tuning

---

## 💰 Support & Donations

If this fork has been useful to you, please consider supporting the development. Your donations help ensure:

- 🖥️ Continued development and bug fixes
- 🚀 New features and improvements
- 💻 Server resources for testing
- 📚 Better documentation and examples

### **Donate via PayPal**

**PayPal**: @belakiss
**Minimum**: $20 USD
**Link**: [https://paypal.me/belakiss/20](https://paypal.me/belakiss/20)

---

## 🤝 Contributing

Contributions are welcome! You can help by:

- 🐛 **Reporting bugs** - Found an issue? Let me know
- 💡 **Suggesting features** - Have an idea? Open an issue
- 🔧 **Submitting code** - Create a pull request with improvements
- 📖 **Improving docs** - Help make documentation clearer
- 🌍 **Translations** - Help translate to other languages

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📋 Credits

**Original Project**: [Fooocus](https://github.com/lllyasviel/Fooocus) by [lllyasviel](https://github.com/lllyasviel)

**Enhanced By**: [c0d3g3n1us](https://github.com/c0d3g3n1us)

**Built With**:
- Stable Diffusion community
- Hugging Face Transformers
- Coqui TTS/XTTS
- OpenAI Whisper
- And many other amazing open-source projects

---

## ⚖️ License

This project is open source and available under the same license as the original Fooocus project.

---

## ❓ FAQ

**Q: Is this free?**
A: Yes! Completely free and open source. You only need the hardware to run it locally.

**Q: What are the system requirements?**
A: Minimum 4GB GPU (NVIDIA) + 8GB RAM. Better GPUs = faster processing.

**Q: Can I use this commercially?**
A: Check the license terms. Generally yes for open source usage.

**Q: How do I get help?**
A: Check the documentation, GitHub issues, or contact the developer.

---

## 🌐 Links

- **GitHub**: [github.com/c0d3g3n1us](https://github.com/c0d3g3n1us)
- **PayPal**: [@belakiss](https://paypal.me/belakiss)
- **Original Fooocus**: [github.com/lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus)

---

**Made with ❤️ by c0d3g3n1us**

*Last Updated: March 2026*
