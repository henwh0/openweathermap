import requests
def get_weather(city):
    api_key = 'YOUR API KEY HERE'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    
    weather_conditions = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    windspeed = data["wind"]["speed"]

    print(f"Weather in {city}: {weather_conditions}")
    print(f"Temperature: {temperature}°F")
    print(f"Wind Speed: {windspeed}mph")

def main():
    while True:
        city = input("Enter name of city (or type 'quit' to exit)")
        if city.lower() == "quit":
            break
        try:
            get_weather(city)
        except KeyError:
            print(f"City not found, try again.")
      
if __name__ == "__main__":
    main()
