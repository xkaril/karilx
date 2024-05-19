import requests

API_KEY = 'b36bba573a15d68b8709bd01fe3ef5de'  # Reemplaza 'tu_clave_api' con tu clave real
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    # Construir la URL completa
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    # Hacer la solicitud a la API
    response = requests.get(url)
    
    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        # Extraer datos relevantes
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        description = weather['description']
        
        return {
            'city': city,
            'temperature': temperature,
            'description': description
        }
    else:
        return None

# Ejemplo de uso
city = "Madrid"
weather_data = get_weather(city)
if weather_data:
    print(f"El clima en {weather_data['city']} es {weather_data['description']} con una temperatura de {weather_data['temperature']}°C.")
else:
    print("No se pudo obtener el clima.")
