from django.http import JsonResponse
from django.views.decorators.http import require_GET
import sys
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'hotel/home.html')

def handle_button_click(request):
    if request.method == 'POST':
        # Обработка действия кнопки
        return HttpResponse("Button clicked!")
    return redirect('home')



@require_GET
def ble_control(request):
    try:
        from BLE import BLEDevice  # Импорт класса из BLE.py
        from main import Device  # Импорт класса из main.py

        # Пример использования
        ble_manager = BLEDevice()
        main_controller = Device()

        # Вызов методов
        ble_result = ble_manager.set_light_on()
        main_result = main_controller.set_light_off()

        return JsonResponse({
            'status': 'success',
            'ble_result': ble_result,
            'main_result': main_result
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)