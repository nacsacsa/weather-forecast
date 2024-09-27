| Tesztelő: Kolozsi Márton  | Idő: 2024-09-23 |
|---------------------------|-----------------|
| Verzió:                   | Kliens: Pycharm |


| Teszteset                                                                          | Várt eredmény | Kapott eredmény | Sikeres | Hibaüzenet | Megjegyzés |
|------------------------------------------------------------------------------------|---------------|-----------------|---------|------------|------------|
| Nem adunk meg várost paraméternek a weather_data_request_simple metóduban          | None          | None            | Igen    |      -     |      -     |
| Nem létező várost adunk meg paraméterként a weather_data_request_simple metódusban | None          | None            | Igen    |      -     |      -     |
| Ha jó a kérés, akkor a válasz is megfelelő-e                                       | Debrecen      | Debrecen        | Igen    |      -     |      -     |
| Hibás kezdő dátum paraméter megadása a weather_data_request metódusban             | None          | None            | Igen    |      -     |      -     |
| Hibás vég dátum paraméter megadása a weather_data_request metódusban               | None          | None            | Igen    |      -     |      -     |
| Üres kezdő dátum paraméter megadása a weather_data_request metódusban              | None          | None            | Igen    |      -     |      -     |
| Üres vég dátum paraméter megadása a weather_data_request metódusban                | None          | None            | Igen    |      -     |      -     |
| Dátumok üresen hagyása a weather_data_request metódusban                           | None          | None            | igen    |      -     |      -     |
| Nem adunk meg város paramétert a weather_data_request metódusban                   | None          | None            | Igen    |      -     |      -     |

| Tesztelő: Kolozsi Márton  | Idő: 2024-09-27 |
|---------------------------|-----------------|
| Verzió:                   | Kliens: Pycharm |

| Teszteset                                                                          | Várt eredmény | Kapott eredmény | Sikeres | Hibaüzenet | Megjegyzés |
|------------------------------------------------------------------------------------|---------------|-----------------|---------|------------|------------|
| Ha jó a kérés, akkor a válasz is megfelelő-e                                       | Debrecen      | 'str' object has no attribute 'address'        | nem    |     'str' object has no attribute 'address'    |      -     |