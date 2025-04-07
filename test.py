import requests

# Use your Vercel URL if deployed. If testing locally, use http://127.0.0.1:5000
url = "http://127.0.0.1:5000"

data = {
    "text": "Hello world!",
    "from_lang": "en",
    "to_lang": "ru"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
