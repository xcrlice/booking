from django.shortcuts import render

# Create your views here.

def index_page(request):
    context = {}
    return render(request, "index.html", context)

def search_page(request):
    context = {}
    return render(request, "search.html", context)

def booking_page(request):
    context = {}
    return render(request, "booking.html", context)