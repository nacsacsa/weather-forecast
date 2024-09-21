import urllib.request
import sys

import json
from types import SimpleNamespace

API_KEY = "6QCRXBDRDQK26Y8TT6S7YPJ2S"

def weather_data_request(city: str, start_date: str, end_date: str):
    """

    Ez a fügvény egy várost és két dátumot vár, ami alapján visszaad egy olyan objektumot, ami
    az időjárást adja vissza a megadott vársoban a két időpont között.

    Paraméterek:

    city (str): A várso neve.

    start_date (str): A kezdő dátum, formátuma (yyyy-MM-dd).

    end_date (str): A vég dátum, formátuma (yyyy-MM-dd).

    return:
    Egy olyan objektumot ami tartalmazza az időjárási adatokat
    """
    # API lekérés
    result_bytes = urllib.request.urlopen(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}/{}/{}"
        "?unitGroup=metric&key={}&contentType=json".format(city, start_date, end_date, API_KEY))

    # JSON formátumba átalakítás
    json_data = str(json.load(result_bytes))
    json_data = json_data.replace("\'", "\"")
    json_data = json_data.replace("None", "null")
    data = json.loads(json_data, object_hook=lambda d: SimpleNamespace(**d))

    # Visszaadjuk az objektumot
    return data

def weather_data_request(city: str):
    """

    Ez a fügvény egy várost kér, ami alapján a következő 15 napi előrejelzés adatait tudja visszaadni
    egy objektumban.

    Paraméterek:

    city (str): A várso neve.

    return:
    Egy olyan objektumot ami tartalmazza az időjárási adatokat
    """
    # API lekérés
    result_bytes = urllib.request.urlopen(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}"
        "?unitGroup=metric&key={}&contentType=json".format(city, API_KEY))

    # JSON formátumba átalakítás
    json_data = str(json.load(result_bytes))
    json_data = json_data.replace("\'", "\"")
    json_data = json_data.replace("None", "null")
    data = json.loads(json_data, object_hook=lambda d: SimpleNamespace(**d))

    # Visszaadjuk az objektumot
    return data
