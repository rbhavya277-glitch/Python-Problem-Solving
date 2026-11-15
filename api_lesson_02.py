import requests

url = "https://air-quality-api.open-meteo.com/v1/air-quality"

params = {
    "latitude": 17.3850,
    "longitude": 78.4867,
    "hourly": "pm2_5",
    "timezone": "Asia/Kolkata"
}

response = requests.get(url, params=params)

print(response.status_code)

data = response.json()

print(data)