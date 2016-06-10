import requests


def get_lat_lon(location, header):
    location_url = "%s%s" % (
        "https://developers.zomato.com/api/v2.1/locations?query=",
        location,
        )

    response = requests.get(location_url, headers=header)

    coordinates = {}
    try:
        res = response.json()
    except ValueError:
        coordinates["Error"] = "ValueError"
        return coordinates
    else:
        coordinates["latitude"] = (res["location_suggestions"][0]["latitude"])
        coordinates["longitude"] = (
            res["location_suggestions"][0]["longitude"]
            )
        return coordinates


def search_restaurants(location, start="0", queries="5"):
    results = {}

    header = {
        "User-agent": "curl/7.43.0",
        "Accept": "application/json",
        "user_key": "73b44e74c879ee61cd9b0220830e3971",
        }

    location = get_lat_lon(location, header)

    if "Error" in location:
        return results

    lat = str(location["latitude"])
    lon = str(location["longitude"])

    search_url = "%s%s%s%s%s%s%s%s%s" % (
        "https://developers.zomato.com/api/v2.1/search?",
        "&start=",
        start,
        "&count=",
        queries,
        "&lat=",
        lat,
        "&lon=",
        lon,
        )

    response = requests.get(search_url, headers=header)

    try:
        res = response.json()
    except ValueError:
        return results

    results["Restaurants"] = []
    for rest_idx in range(int(start), int(queries)):

        rest_dictionary = {}
        rest_dictionary["Name"] = (
            res["restaurants"][rest_idx]["restaurant"]["name"]
            )
        rest_dictionary["Url"] = (
            res["restaurants"][rest_idx]["restaurant"]["url"]
            )

        results["Restaurants"].append(rest_dictionary)
    return results
