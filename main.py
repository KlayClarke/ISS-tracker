import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

positional_data = response.json()['iss_position']

longitude = positional_data['longitude']
latitude = positional_data['latitude']

print(longitude)
print(latitude)