import speech_recognition as sr
import record as rec
def trigger_function():
    print("Trigger word detected! Activating other function...")
    # здесь вы можете вызвать другую функцию, которую вы хотите запустить
    start_rec = rec.recordAll()

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        while True:
            audio_data = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio_data, language="en-US")
                print("Recognized:", text)
                if "hello" in text:  # замените "Alex" на ваше триггер-слово
                    trigger_function()
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError:
                print("Could not request results; check your internet connection")

if __name__ == "__main__":
    main()
