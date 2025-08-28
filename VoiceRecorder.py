import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import wavio as wv


def record_audio(filename="output.wav", duration=5, freq=44100, channels=2):
    """Record audio from microphone and save as WAV."""
    try:
        print(f"🎙️ Recording for {duration} seconds...")
        recording = sd.rec(int(duration * freq), samplerate=freq,
                           channels=channels, dtype='float32')

        int_recording = np.int16(recording * 32767)

        write(filename, freq, int_recording)
        print(f"✅ Saved recording as {filename}")

        alt_filename = "alt_" + filename
        wv.write(alt_filename, recording, freq, sampwidth=2)
        print(f"✅ Saved alternate recording as {alt_filename}")

    except Exception as e:
        print(f"❌ Error while recording: {e}")


if __name__ == "__main__":
    record_audio("recording.wav", duration=5)
