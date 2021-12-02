from django.shortcuts import render, redirect
from .forms import ReserveForm
from .models import Reserve


# Create your views here.

def about_us(request):
    return render(request, 'restaurant/about_us.html')


def menu(request):
    return render(request, 'restaurant/menu.html')


def homepage(request):
    return render(request, 'restaurant/homepage.html')


def reservation(request):
    reserve = Reserve.objects.all()
    context = {'reserve': reserve}
    return render(request, 'restaurant/reservation.html', context)


def confirm_reservation(request):
    form = ReserveForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('reservation')

    return render(request, 'restaurant/confirm_reservation.html')
