import requests

res = requests.post("https://argos-translate.onrender.com/translate", json={
    "text": "hi",
    "from_lang": "en",
    "to_lang": "ru"
})

print(res.json())
