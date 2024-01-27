import speech_recognition as sr
import record as rec

def trigger_function():
    print("Trigger word detected!")
    rec.recordAll()
    # start_rec = rec.recordAll()

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        while True:
            audio_data = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio_data, language="ru-RU")
                print("Recognized:", text)
                if "Эй хуй" in text:
                    trigger_function()
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError:
                print("Could not request results")

if __name__ == "__main__":
    main()