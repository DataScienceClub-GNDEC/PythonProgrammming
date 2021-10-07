import speech_recognition as sr
audio_file = ("Dhoom3.wav")
# use audio file as source

r = sr.Recognizer() # initialize the recognizer
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
# read the audio file

try:
    print("Audio file contains: " + r.recognize_google(audio))
except sr.UnknownValueError :
    print("Google speech recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from google Speech Recognition")