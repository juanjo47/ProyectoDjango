from rest_framework import serializers
from .models import Categoria, Servicio, DispElec, Tutoriales


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = "__all__"

class DispElecSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispElec
        fields = "__all__"

class TutorialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutoriales
        fields = "__all__"