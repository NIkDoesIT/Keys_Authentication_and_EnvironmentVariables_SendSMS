import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "my api key"
account_sid = "my twilio account sid"
auth_token = "my twilio auth token"
auth_token = ""

weather_params = {
    "lat": 13.082680,  #   49.023880,
    "lon": 80.270721,   # -122.801178,
    "appid": api_key,
    "cnt": 4,
}
requests.get(OWM_Endpoint, params=weather_params)

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = "Join Earth's mightiest heroes Like Kevin Bacon.",
        from_ = "my twilio phone number",
        to = "my home number in Canada")

# {"coord":{"lon":-122.8026,"lat":49.0164},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main":{"temp":280.32,"feels_like":280.32,"temp_min":279.38,"temp_max":281.19,"pressure":1026,"humidity":95,"sea_level":1026,"grnd_level":1022},"visibility":10000,"wind":{"speed":0.89,"deg":78,"gust":1.79},"clouds":{"all":100},"dt":1764188276,"sys":{"type":2,"id":2004740,"country":"CA","sunrise":1764171475,"sunset":1764202786},"timezone":-28800,"id":6180961,"name":"White Rock","cod":200}