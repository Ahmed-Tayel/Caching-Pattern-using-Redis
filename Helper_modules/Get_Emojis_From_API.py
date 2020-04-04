import requests
import json

response = requests.get("https://api.github.com/emojis")
response = json.loads(response.text)

i = 1
with open("MyEmojs.txt",'w') as f:
    for key,_ in response.items():
        f.write(f"{i} - ")
        f.write(str(key))
        f.write('\n')
        f.write('<br>')
        f.write('\n')
        i += 1