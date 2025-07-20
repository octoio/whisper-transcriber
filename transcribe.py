#!/usr/bin/env python3
"""
Whisper MP3 Transcriber
A simple CLI tool to transcribe MP3 files using OpenAI's Whisper.
"""

import argparse
import os
import sys
import subprocess
from pathlib import Path

try:
    import whisper
except ImportError:
    print("Error: OpenAI Whisper is not installed.")
    print("Please install it with: pip install -r requirements.txt")
    sys.exit(1)


def check_ffmpeg():
    """Check if ffmpeg is available in the system."""
    try:
        subprocess.run(['ffmpeg', '-version'], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL, 
                      check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def transcribe_audio(audio_path, model_name="base"):
    """
    Transcribe an audio file using Whisper.
    
    Args:
        audio_path (str): Path to the audio file
        model_name (str): Whisper model to use (default: "base")
    
    Returns:
        str: Transcribed text
    """
    print(f"Loading Whisper '{model_name}' model...")
    model = whisper.load_model(model_name)
    
    print(f"Transcribing {audio_path}...")
    result = model.transcribe(audio_path)
    
    return result["text"]


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe MP3 files to text using OpenAI's Whisper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python transcribe.py audio.mp3
  python transcribe.py /path/to/audio.mp3
        """
    )
    
    parser.add_argument(
        "audio_file",
        help="Path to the MP3 file to transcribe"
    )
    
    parser.add_argument(
        "--model",
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model to use (default: base)"
    )
    
    # Show usage if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()
    
    # Check if ffmpeg is available
    if not check_ffmpeg():
        print("Warning: ffmpeg is not installed or not found in PATH.")
        print("Whisper may not work properly without ffmpeg.")
        print("Please install ffmpeg. See README.md for instructions.")
        print()
    
    # Validate input file
    audio_path = Path(args.audio_file)
    if not audio_path.exists():
        print(f"Error: File '{args.audio_file}' not found.")
        sys.exit(1)
    
    if not audio_path.suffix.lower() in ['.mp3', '.wav', '.m4a', '.flac', '.ogg']:
        print(f"Warning: '{audio_path.suffix}' files may not be supported.")
        print("Supported formats: .mp3, .wav, .m4a, .flac, .ogg")
        print()
    
    try:
        # Transcribe the audio
        transcript = transcribe_audio(str(audio_path), args.model)
        
        # Create output filename
        output_path = audio_path.parent / f"{audio_path.stem}.txt"
        
        # Save transcript
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(transcript.strip())
        
        print(f"Transcription completed!")
        print(f"Transcript saved to: {output_path}")
        print()
        print("Transcript preview:")
        print("-" * 50)
        print(transcript.strip()[:200] + "..." if len(transcript) > 200 else transcript.strip())
        
    except Exception as e:
        print(f"Error during transcription: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()