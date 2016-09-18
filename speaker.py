import pyttsx as tts

class Speaker:

    def __init__(self):
        self.engine = tts.init()
        
    def say_line(self, line):
        self.engine.say(line)
        self.engine.runAndWait()
