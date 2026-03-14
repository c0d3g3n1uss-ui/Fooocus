# ============================================
# CAPTION & SUBTITLE GENERATOR
# Auto-generate captions like HeyGen
# 
# Features:
# - Auto speech-to-text (ASR)
# - Multi-language support
# - Timestamp synchronization
# - Multiple subtitle formats (SRT, VTT, ASS)
# - Styling and positioning
# ============================================

from typing import Optional, List, TYPE_CHECKING
from pathlib import Path
import json
import os
from dataclasses import dataclass
from enum import Enum

if TYPE_CHECKING:
    import numpy as np  # type: ignore
else:
    try:
        import numpy as np  # type: ignore
    except ImportError:
        np = None  # type: ignore

try:
    import librosa  # type: ignore
    import soundfile as sf  # type: ignore
except ImportError:
    librosa = None  # type: ignore
    sf = None  # type: ignore

try:
    from transformers import pipeline  # type: ignore
    has_transformers = True
except ImportError:
    has_transformers = False


class SubtitleFormat(str, Enum):
    """Supported subtitle formats"""
    SRT = "srt"      # SubRip (most compatible)
    VTT = "vtt"      # WebVTT (HTML5)
    ASS = "ass"      # Advanced SubStation Alpha (styling)
    JSON = "json"    # JSON (custom)


class CaptionStyle(str, Enum):
    """Caption styling presets"""
    DEFAULT = "default"       # White text, black background
    MODERN = "modern"         # Bold, centered
    MINIMAL = "minimal"       # Small, unobtrusive
    VIBRANT = "vibrant"       # Colored text
    PROFESSIONAL = "professional"  # Like HeyGen


@dataclass
class Caption:
    """Single caption entry"""
    start_time: float  # seconds
    end_time: float    # seconds
    text: str
    speaker: Optional[str] = None
    confidence: float = 1.0


@dataclass
class SubtitleConfig:
    """Configuration for subtitle generation"""
    format: SubtitleFormat = SubtitleFormat.SRT
    style: CaptionStyle = CaptionStyle.PROFESSIONAL
    language: str = "es"  # Spanish by default
    auto_detect: bool = True
    add_speaker_name: bool = True
    max_chars_per_line: int = 42
    position: str = "bottom"  # bottom, top, center
    font_size: int = 24
    font_color: str = "white"
    background_color: str = "black"
    background_opacity: float = 0.7


