import requests

def fetch_weather(api_key, city):
    # API endpoint for current weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Fetch weather data
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        # Extract relevant weather information
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        return None

# Example usage
api_key = 'your_api_key'
city = 'New York'

weather_info = fetch_weather(api_key, city)
if weather_info:
    print("Weather Information for", weather_info["city"])
    print("Temperature:", weather_info["temperature"], "°C")
    print("Description:", weather_info["description"])
    print("Humidity:", weather_info["humidity"], "%")
    print("Wind Speed:", weather_info["wind_speed"], "m/s")
else:
    print("Failed to fetch weather information.")
