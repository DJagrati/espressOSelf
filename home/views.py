from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse

def index(request):
    return HttpResponse("Homepage")

def bookSeat(request):
    return HttpResponse("Book a seat")
