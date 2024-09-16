import requests

api_address = "https://newsapi.org/v2/top-headlines?country=us&apikey=60a808de0cea44ab8fb00ee9517c4341"
json_data = requests.get(api_address).json()

ar = []

def news():
    for i in range(3):
        ar.append(f"Number {i + 1}: {json_data['articles'][i]['title']}.")
    return ar

