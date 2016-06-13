from django.http import JsonResponse

import zomato_api


def show_restaurants(request):
    location = request.GET.get('q')
    if not location:
        res = {}
        return JsonResponse(res, status=400, safe=False)
    res, status_code = zomato_api.search_restaurants(location)
    response = JsonResponse(data=res, status=status_code, safe=False)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET'
    return response