class CaptionGenerator:
    """
    Generate captions from audio using automatic speech recognition.
    Inspired by HeyGen's caption system.
    """
    
    def __init__(self, language: str = "es", device: str = "cuda"):
        """
        Initialize caption generator.
        
        Args:
            language: Language code ('es', 'en', 'fr', 'de', 'it', 'pt', 'ja', 'zh')
            device: 'cuda' or 'cpu'
        """
        self.language = language
        self.device = device
        self.asr_model = None
        self.supported_languages = {
            'es': 'Spanish',
            'en': 'English',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'pt': 'Portuguese',
            'ja': 'Japanese',
            'zh': 'Chinese'
        }
        
        self._init_asr()
    
    def _init_asr(self) -> None:
        """Initialize Automatic Speech Recognition model"""
        print(f"[CAPTION] Initializing ASR for {self.supported_languages.get(self.language, 'Unknown')}...")
        
        if not has_transformers:
            print("[CAPTION] ⚠️  transformers not installed. Install: pip install transformers torch")
            return
        
        try:
            # Use Whisper-style model or Wav2Vec2
            model_name = f"openai/whisper-small"
            self.asr_model = pipeline(
                "automatic-speech-recognition",
                model=model_name,
                device=0 if self.device == "cuda" else -1
            )
            print("[CAPTION] ✅ ASR model loaded")
        except Exception as e:
            print(f"[CAPTION] ❌ ASR initialization failed: {e}")
            self.asr_model = None
    
    def extract_captions_from_audio(self,
                                   audio_path: str,
                                   chunk_duration: float = 30.0) -> Optional[List[Caption]]:
        """
        Extract captions from audio file using ASR.
        
        Args:
            audio_path: Path to audio file
            chunk_duration: Process audio in chunks (seconds)
            
        Returns:
            List of Caption objects or None if failed
        """
        if not os.path.exists(audio_path):
            print(f"[CAPTION] ❌ Audio file not found: {audio_path}")
            return None
        
        if self.asr_model is None:
            print("[CAPTION] ❌ ASR model not initialized")
            return None
        
        if librosa is None:
            print("[CAPTION] ❌ librosa not available")
            return None
        
        try:
            print(f"[CAPTION] 🔄 Extracting captions from {Path(audio_path).name}...")
            
            # Load audio
            y, sr = librosa.load(audio_path, sr=16000)
            duration = len(y) / sr
            
            captions: List[Caption] = []
            
            # Process in chunks
            num_chunks = int(duration / chunk_duration) + 1
            
            for chunk_idx in range(num_chunks):
                start_sample = int(chunk_idx * chunk_duration * sr)
                end_sample = int((chunk_idx + 1) * chunk_duration * sr)
                
                audio_chunk = y[start_sample:end_sample]
                start_time = chunk_idx * chunk_duration
                
                # Transcribe chunk
                result = self.asr_model(audio_chunk)
                text = result.get('text', '').strip()
                
                if text:
                    # Estimate end time based on chunk
                    end_time = min((chunk_idx + 1) * chunk_duration, duration)
                    
                    caption = Caption(
                        start_time=start_time,
                        end_time=end_time,
                        text=text,
                        confidence=result.get('confidence', 1.0)
                    )
                    captions.append(caption)
                    
                    progress = f"[{chunk_idx + 1}/{num_chunks}] {text[:50]}..."
                    print(f"[CAPTION] {progress}")
            
            print(f"[CAPTION] ✅ Extracted {len(captions)} captions")
            return captions
        
        except Exception as e:
            print(f"[CAPTION] ❌ Extraction failed: {e}")
            return None
    
    def extract_captions_from_video(self,
                                   video_path: str,
                                   chunk_duration: float = 30.0) -> Optional[List[Caption]]:
        """
        Extract captions from video by first extracting audio.
        
        Args:
            video_path: Path to video file
            chunk_duration: Process audio in chunks
            
        Returns:
            List of Caption objects
        """
        if not os.path.exists(video_path):
            print(f"[CAPTION] ❌ Video file not found: {video_path}")
            return None
        
        try:
            import cv2  # type: ignore
            
            print(f"[CAPTION] 🎬 Extracting audio from video...")
            
            # Extract audio from video
            cap = cv2.VideoCapture(video_path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # Use ffmpeg to extract audio
            audio_path = "/tmp/extracted_audio.wav"
            os.system(f"ffmpeg -i '{video_path}' -q:a 9 -n '{audio_path}' 2>/dev/null")
            
            if not os.path.exists(audio_path):
                print("[CAPTION] ❌ Audio extraction failed")
                return None
            
            # Extract captions from extracted audio
            captions = self.extract_captions_from_audio(audio_path, chunk_duration)
            
            # Cleanup
            os.remove(audio_path)
            
            return captions
        
        except Exception as e:
            print(f"[CAPTION] ❌ Video processing failed: {e}")
            return None
    
    def refine_captions(self, captions: List[Caption]) -> List[Caption]:
        """
        Refine captions by merging short segments and adjusting timing.
        
        Args:
            captions: List of original captions
            
        Returns:
            Refined caption list
        """
        if not captions:
            return []
        
        refined: List[Caption] = []
        
        for caption in captions:
            # Skip very short captions
            if len(caption.text.split()) < 2:
                if refined:
                    # Merge with previous
                    refined[-1].text += " " + caption.text
                    refined[-1].end_time = caption.end_time
                continue
            
            refined.append(caption)
        
        return refined
    
    def format_time(self, seconds: float, format_type: SubtitleFormat) -> str:
        """
        Format time for subtitle format.
        
        Args:
            seconds: Time in seconds
            format_type: Subtitle format (SRT, VTT, etc.)
            
        Returns:
            Formatted time string
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        millis = int((secs % 1) * 1000)
        secs = int(secs)
        
        if format_type in [SubtitleFormat.SRT, SubtitleFormat.VTT]:
            return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
        elif format_type == SubtitleFormat.ASS:
            # ASS format: H:MM:SS.CS (centiseconds)
            centis = int((secs % 1) * 100)
            return f"{hours}:{minutes:02d}:{secs:02d}.{centis:02d}"
        else:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    
    def captions_to_srt(self, captions: List[Caption]) -> str:
        """Convert captions to SRT format"""
        srt_content = ""
        
        for idx, caption in enumerate(captions, 1):
            start = self.format_time(caption.start_time, SubtitleFormat.SRT)
            end = self.format_time(caption.end_time, SubtitleFormat.SRT)
            
            srt_content += f"{idx}\n"
            srt_content += f"{start} --> {end}\n"
            srt_content += f"{caption.text}\n"
            srt_content += "\n"
        
        return srt_content
    
    def captions_to_vtt(self, captions: List[Caption]) -> str:
        """Convert captions to WebVTT format"""
        vtt_content = "WEBVTT\n\n"
        
        for caption in captions:
            start = self.format_time(caption.start_time, SubtitleFormat.VTT)
            end = self.format_time(caption.end_time, SubtitleFormat.VTT)
            
            vtt_content += f"{start} --> {end}\n"
            vtt_content += f"{caption.text}\n"
            vtt_content += "\n"
        
        return vtt_content
    
    def captions_to_ass(self, captions: List[Caption], 
                       config: SubtitleConfig) -> str:
        """Convert captions to ASS format with styling"""
        ass_content = """[Script Info]
Title: Generated Captions
ScriptType: v4.00+

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,24,&H00FFFFFF,&H00000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,2,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
        
        for caption in captions:
            start = self.format_time(caption.start_time, SubtitleFormat.ASS)
            end = self.format_time(caption.end_time, SubtitleFormat.ASS)
            
            ass_content += f"Dialogue: 0,{start},{end},Default,,0,0,0,,{caption.text}\n"
        
        return ass_content
    
    def captions_to_json(self, captions: List[Caption]) -> str:
        """Convert captions to JSON format"""
        captions_data = []
        
        for caption in captions:
            captions_data.append({
                'start': caption.start_time,
                'end': caption.end_time,
                'text': caption.text,
                'speaker': caption.speaker,
                'confidence': caption.confidence
            })
        
        return json.dumps(captions_data, indent=2, ensure_ascii=False)
    
    def save_captions(self,
                     captions: List[Caption],
                     output_path: str,
                     config: SubtitleConfig) -> bool:
        """
        Save captions to file.
        
        Args:
            captions: List of captions
            output_path: Output file path
            config: Subtitle configuration
            
        Returns:
            True if successful
        """
        try:
            # Convert to requested format
            if config.format == SubtitleFormat.SRT:
                content = self.captions_to_srt(captions)
            elif config.format == SubtitleFormat.VTT:
                content = self.captions_to_vtt(captions)
            elif config.format == SubtitleFormat.ASS:
                content = self.captions_to_ass(captions, config)
            elif config.format == SubtitleFormat.JSON:
                content = self.captions_to_json(captions)
            else:
                print(f"[CAPTION] ❌ Unsupported format: {config.format}")
                return False
            
            # Write to file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"[CAPTION] ✅ Captions saved: {output_path}")
            return True
        
        except Exception as e:
            print(f"[CAPTION] ❌ Save failed: {e}")
            return False
    
    def embed_captions_in_video(self,
                               video_path: str,
                               captions: List[Caption],
                               output_path: str,
                               config: SubtitleConfig) -> bool:
        """
        Embed captions directly into video file.
        
        Args:
            video_path: Input video path
            captions: List of captions
            output_path: Output video path
            config: Subtitle configuration
            
        Returns:
            True if successful
        """
        if not os.path.exists(video_path):
            print(f"[CAPTION] ❌ Video not found: {video_path}")
            return False
        
        try:
            import cv2  # type: ignore
            
            print(f"[CAPTION] 🎬 Embedding captions in video...")
            
            cap = cv2.VideoCapture(video_path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # Create video writer
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            
            frame_idx = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                current_time = frame_idx / fps
                
                # Find active captions
                active_captions = [c for c in captions 
                                 if c.start_time <= current_time <= c.end_time]
                
                # Draw captions
                y_offset = height - 60 if config.position == "bottom" else 60
                
                for caption in active_captions:
                    text = caption.text
                    
                    # Wrap text if needed
                    words = text.split()
                    lines = []
                    current_line = ""
                    
                    for word in words:
                        if len(current_line) + len(word) + 1 <= config.max_chars_per_line:
                            current_line += word + " "
                        else:
                            if current_line:
                                lines.append(current_line.strip())
                            current_line = word + " "
                    
                    if current_line:
                        lines.append(current_line.strip())
                    
                    # Draw each line
                    for line_idx, line in enumerate(lines):
                        text_size = cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, 
                                                   config.font_size / 24, 2)[0]
                        x = (width - text_size[0]) // 2
                        y = y_offset + (line_idx * (config.font_size + 10))
                        
                        # Draw background
                        cv2.rectangle(frame, (x - 10, y - config.font_size - 5),
                                    (x + text_size[0] + 10, y + 5),
                                    (0, 0, 0), -1)
                        
                        # Draw text
                        cv2.putText(frame, line, (x, y),
                                  cv2.FONT_HERSHEY_SIMPLEX, config.font_size / 24,
                                  (255, 255, 255), 2)
                
                out.write(frame)
                frame_idx += 1
                
                if frame_idx % (fps * 5) == 0:  # Progress every 5 seconds
                    progress = f"{frame_idx}/{total_frames}"
                    print(f"[CAPTION] {progress}...")
            
            cap.release()
            out.release()
            
            print(f"[CAPTION] ✅ Video with captions saved: {output_path}")
            return True
        
        except Exception as e:
            print(f"[CAPTION] ❌ Embedding failed: {e}")
            return False


# Convenience function
def generate_captions_for_video(video_path: str,
                               output_format: str = "srt",
                               language: str = "es",
                               embed: bool = False) -> Optional[str]:
    """
    Quick function to generate captions for a video.
    
    Args:
        video_path: Path to video file
        output_format: Output format ('srt', 'vtt', 'ass', 'json')
        language: Language code
        embed: If True, embed captions in video; if False, save separately
        
    Returns:
        Path to output file or None if failed
    """
    generator = CaptionGenerator(language=language)
    
    # Extract captions
    captions = generator.extract_captions_from_video(video_path)
    if not captions:
        return None
    
    # Refine captions
    captions = generator.refine_captions(captions)
    
    config = SubtitleConfig(
        format=SubtitleFormat(output_format),
        language=language
    )
    
    # Save captions
    base_path = Path(video_path).stem
    if embed:
        output_path = f"{base_path}_with_captions.mp4"
        success = generator.embed_captions_in_video(video_path, captions, output_path, config)
    else:
        output_path = f"{base_path}.{output_format}"
        success = generator.save_captions(captions, output_path, config)
    
    return output_path if success else None


if __name__ == "__main__":
    print("[CAPTION] Caption Generator Module")
    print("[CAPTION] Ready for video captioning like HeyGen")
