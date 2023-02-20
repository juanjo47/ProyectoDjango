from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from rest_framework import viewsets, generics
from .models import Categoria, Servicio, DispElec, Tutoriales
from .serializers import CategoriaSerializer, ServicioSerializer
from rest_framework.decorators import api_view

##def index(request):
##    return HttpResponse("hola mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class DispElecViewSet(viewsets.ModelViewSet):
    queryset = DispElec.objects.all()
    serializer_class = ServicioSerializer

class TutorialesViewSet(viewsets.ModelViewSet):
    queryset = Tutoriales.objects.all()
    serializer_class = ServicioSerializer

@api_view(["GET"])
def categoria_count(request):

    try:
        cantidad = Categoria.objects.count()
        return JsonResponse(
            {
                "nombres": cantidad
            },
            safe = False,
            status = 200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)

@api_view(["GET"])
def servicios_cantidad(request):

    try:
        cantidad = Servicio.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe = False,
            status = 200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)