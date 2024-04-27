from datetime import date, datetime, timedelta
import calendar

from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def get_geolocalizacao(bairro, cidade):
    
    """
    The get_geolocalizacao function takes a bairro and cidade as input, 
    and returns the latitude and longitude of that location.
    
    
    :param bairro: Search for the neighborhood
    :param cidade: Search for the city in which the neighborhood is located
    :return: A tuple with latitude and longitude
    :doc-author: Trelent
    """

    # Inicializa o geocoder do Nominatim
    geolocalizador = Nominatim(user_agent="my_app")

    # Concatena bairro e cidade para formar a consulta de pesquisa
    consulta = f"{bairro}, {cidade}"

    # Tenta encontrar a localização usando a consulta
    try:
        localizacao = geolocalizador.geocode(consulta)
        if localizacao:
            latitude = localizacao.latitude
            longitude = localizacao.longitude
            return latitude, longitude
        else:
            return None
    except Exception as e:
        print("Erro ao encontrar localização:", e)
        return None

  
def get_distance(lat1, lon1, lat2, lon2):
    
    """
    The get_distance function takes in two sets of coordinates and returns the distance between them.
        The function uses the geodesic method from the geopy library to calculate this distance.
    
    :param lat1: Get the latitude of the first coordinate
    :param lon1: Represent the longitude of the first coordinate
    :param lat2: Get the latitude of the second coordinate
    :param lon2: Get the longitude of the second coordinate
    :return: The distance between two points in kilometers
    :doc-author: Trelent
    """
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)

    distance = geodesic(coord1, coord2).kilometers
    return distance
    

def get_mes_passado():
    mes_passado = (datetime.now().month)-1
    if mes_passado == 0:
        mes_passado = 12
    
    return mes_passado


def get_dias_mes_passado():
    mes_passado = (datetime.now().month)-1

    num_days = calendar.monthrange(datetime.now().year, mes_passado)[1]

    return num_days
