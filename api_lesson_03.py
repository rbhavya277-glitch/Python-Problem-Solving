import requests

url = "https://air-quality-api.open-meteo.com/v1/air-quality"

params = {
    "latitude": 17.3850,
    "longitude": 78.4867,
    "hourly": "pm2_5",
    "timezone": "Asia/Kolkata"
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)

data = response.json()

print("\nCity coordinates:")
print(data["latitude"], data["longitude"])

print("\nAvailable hourly data:")
print(data["hourly"].keys())

print("\nFirst 5 timestamps:")
print(data["hourly"]["time"][:5])

print("\nFirst 5 PM2.5 measurements:")
print(data["hourly"]["pm2_5"][:5])