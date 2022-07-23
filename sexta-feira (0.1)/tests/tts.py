import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", "brazil")
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.)

engine.say('eu vou falar esse texto')
    
engine.runAndWait()