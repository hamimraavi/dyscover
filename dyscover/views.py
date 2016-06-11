from django.http import HttpResponse, JsonResponse

import zomato_api


def index(request):
    return HttpResponse("Welcome to dyscover")


def show_restaurants(request):
    location = request.GET.get('q')
    if not location:
        res = {}
        return JsonResponse(res, status=400, safe=False)
    res = zomato_api.search_restaurants(location)
    if not res:
        res = {}
        return JsonResponse(data=res, status=404, safe=False)
    if "Status" in res:
        status = res["Status"]
        res = {}
        return JsonResponse(data=res, status=status, safe=False)
    return JsonResponse(data=res, status=200, safe=False)
