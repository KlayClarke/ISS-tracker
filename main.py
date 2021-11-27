import requests

#
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
# positional_data = data['iss_position']
#
# longitude = positional_data['longitude']
# latitude = positional_data['latitude']
#
# iss_position = (longitude,latitude)
#
# print(iss_position)

my_latitude = 42.360081
my_longitude = -71.058884

parameters = {
    'lat': my_latitude,
    'lng': my_longitude,
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise)
print(sunset)

