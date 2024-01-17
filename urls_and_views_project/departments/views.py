import time

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse(f'Response from {time.time()}')


def index2(request, *args, **kwargs):
    return HttpResponse(f'Response with {args} and {kwargs}')
