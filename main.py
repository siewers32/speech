# import speech_recognition as sr

# rec = sr.Recognizer()

# audio = "test.wav"

# with sr.AudioFile(audio) as source:
#     au = rec.record(source)

# text = rec.recognize_google(au)

# print(text)

from openai import OpenAI
client = OpenAI()

audio_file= open("spoelen.wav", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

t = open("spoelen.txt", "wt" )
t.write(transcription.text)
print(transcription.text)