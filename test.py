import requests

res = requests.post("http://localhost:5000/translate", json={
    "text": "hi",
    "from_lang": "en",
    "to_lang": "ru"
})

print(res.json())
