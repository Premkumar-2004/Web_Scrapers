import requests

apikey = "a6c33c6de71d79e8a2803702c558007e"

city = input("Enter the name of the city: ")
if not city:
    print("Please enter a valid city name.")
    exit()  # or handle the error appropriately

requesturl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

response = requests.get(requesturl)

if response.status_code == 200:
    data = response.json()
    desc = data['weather'][0]['description']
    print(f"CLIMATE:{desc}")
    temperature = data['main']['temp']
    print(f"THE CURRENT TEMPERATURE IN {city}:{temperature - 273.15} CELSIUS")
    weather=data['weather']# Add this line to print the data
    print(weather)

    syst=data['sys']
    print(syst)




else:
    print("Error occurred. Check your API key and city name.")
