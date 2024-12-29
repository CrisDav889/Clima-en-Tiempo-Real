import requests


def obtener_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        clima = datos['weather'][0]['description']
        temp_actual = datos['main']['temp']
        temp_min = datos['main']['temp_min']
        temp_max = datos['main']['temp_max']

        print(f"Clima en {ciudad}: {clima}")
        print(f"Temperatura actual: {temp_actual}°C")
        print(f"Temperatura mínima: {temp_min}°C")
        print(f"Temperatura máxima: {temp_max}°C")
    else:
        print(f"Error al obtener el clima de {ciudad}. Código de estado: {respuesta.status_code}")


if __name__ == "__main__":
    ciudad = input("Ingrese la ciudad: ")
    api_key = ''
# Usa tu Api Key de openweather 
    obtener_clima(ciudad, api_key)

