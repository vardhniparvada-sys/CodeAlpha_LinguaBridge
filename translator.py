import requests

def translate_text(text, source, target):

    language_codes = {
        "English": "en",
        "Tamil": "ta",
        "Hindi": "hi",
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Japanese": "ja"
    }

    source_code = language_codes[source]
    target_code = language_codes[target]

    url = "https://translate.googleapis.com/translate_a/single"

    params = {
        "client": "gtx",
        "sl": source_code,
        "tl": target_code,
        "dt": "t",
        "q": text
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()

    translated_text = "".join(
        item[0] for item in data[0] if item[0]
    )

    return translated_text
