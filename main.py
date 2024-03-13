# import speech_recognition as sr

# rec = sr.Recognizer()

# audio = "test.wav"

# with sr.AudioFile(audio) as source:
#     au = rec.record(source)

# text = rec.recognize_google(au)

# print(text)

from openai import OpenAI
client = OpenAI()

audio_file= open("test2.wav", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)