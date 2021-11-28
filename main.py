import requests
import smtplib
from datetime import datetime

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()
positional_data = data['iss_position']

iss_latitude = float(positional_data['latitude'])
iss_longitude = float(positional_data['longitude'])

iss_position = (iss_latitude, iss_longitude)

my_latitude = 42.360081
my_longitude = -71.058884

my_position = (my_latitude, my_longitude)

parameters = {
    'lat': my_latitude,
    'lng': my_longitude,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise_hour = int(sunrise.split('T')[1].split(':')[0])
sunset_hour = int(sunset.split('T')[1].split(':')[0])

current_time = datetime.now()

current_hour = current_time.hour

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

currently_dark = False
iss_currently_overhead = False

if (current_hour > 18) or current_hour < 3:
    currently_dark = True

if -5 < (iss_latitude - my_latitude) < 5 and -5 < (iss_longitude - my_longitude) < 5:
    iss_currently_overhead = True

if iss_currently_overhead and currently_dark:
    my_email = 'kccodetest@gmail.com'
    my_password = 'klayclarkecodetest'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='klayaclarke@gmail.com',
                            msg='Subject: Look Up\n\n'
                                'The international space station is in your area. Look up to see it.')
