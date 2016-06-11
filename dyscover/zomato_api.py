import requests

from django.conf import settings
from requests.exceptions import ConnectionError

BASE_URL = "https://developers.zomato.com/api/v2.1"


def get_lat_lon(location, header):
    coordinates = {}
    location_url = ("%s/locations?query=%s") % (BASE_URL, location)

    try:
        response = requests.get(location_url, headers=header)
    except ConnectionError:
        coordinates["Error"] = 503
        return coordinates

    res = response.json()
    try:
        coordinates["latitude"] = (res["location_suggestions"][0]["latitude"])
        coordinates["longitude"] = (
            res["location_suggestions"][0]["longitude"])
    except IndexError:
        coordinates["Error"] = 404
        return coordinates
    return coordinates


def search_restaurants(location, start="0", queries="5"):
    results = {}

    header = {
        "User-agent": "curl/7.43.0",
        "Accept": "application/json",
        "user_key": settings.ZOMATO_KEY,
    }

    location = get_lat_lon(location, header)

    if "Error" in location:
        results["Status"] = location["Error"]
        return results

    lat = str(location["latitude"])
    lon = str(location["longitude"])

    search_url = ("%s/search?start=%s&count=%s&lat=%s&lon=%s") % (
        BASE_URL, start, queries, lat, lon)

    try:
        response = requests.get(search_url, headers=header)
    except ConnectionError:
        results["Status"] = 503
        return results

    res = response.json()

    results["Restaurants"] = []
    for rest_idx in range(int(start), int(queries)):

        rest_dictionary = {}
        rest_dictionary["Name"] = (
            res["restaurants"][rest_idx]["restaurant"]["name"])
        rest_dictionary["Url"] = (
            res["restaurants"][rest_idx]["restaurant"]["url"])

        results["Restaurants"].append(rest_dictionary)
    return results
