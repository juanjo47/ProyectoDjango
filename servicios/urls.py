from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"servicios", views.ServicioViewSet)
router.register(r"dispositivos", views.DispElecViewSet)
router.register(r"tutoriales", views.TutorialesViewSet)

urlpatterns = [
    path('contact/<str:name>', views.contact, name="contacto"),
    path('', include(router.urls)),
    path('categorias/cantidad', views.categoria_count),
    path('servicios/cantidad', views.servicios_cantidad)
]