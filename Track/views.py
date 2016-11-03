from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('My First Track')


def test(request):
    return HttpResponse('My First Track Lab')