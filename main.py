import speech_recognition as sr
from pydub import AudioSegment

def speech_to_text(audio_file, language):
    #Ex: trasncript = speech_to_text(audio_file="file.mp3", language="pt-BR")

    audio = AudioSegment.from_file(audio_file)
    audio.export("audio_temp.wav", format="wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile("audio_temp.wav") as source:
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except Exception as e:
            print(e)
            return None
