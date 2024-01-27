import pyaudio
import wave
import speech_recognition as speech_r
import librosa.display
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# import openai
from openai import OpenAI
import Config

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()
RECORD_SECONDS = 5
def record_audio():
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)


    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return OUTPUT_FILENAME



def recognize_audio(audio_file):
    recognizer = speech_r.Recognizer()
    with speech_r.AudioFile(audio_file) as audio:
        audio_data = recognizer.record(audio)
        recognized_text = recognizer.recognize_google(audio_data, language="ru-RU")
    return recognized_text

def text_to_openai(recognized_text):
    client = OpenAI (
        api_key=Config.API_KEY,
        base_url="https://api.proxyapi.ru/openai/v1",
    )


    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": recognized_text}]
    )

    print(chat_completion.choices[0].message.content)




def recordAll():
    audio_file = record_audio()
    recognized_text = recognize_audio(audio_file)
    print("Recognized Text:")
    print(recognized_text)
    text_to_openai(recognized_text)
    # This Function Send recognized text to openAI



if __name__ == '__main__':
    recordAll()











# def text_to_openai(recognized_text):
#     response = openai.Completion.create(
#         engine="gpt-3.5-turbo-1106",  # Replace with the desired GPT-3 engine configuration
#         prompt="The person said: " + recognized_text,
#
#     )
#
#     response_text = response.choices[0].text.strip()
#     print("OpenAI GPT Response:")
#     print(response_text)