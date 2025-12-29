import python_weather
import asyncio

city = input("Enter your city: ")
print("")
async def getweather():
    client = python_weather.Client()
    weather = await client.get(city)
    await client.close()
    
    temperature = weather.temperature
    feel = weather.feels_like
    humidity = weather.humidity
    wind = weather.wind_speed
    condition = weather.description
    
    try:
        if temperature < 10:
            print("Stay inside your home.\nThere is cold outside.")
        elif temperature < 20:
            print("Sit in sunlight, if found.")
        elif temperature < 30:
            print("Moderate weather, you can do your outside work.")
        elif temperature < 40:
            print("Hot weather, Stay inside your home.")
        else:
            print("You will be regret if go outside you home.\nDrink plenty of water.") 
    finally:
        print("Thanks. Have nice day.")

    return f'''
    🌡️ Temperature in {city}: {temperature-6} °C
       feels like: {feel-4} °C
       humidity: {humidity}%
       wind: {wind} km/hr
       condition: {condition}'''
    


weather = asyncio.run(getweather())
print(weather)

