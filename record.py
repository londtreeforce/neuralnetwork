import pyaudio
import wave
import speech_recognition as speech_r
import librosa.display
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

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

# def text_to_openai(recognized_text):
#     model_name = "gpt-2"
#     tokenizer = GPT2Tokenizer.from_pretrained(model_name)
#     model = GPT2LMHeadModel.from_pretrained(model_name)
#
#     input_text = recognized_text
#     inputs = tokenizer.encode("The person said: " + input_text, return_tensors="pt")
#
#     response = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
#     response_text = tokenizer.decode(response[0], skip_special_tokens=True)
#     print("OpenAI GPT Response:")
#     print(response_text)

def recordAll():
    audio_file = record_audio()
    recognized_text = recognize_audio(audio_file)
    print("Recognized Text:")
    print(recognized_text)
    # text_to_openai(recognized_text)

if __name__ == '__main__':
    recordAll()
