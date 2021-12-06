from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_view, name='reservation'),
    path('create/', views.create_view, name='create'),
    path('delete/<int:id>', views.delete_view, name='delete'),
    path('update/<int:id>', views.update_view, name='update'),
]
