import urllib.request
import sys
from typing import Final

import json
import re
from types import SimpleNamespace

class WeatherForecast:

    API_KEY: Final = "6QCRXBDRDQK26Y8TT6S7YPJ2S"
    Daily = True
    Hourly = True
    Base_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}"
    Middle_URL = "?unitGroup=metric"
    End_URL = "&key={}&contentType=json"

    def __init__(self, daily : bool, hourly : bool):
        self.Daily = daily
        self.Hourly = hourly

    def weather_data_request(self, city: str, start_date: str, end_date: str):
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

        url = self.Base_URL

        # Ha üresen marad a város, akkor Nonenal tér vissza
        if city == "":
            return None

        if  start_date == "" and end_date == "":
            return self.weather_data_request_simple(city)

        # Ha a dátumok formázása nem megfelelő, akkor Nonenal tér vissza
        matcher = re.compile('[0-2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]')
        if  not matcher.match(start_date) or  not matcher.match(end_date):
            return None

        url += "/{}/{}"
        url += self.Middle_URL

        if  self.Daily == False and self.Hourly == False:
            url += "&include=alerts%2Ccurrent"
        elif self.Daily == False and self.Hourly == True:
            url += "&include=alerts%2Ccurrent%2Chours"
        elif self.Daily == True and self.Hourly == False:
            url += "&include=alerts%2Ccurrent%2Cdays"
        else:
            url += "&include=hours%2Cdays%2Ccurrent%2Calerts"

        url += self.End_URL

        # API lekérés
        try:
            result_bytes = urllib.request.urlopen(url.format(city, start_date, end_date, self.API_KEY))
        except urllib.error.HTTPError as e:
            return None

        except  urllib.error.URLError as e:
            return None

        # JSON formátumba átalakítás
        json_data = str(json.load(result_bytes))
        json_data = json_data.replace("\'", "\"")
        json_data = json_data.replace("None", "null")

        data = json.loads(json_data, object_hook=lambda d: SimpleNamespace(**d))

        if data == "Bad API Request:Invalid location parameter value.":
            return None

        # Visszaadjuk az objektumot
        return data

    def weather_data_request_simple(self, city: str):
        """

        Ez a fügvény egy várost kér, ami alapján a következő 15 napi előrejelzés adatait tudja visszaadni
        egy objektumban.

        Paraméterek:

        city (str): A várso neve.

        return:
        Egy olyan objektumot ami tartalmazza az időjárási adatokat
        """

        url = self.Base_URL

        # Ha üresen marad a város, akkor Nonenal tér vissza
        if city == "":
            return None

        url += self.Middle_URL

        if self.Daily == False and self.Hourly == False:
            url += "&include=alerts%2Ccurrent"
        elif self.Daily == False and self.Hourly == True:
            url += "&include=alerts%2Ccurrent%2Chours"
        elif self.Daily == True and self.Hourly == False:
            url += "&include=alerts%2Ccurrent%2Cdays"
        else:
            url += "&include=hours%2Cdays%2Ccurrent%2Calerts"

        url += self.End_URL

        # API lekérés
        try:
            result_bytes = urllib.request.urlopen(url.format(city, self.API_KEY))
        except urllib.error.HTTPError as e:
            return None

        except  urllib.error.URLError as e:
            return None

        # JSON formátumba átalakítás
        json_data = str(json.load(result_bytes))
        json_data = json_data.replace("\'", "\"")
        json_data = json_data.replace("None", "null")

        data = json.loads(json_data, object_hook=lambda d: SimpleNamespace(**d))

        # Visszaadjuk az objektumot
        return data
