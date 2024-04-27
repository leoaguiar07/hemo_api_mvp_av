from geopy.geocoders import Nominatim

def encontrar_localizacao(bairro, cidade):
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

# Exemplo de uso
bairro = "Jórdoa"
cidade = "São Luis"
coordenadas = encontrar_localizacao(bairro, cidade)
if coordenadas:
    print(f"A localização de {bairro}, {cidade} é latitude:{coordenadas[0]}, longitude:{coordenadas[1]} ")
else:
    print(f"Não foi possível encontrar a localização de {bairro}, {cidade}")
