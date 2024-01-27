from openai import OpenAI
import Config

client = OpenAI(
    api_key=Config.API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)

def main():

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Привет"}]
    )
    # print(chat_completion["message"]["content"])



    print(chat_completion.choices[0].message.content)





if __name__ == '__main__':
    main()