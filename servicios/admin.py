from django.contrib import admin
from .models import Categoria, Servicio, DispElec, Tutoriales

"""
Categoria
"""
admin.site.register(Categoria)
"""
Servicio
"""
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades", "disponible",)
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["disponible"]
admin.site.register(Servicio, ServicioAdmin)
"""
Dispositivos Electronicos
"""
class DispElecAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "unidades", "disponible",)
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["disponible"]
admin.site.register(DispElec, DispElecAdmin)
"""
Tutoriales
"""
admin.site.register(Tutoriales)