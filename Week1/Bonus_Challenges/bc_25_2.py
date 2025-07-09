import requests
api_key = "2b164b8ecda1d52c1dcd81034ea1dff0"

def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/3.0/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print("Error:", response.json().get("message", "Unknown error"))

city = input("Enter a city: ")
get_weather(city, api_key)
