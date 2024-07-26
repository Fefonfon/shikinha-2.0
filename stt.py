import speech_recognition as sr
from pydub import AudioSegment

def speech_to_text(audio_file, language):
    # Loads audio file into memory and exports it to a .wav format through pydub
    audio = AudioSegment.from_file(audio_file)
    audio.export("audio_temp.wav", format="wav")

    # Create a speech recognizer
    recognizer = sr.Recognizer()
    with sr.AudioFile("audio_temp.wav") as source:
        audio_data = recognizer.record(source)

        try:
            # Uses Google's speech recognition service to transcribe audio
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except Exception as e:
            print(e)
            return None

# Usage example:
transcript = speech_to_text(audio_file="audio_teste.ogg", language="pt-BR")
print(transcript)
