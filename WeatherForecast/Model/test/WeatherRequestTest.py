import unittest

from WeatherForecast.Model.WeatherRequest import WeatherForecast


class MyTestCase(unittest.TestCase):

    def test_konstruktor1(self):
        w = WeatherForecast(False, False)
        self.assertEqual(w.Daily, False)
        self.assertEqual(w.Hourly, False)

    def test_konstruktor2(self):
        w = WeatherForecast(True, True)
        self.assertEqual(w.Daily, True)
        self.assertEqual(w.Hourly, True)

    def test_konstruktor3(self):
        w = WeatherForecast(True, False)
        self.assertEqual(w.Daily, True)
        self.assertEqual(w.Hourly, False)

    def test_konstruktor4(self):
        w = WeatherForecast(False, True)
        self.assertEqual(w.Daily, False)
        self.assertEqual(w.Hourly, True)

    def test_weather_data_request1(self):
        w = WeatherForecast(False, False)
        self.assertEqual(None, w.weather_data_request("", "2024-09-21", "2024-09-23"))

    def test_weather_data_request2(self):
        w = WeatherForecast(False, False)
        self.assertEqual(None, w.weather_data_request("Debrecen", "", "2024-09-23"))
        self.assertEqual(None, w.weather_data_request("Debrecen", "2024-09-21", ""))
        self.assertEqual(None, w.weather_data_request("Debrecen", "adada", "2024-09-23"))
        self.assertEqual(None, w.weather_data_request("Debrecen", "2024-09-21", "dfet353r"))
        self.assertEqual(None, w.weather_data_request("Debrecen", "adada", "dfet353r"))
        self.assertEqual(None, w.weather_data_request("Debrecen", "2024.09.21", "2024.09.22"))
        self.assertEqual(None, w.weather_data_request("dgdgdgdgd", "2024.09.21", "2024.09.22"))

    def test_weather_data_request_simple1(self):
        w = WeatherForecast(False, False)
        self.assertEqual(None, w.weather_data_request_simple(""))
        self.assertEqual(None, w.weather_data_request_simple("dgdgdgd"))

    def test_weather_data_request_simple2(self):
        w = WeatherForecast(False, False)
        self.assertEqual("Debrecen", w.weather_data_request_simple("Debrecen").address)
        self.assertEqual(None, w.weather_data_request_simple("dgdgdgd"))


if __name__ == '__main__':
    unittest.main()
