"""Fetch current weather and make clothing recommendations."""


import urllib  # allows getting data from URLs
import json  # parses JSON data


def jacket(condition):
    """Return true if weather conditon is wet."""
    condition = condition.lower()
    if condition == 'drizzle' or condition == 'mist' or 'rain' in condition or 'showers' in condition:
        return "It\'s raining, I recommend a rain coat."
    if 'snow' in condition:
        return "It\'s snowing, I recommend a coat."
    else:
        return "Conditions aren't too bad, you probaly don't need a coat."


API_KEY = '8595da0358b51ce6'
BASE_URL = 'http://api.wunderground.com/api/'
feature = 'conditions'

userCity = raw_input()
url = BASE_URL+API_KEY+'/'+feature+'/q/'+userCity+'.json'
response = urllib.urlopen(url)
data = json.loads(response.read())

if 'results' in data['response']:
    print "Which country is your city located in?"
    userCountry = raw_input()
    country_count = 0
    country_index = 0
    states = []
    for result in data['response']['results']:
        if result['country_name'].lower() == userCountry.lower():
            country_count += 1
            country_index += 1
            states.append(result['state'])
    if country_count > 1:
        print "Which province / state is your city located in?"
        print "You can chose from [" + '], ['.join(states) + "]"
        userState = raw_input()
        state_count = 0
        for result in data['response']['results']:
            if result['state'].lower() == userState.lower():
                state_count += 1
        if state_count > 1:
            print "There were still ambiguous results!"
            print "This has not been fixed yet."
        else:
            url = BASE_URL+API_KEY+'/'+feature
            url += data['response']['results'][country_index]['l']+'.json'
            response = urllib.urlopen(url)
            data = json.loads(response.read())
    else:
        url = BASE_URL+API_KEY+'/'+feature
        url += data['response']['results'][country_index]['l']+'.json'
        response = urllib.urlopen(url)
        data = json.loads(response.read())

weather_condition = data['current_observation']['weather']
temp_c = data['current_observation']['temp_c']

print jacket(weather_condition)

if temp_c >= 10:
    print "It's warm, you're probably good to wear shorts and a T-shirt."
if temp_c >= 4 and 10 > temp_c:
    print "It's a bit chilly, maybe wear a sweater."
if temp_c >= -1 and 4 > temp_c:
    print "It's cold, wear a sweater and some gloves."
if temp_c >= -6 and -1 > temp_c:
    print "It's below zero, wear a sweater, some decent pants, and a coat."
if -6 > temp_c:
    print "It's pretty cold out. Stay inside."

print "The current conditions are", weather_condition.lower(), "and", temp_c, "C."
# print data['current_observation']['weather']
# print data
