import requests
import re

response = requests.get('https://reqres.in/api/users')
emails = re.findall('\w+@\w+.\w+', response.text)
for line in emails:
    print(line)
