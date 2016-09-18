import speech_recognition as sr

def listenToSpeech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Recording... ")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # outputs parsed audio
    return r.recognize_google(audio)

def checkSpeech(spoken, actual):
    # fix parsed speech and actual text (only alpha)
#    spoken = spoken.translate(None, ',.;:\"\'')
#    actual = actual.translate(None, ',.;:\"\'')
    if spoken == actual:
        return True
    else:
        return False

# simple testing"
s = listenToSpeech()
print checkSpeech(s, "box")
print checkSpeech(s, "hello")
