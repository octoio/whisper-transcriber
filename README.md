# Whisper Transcriber

A simple command-line tool that transcribes MP3 files to text using OpenAI's Whisper model.

## Features

- Transcribe MP3 (and other audio formats) to text
- Uses OpenAI's Whisper "base" model by default
- Saves transcripts as `.txt` files in the same directory as the source audio
- Graceful error handling for missing dependencies
- Support for multiple Whisper model sizes

## Requirements

- Python 3.8 or higher
- ffmpeg (for audio processing)

## Installation

### 1. Set Up Python Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Alternative: Global Installation

If you prefer to install globally (not recommended):

```bash
pip install -r requirements.txt
```

### 2. Install ffmpeg

#### macOS (using Homebrew)
```bash
brew install ffmpeg
```

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

#### Windows
1. Download ffmpeg from https://ffmpeg.org/download.html
2. Extract and add the `bin` folder to your system PATH
3. Or use chocolatey: `choco install ffmpeg`

#### Verify ffmpeg installation
```bash
ffmpeg -version
```

## Usage

### Basic Usage

Make sure your virtual environment is activated first:

```bash
# Activate virtual environment (if using venv)
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Transcribe audio file
python transcribe.py audio.mp3
```

This will create a file called `audio.txt` in the same directory as `audio.mp3`.

### Specify Whisper Model

```bash
python transcribe.py --model small audio.mp3
```

Available models (from fastest/least accurate to slowest/most accurate):
- `tiny`
- `base` (default)
- `small`
- `medium`
- `large`

### Examples

```bash
# Transcribe a podcast episode
python transcribe.py podcast_episode.mp3

# Use a more accurate model for important audio
python transcribe.py --model large interview.mp3

# Process audio from different directory
python transcribe.py /path/to/audio/meeting.mp3
```

### Help

```bash
python transcribe.py --help
```

## Supported Audio Formats

While this tool is designed for MP3 files, Whisper supports many audio formats:
- MP3
- WAV
- M4A
- FLAC
- OGG

## Output

The transcribed text will be saved as a `.txt` file with the same name as the input file:
- `meeting.mp3` → `meeting.txt`
- `interview.wav` → `interview.txt`

## Troubleshooting

### "Error: OpenAI Whisper is not installed"
Make sure your virtual environment is activated and run:
```bash
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### "Warning: ffmpeg is not installed"
Install ffmpeg using the instructions above. Whisper requires ffmpeg for audio processing.

### Out of Memory Errors
Try using a smaller model:
```bash
python transcribe.py --model tiny audio.mp3
```

### Slow Transcription
- The first run downloads the model (can take a few minutes)
- Subsequent runs are much faster
- Use smaller models (`tiny` or `base`) for faster processing
- Use larger models (`medium` or `large`) for better accuracy

## How It Works

1. Loads the specified Whisper model (downloads on first use)
2. Processes the audio file using Whisper's transcription engine
3. Saves the transcript as a text file in the same directory
4. Shows a preview of the transcribed text

## Model Download Sizes

Models are downloaded automatically on first use:
- `tiny`: ~39 MB
- `base`: ~142 MB
- `small`: ~466 MB
- `medium`: ~1.5 GB
- `large`: ~2.9 GB

## License

This project uses OpenAI's Whisper, which is licensed under the MIT License.