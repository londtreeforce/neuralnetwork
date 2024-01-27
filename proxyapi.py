from openai import OpenAI

client = OpenAI(
    api_key="sk-g87G6e1hsxLkomwQDj5b39aK8dzBLK96",
    base_url="https://api.proxyapi.ru/openai/v1",
)

def main():

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}]
    )
    # print(chat_completion["message"]["content"])

    print(chat_completion)




if __name__ == '__main__':
    main()