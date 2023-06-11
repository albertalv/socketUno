from django.shortcuts import render
from django.http import JsonResponse
connected = False

def sala(request):
    return render(request, 'prueba/sala.html', {'connected': connected})

def indice(request):
    return render(request, 'prueba/indice.html', {'connected': connected})

def cambiar_estado(request):
    global connected
    connected = not connected
    return render(request, 'prueba/sala.html', {'connected': connected})


def obtener_estado(request):
    return JsonResponse({'connected': connected})
