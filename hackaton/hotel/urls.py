from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('button-click/', views.handle_button_click, name='button_click'),
    path('ble-control/', views.ble_control, name='ble_control'),
]