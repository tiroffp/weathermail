import os
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weathermail.settings")
import django
django.setup()

from django.core.mail import send_mass_mail
from signup.models import Subscriber


def get_weather_text(city):
    base_url = 'http://api.wunderground.com/api/0276e500c3f22252/{}/q/{}/{}.json'

    # get current weather information
    request_url = base_url.format('conditions', city.state, city.name)
    response = requests.get(request_url).json()['current_observation']
    curr_temp = int(response['temp_f'])
    description = response['weather']

    # get historical weather information
    request_url = base_url.format('almanac', city.state, city.name)
    response = requests.get(request_url).json()['almanac']
    average_temp = int(response['temp_high']['normal']['F'])
    print(curr_temp, average_temp, description)

    # set return values
    subject = "Enjoy a discount on us!"
    message = "Today in {} it is {} degrees and {}".format(
        city.name,
        curr_temp,
        description.lower())

    # change subject if needed
    if (curr_temp >= average_temp + 5) or description == 'Sunny':
        subject = "It's nice out! Enjoy a discount on us."
    if (curr_temp <= average_temp - 5) or description == 'Precipitating':
        subject = "Not so nice out? That's okay, enjoy a discount on us."

    return {'Subject': subject, 'Message': message}

subscribers = Subscriber.objects.all()
messages = []
for sub in subscribers:
    weather_text = get_weather_text(sub.city)
    message = (
        weather_text['Subject'],
        weather_text['Message'],
        'Peyton@Weathermail.com',
        [sub.email])
    messages.append(message)
    # send_mass_mail(messages)
