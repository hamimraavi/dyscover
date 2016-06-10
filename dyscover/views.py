from django.http import HttpResponse, JsonResponse

import dyscover


def index(request):
    return HttpResponse("Welcome to dyscover")


def show_restaurants(request):
    location = request.GET.get('q')
    if not location:
        res = {}
        return JsonResponse(res, status=400, safe=False)
    res = dyscover.search_restaurants(location)
    if not res:
        return JsonResponse(data=res, status=404, safe=False)
    return JsonResponse(data=res, status=200, safe=False)
