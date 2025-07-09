import json

def get_weather(city_name):
    try:
        with open("Week1/Bonus_Challenges/weather_data.json", "r") as file:
            weather_data = json.load(file)

        city = city_name.strip().lower()

        if city in weather_data:
            data = weather_data[city]
            print(f"\nWeather in {city.title()}")
            print(f"Temperature: {data['temperature']}°C")
            print(f"Condition: {data['condition'].title()}")
            print(f"Humidity: {data['humidity']}%")
        else:
            print("City not found in the database.")

    except FileNotFoundError:
        print("'weather_data.json' file not found.")
    except json.JSONDecodeError:
        print("Failed to read weather data.")


if __name__ == "__main__":
    while True:
        city_input = input("\nEnter a city (or 'q' to quit): ")
        if city_input.lower() == "q":
            break
        get_weather(city_input)
