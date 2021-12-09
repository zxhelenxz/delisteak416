from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from reservations.forms import ReserveForm
from reservations.models import Reserve

# Create your views here.


@login_required(login_url='login')
def reservation_view(request):
    reservation = Reserve.objects.filter(user=request.user)
    context = {'reservations': reservation}
    return render(request, 'reservation/reservation.html', context)


@login_required(login_url='login')
def create_view(request):
    form = ReserveForm(request.POST or None)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            context = {'user': form.instance.user}
            return render(request, 'reservation/confirm_reservation.html',context)
    return render(request, 'reservation/create_reservation.html', {'form': form})


@login_required(login_url='login')
def delete_view(request, id):
    reservation = Reserve.objects.get(id=id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation')
    return render(request, 'reservation/delete_reservation.html', {'reservation': reservation})


@login_required(login_url='login')
def update_view(request, id):
    reservation = Reserve.objects.get(id=id)
    form = ReserveForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
        return redirect('reservation')
    return render(request, 'reservation/update_reservation.html', {'form': form})
