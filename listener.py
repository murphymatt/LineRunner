import speech_recognition as sr

def listenToSpeech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening for your line... ")
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
