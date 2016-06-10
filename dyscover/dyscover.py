import requests

from django.conf import settings


def get_lat_lon(location, header):
    location_url = ("https://developers.zomato.com/api/v2.1/locations?"
                    "query=%s") % location

    response = requests.get(location_url, headers=header)
    res = response.json()

    coordinates = {}

    try:
        coordinates["latitude"] = (res["location_suggestions"][0]["latitude"])
        coordinates["longitude"] = (
            res["location_suggestions"][0]["longitude"])
    except IndexError:
        coordinates["Error"] = "IndexError"
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
        return results

    lat = str(location["latitude"])
    lon = str(location["longitude"])

    search_url = ("https://developers.zomato.com/api/v2.1/search?start="
                  "%s&count=%s&lat=%s&lon=%s") % (start, queries, lat, lon)

    response = requests.get(search_url, headers=header)

    try:
        res = response.json()
    except ValueError:
        return results

    results["Restaurants"] = []
    for rest_idx in range(int(start), int(queries)):

        rest_dictionary = {}
        rest_dictionary["Name"] = (
            res["restaurants"][rest_idx]["restaurant"]["name"])
        rest_dictionary["Url"] = (
            res["restaurants"][rest_idx]["restaurant"]["url"])

        results["Restaurants"].append(rest_dictionary)
    return results
