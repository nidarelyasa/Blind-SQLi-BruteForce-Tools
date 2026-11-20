import requests

url = "https://0a570040030e49fb80004ef50012005f.web-security-academy.net/"

response = requests.get(url, timeout=20)

print("Status:", response.status_code)
print("TrackingId:", response.cookies.get("TrackingId"))
print("Session:", response.cookies.get("session"))