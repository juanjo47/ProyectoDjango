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
class TutorialesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "link",)
    ordering = ["nombre"]
    search_fields = ["nombre"]
admin.site.register(Tutoriales)