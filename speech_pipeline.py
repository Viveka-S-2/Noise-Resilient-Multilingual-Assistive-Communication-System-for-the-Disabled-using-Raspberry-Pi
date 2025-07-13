import os
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
import whisper
from speechbrain.pretrained import SpectralMaskEnhancement

# ======== CONFIGURATIONS ========
DURATION = 5  # Recording duration in seconds
SAMPLE_RATE = 16000
RAW_AUDIO = "raw_input.wav"
CLEANED_AUDIO = "enhanced.wav"
OUTPUT_SPEECH = "output.mp3"
WHISPER_MODEL = "tiny"  # You can also try "base", "small" for better accuracy
# ================================

# --------- STEP 1: RECORD MICROPHONE INPUT ---------
def record_audio(filename=RAW_AUDIO, duration=DURATION, fs=SAMPLE_RATE):
    print("🎙️ Recording... Speak now!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)
    print(f"✅ Audio saved as: {filename}")

# --------- STEP 2: ENHANCE AUDIO USING METRICGAN+ ---------
def enhance_audio(input_path=RAW_AUDIO, output_path=CLEANED_AUDIO):
    print("🧠 Enhancing audio using MetricGAN+...")
    enhancer = SpectralMaskEnhancement.from_hparams(
        source="speechbrain/metricgan-plus-voicebank",
        savedir="pretrained_models/metricgan-plus"
    )
    enhanced_path = enhancer.enhance_file(input_path, output_path)
    print(f"✅ Enhanced audio saved as: {enhanced_path}")
    return enhanced_path


# --------- STEP 3: TRANSCRIBE WITH WHISPER ---------
def transcribe_audio(audio_path=CLEANED_AUDIO, model_size=WHISPER_MODEL):
    print("🗣️ Transcribing with Whisper...")
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path, task="transcribe")
    print("📝 Transcription:", result["text"])
    print("🌐 Detected language:", result["language"])
    return result["text"], result["language"]

# --------- STEP 4: CONVERT TEXT TO SPEECH ---------
def speak_text(text, lang_code="en", output_path=OUTPUT_SPEECH):
    print(f"🔊 Speaking text in language '{lang_code}'...")
    tts = gTTS(text=text, lang=lang_code)
    tts.save(output_path)
    os.system(f"mpg321 {output_path}")
    print("✅ Speech played successfully!")

# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    record_audio()
    enhance_audio()
    text, language_code = transcribe_audio()
    
    if text.strip():
        speak_text(text, lang_code=language_code)
    else:
        print("⚠️ No speech detected.")
