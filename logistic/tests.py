import requests
import json

url = 'http://localhost:8882/api/v1'
headers = {'Content-Type': 'application/json'}

attr = '/stocks/'
response = requests.get(url + attr, headers=headers)
print(response.json())

# attr = '/products/?search=апельсин'
# response = requests.get(url + attr, headers=headers)
# print(response.json())
#
# attr = '/stocks/?products=1'
# response = requests.get(url + attr, headers=headers)
# print(response.json())
