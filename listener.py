import speech_recognition as sr

class Listener:

    def __init__(self):
        self.r = sr.Recognizer()

    def listen_to_speech(self):
        with sr.Microphone() as source:
            audio = self.r.listen(source)

        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            print("You said: " + self.r.recognize_google(audio))
        except sr.UnknownValueError:
            print "I didn't quite get that"
            return self.listen_to_speech()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}"\
                  .format(e))

        # outputs parsed audio
        return self.r.recognize_google(audio)
