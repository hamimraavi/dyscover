from django.http import HttpResponse

import homepage_python


def homepage(request):
    return HttpResponse(homepage_python.HTML_PAGE)
