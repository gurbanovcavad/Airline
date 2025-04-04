from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    context = {"flights": Flight.objects.all()}
    return render(request, 'flights/index.html', context)

def flight(request, id):
    f = Flight.objects.get(pk=id)
    context = {'flight': f, 'passengers': f.passengers.all(), 
               'non_passengers': Passenger.objects.exclude(flights=f).all()}
    return render(request, 'flights/flight.html', context)

def book(request, id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=id)
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=[id, ]))
