import pyttsx3
import pywintypes

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  
engine.setProperty('rate', 200)

engine.say("Grupo cadastrado é INATIVO!")
engine.runAndWait()
