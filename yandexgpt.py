import requests

def text_to_yandexgpt(api_key, clear_text):
    base_url = "https://api.yandexgpt.com/v1/completion"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "engine": "your_engine_name",  # Замените на имя вашего движка YandexGPT
        "prompt": f"The person said: {clear_text}",
        "max_tokens": 100
    }

    response = requests.post(base_url, json=data, headers=headers)

    if response.status_code == 200:
        response_text = response.json()["choices"][0]["text"].strip()
        print("YandexGPT Response:")
        print(response_text)
    else:
        print(f"Error {response.status_code}: {response.text}")

# Пример использования
api_key = "YOUR_API_KEY"
clear_text = "Your input text here"
text_to_yandexgpt(api_key, clear_text)