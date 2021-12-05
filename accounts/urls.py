from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('',views.homepage, name ='homepage'),
    path('menu', views.menu, name='menu'),
    path('aboutus', views.about_us, name='about'),
    path('homepage', views.homepage, name='homepage'),
    path('reservation', views.reservation, name='reservation'),
    path('confirm_reservation', views.confirm_reservation, name='confirm_reservation')
]