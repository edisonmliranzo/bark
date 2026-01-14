"""
Simple test script to run Bark text-to-audio generation.
"""

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import numpy as np

# Preload models (this will download them on first run)
print("Loading Bark models...")
preload_models()

# Text prompt to generate audio from
text_prompt = """
Hello, my name is Bark. I am a text-to-audio AI model created by Suno.
I can generate realistic speech, music, and sound effects!
"""

print("Generating audio...")
audio_array = generate_audio(text_prompt)

# Save the audio to a WAV file
output_file = "bark_output.wav"
write_wav(output_file, SAMPLE_RATE, audio_array)
print(f"Audio saved to {output_file}")
print("Done!")
