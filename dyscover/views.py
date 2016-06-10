from django.http import HttpResponse, JsonResponse

import dyscover


def index(request):
    return HttpResponse("Welcome to dyscover")


def show_restaurants(request):
    location = request.GET.get('q')
    if not location:
        res = {}
        res["Status"] = "400"
        return JsonResponse(res, safe=False)
    res = dyscover.search_restaurants(location)
    return JsonResponse(res, safe=False)
