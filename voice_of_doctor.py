import os
from gtts import gTTS
from dotenv import load_dotenv
load_dotenv()

#Step 1a: Setup Text to Speech - TTS-Model(gTTS)

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text="Hi, I am Doctor AIsha. How can I help you?"
#text_to_speech_with_gtts_old(input_text=input_text,output_filepath="gtts_testing.mp3")

#Step 1b: Setup Text to Speech - TTS-Model(ElevenLabs)
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs()
    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id= "9BWtsMINqrJLrRacOk9x",
        model_id= "eleven_turbo_v2",
        output_format= "mp3_22050_32"
    )
    elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text=input_text, output_filepath="elevenlabs_testing.mp3")

#Step 2: Use Model for text output to voice (for making the saved file play itself immediately)

import subprocess
import platform
from elevenlabs import save

def play_audio(audio_path):
    os_name = platform.system()
    try:
        if os_name == "Windows" or os_name == "Linux":
            subprocess.run(['ffplay', '-nodisp', '-autoexit', audio_path])
        elif os_name == "Darwin":  # macOS
            subprocess.run(['afplay', audio_path])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Audio playback error: {e}")

# Autoplay with gTTS
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    play_audio(output_filepath)

# Autoplay with ElevenLabs
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs()
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="9BWtsMINqrJLrRacOk9x",
        model_id="eleven_turbo_v2",
        output_format="mp3_22050_32"
    )
    save(audio, output_filepath)
    play_audio(output_filepath)

# Test gTTS autoplay
input_text = "Hi, I am Doctor AIsha. How can I help you?"
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

# Test ElevenLabs autoplay
#text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_testing_autoplay.mp3")