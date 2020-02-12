print("REQUESTING SOME DATA FROM THE INTERNET...")

import requests 

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
print(request_url)

response = requests.get(request_url)
print(type(response))
print(dir(response))

print(response.status_code)
print(response.text)
