import pyttsx as tts

def sayLine(line):
    engine = tts.init()
    engine.say(line)
    engine.runAndWait()
