import requests


def get_stations():
    """
    Возвращает номера станция в формате list
    """
    response = requests.get("https://qa-scooter.praktikum-services.ru/api/v1/stations/search")
    data = []
    for i in response.json():
        data.append(i["number"])
    return data