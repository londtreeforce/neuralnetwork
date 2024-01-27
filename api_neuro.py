import openai
import record
import Config

clear_text = record.recordAll().recognized_text()

def text_to_openai():
    api_key = Config.API_KEY

    input_text = clear_text
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt="The person said: " + input_text,
        max_tokens=100
    )

    response_text = response.choices[0].text.strip()
    print("OpenAI GPT Response:")
    print(response_text)


if __name__ == "__main__":
    text_to_openai()



