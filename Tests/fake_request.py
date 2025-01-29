import requests

url = "http://127.0.0.1:5000/api/check-imei"
headers = {"Content-Type": "application/json"}
data = {"imei": "490154203237518", "token": "your_api_token"}

response = requests.post(url, json=data, headers=headers)
print(response.json())