# API provider https://www.weatherapi.com/ 
import requests
def weather():
    response = response = requests.get("http://api.weatherapi.com/v1/current.json?key=<your_api_key_here>&q=Bangalore")
    data=response.json()
    return str(data)


