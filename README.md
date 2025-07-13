# Noise-Resilient-Multilingual-Assistive-Communication-System-for-the-Disabled-using-Raspberry-Pi
This project presents a low-cost, portable, and real-time assistive communication system designed to help individuals with speech and motor disabilities communicate through voice. The system records speech using a USB microphone connected to a Raspberry Pi, then applies a state-of-the-art speech enhancement model (MetricGAN+) to reduce noise from the captured audio. The enhanced audio is passed to OpenAI’s Whisper model for automatic speech recognition (ASR), which transcribes it into text. The transcribed text is then converted back into natural speech using offline text-to-speech (TTS) engines like gTTS or Festival, ensuring accessibility in multilingual contexts, including support for South Indian languages like Tamil and Telugu.

The complete pipeline is implemented on a Raspberry Pi 4, eliminating the need for a PC or internet connection, making it ideal for rural or remote environments. The user interface is entirely CLI-based and user-friendly, designed to be easily operable with minimal technical knowledge. To maintain robustness in diverse real-world acoustic environments, the system is equipped with a denoising mechanism that ensures the ASR output is accurate even in noisy backgrounds, earning the project its "noise-resilient" identity. The modular design allows for easy updates, such as switching TTS engines or ASR models based on hardware capabilities and language requirements.

Hardware Components Used:

🎤 USB Microphone – for capturing user's voice input.

🖥️ Raspberry Pi 4 (4GB/8GB RAM) – central processing unit for running enhancement, transcription, and TTS.

🔊 3.5mm Wired Earphones/Speaker – for audio output of the final synthesized speech.

💾 MicroSD Card (32GB or higher) – for OS and package storage.

⚡ Power Supply (5V/3A USB-C) – to power the Raspberry Pi.

🖱️ HDMI Monitor, Keyboard & Mouse – for local debugging and development (optional once system is deployed).

This project can be extended in the future with a touchscreen interface, support for dynamic language switching, and improved contextual understanding using NLP. It has the potential to bridge communication gaps for disabled individuals in multiple languages and environments, empowering them with a real-time voice of their own.
