import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices') #getting voices
engine.setProperty('voice', voices[1].id) #change parameter to 0 if you want male voice
engine.setProperty('rate', 165) #change the rate as your wish
def speak(audio):
    engine.say(audio)
    print(audio) #if you want to print the audio
    engine.runAndWait()

if __name__ == '__main__':
    speak("Hello, I am a text to speech generator I was created by subhankhan786")