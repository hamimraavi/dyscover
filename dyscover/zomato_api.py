import requests

from django.conf import settings
from requests.exceptions import ConnectionError

BASE_URL = "https://developers.zomato.com/api/v2.1"


def get_lat_lon(location, header):
    coordinates = {}
    location_url = ("{base}/locations?query={location}".format(
        base=BASE_URL, location=location))

    try:
        response = requests.get(location_url, headers=header)
    except ConnectionError:
        status_code = 503
        return (coordinates, status_code)

    res = response.json()
    try:
        coordinates["latitude"] = (res["location_suggestions"][0]["latitude"])
        coordinates["longitude"] = (
            res["location_suggestions"][0]["longitude"])
    except IndexError:
        status_code = 404
        return (coordinates, status_code)
    status_code = 200
    return (coordinates, status_code)


def search_restaurants(location, start="0", queries="5"):
    results = {}

    header = {
        "User-agent": "curl/7.43.0",
        "Accept": "application/json",
        "user_key": settings.ZOMATO_KEY,
    }

    location, status_code = get_lat_lon(location, header)

    if status_code != 200:
        return (results, status_code)

    lat = str(location["latitude"])
    lon = str(location["longitude"])

    search_url = ("{base}/search?start={start}&count={queries}&lat={lat}" +
                  "&lon={lon}").format(base=BASE_URL, start=start,
                                       queries=queries, lat=lat, lon=lon)

    try:
        response = requests.get(search_url, headers=header)
    except ConnectionError:
        status_code = 503
        return (results, status_code)

    res = response.json()

    results["Restaurants"] = []
    for rest_idx in range(int(start), int(queries)):

        rest_dictionary = {}
        rest_dictionary["Name"] = (
            res["restaurants"][rest_idx]["restaurant"]["name"])
        rest_dictionary["Url"] = (
            res["restaurants"][rest_idx]["restaurant"]["url"])

        results["Restaurants"].append(rest_dictionary)
    status_code = 200
    return (results, status_code)
