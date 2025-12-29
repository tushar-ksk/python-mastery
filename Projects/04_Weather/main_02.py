import requests

def get_weather(city):
    API_KEY = "a0659afc86134862a8875643250205"  # Replace this with your WeatherAPI key
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    response = requests.get(url)
    print("Raw response:", response.text)  # 🐛 Debug line

    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['feelslike_c']
        weather = data['current']['condition']['text']
        return temperature, weather
    else:
        print("Error Code:", response.status_code)
        return None, None

# Test:
city = input("Enter city name: ")
temp, condition = get_weather(city)

if temp is not None:
    print(f"🌡️ Temperature in {city}: {temp} °C")
    print(f"🌥️ Condition: {condition}")
else:
    print("⚠️ Couldn't fetch weather. City might be wrong or API issue.")


try:
    if temp < 10:
        print("Stay inside your home.\nThere is cold outside.")
    elif temp < 20:
        print("Sit in sunlight, if found.")
    elif temp < 30:
        print("You can do your outdoor work.")
    elif temp < 37:
        print("You can go for a walk.")
    else:
        print("Stay inside your home.") 
finally:
    print("Thanks. Have a nice day.")
