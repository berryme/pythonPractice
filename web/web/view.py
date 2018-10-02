from django.http import HttpResponse


def index(request):
    str = "Hello"
    return HttpResponse(str)
