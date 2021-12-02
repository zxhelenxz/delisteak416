from django.urls import path
from . import views

urlpatterns = [
    path('menu', views.menu, name='menu'),
    path('aboutus', views.about_us, name='aboutus'),
    path('homepage', views.homepage, name='homepage'),
    path('reservation', views.reservation, name='reservation'),
    path('confirm_reservation', views.confirm_reservation, name='confirm_reservation')
]