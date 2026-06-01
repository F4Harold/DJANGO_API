from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    auditoria_loginViewSet,
    credencialViewSet,
    rolViewSet,
    tipo_documentoViewSet,
    usuarioViewSet,
    usuario_rolViewSet
)
from rest_framework import permissions
from drf_yasg.Views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

router.register(r'auditoria_login', auditoria_loginViewSet)
router.register(r'credencial', credencialViewSet)
router.register(r'rol', rolViewSet)
router.register(r'tipo_documento', tipo_documentoViewSet)
router.register(r'usuario', usuarioViewSet)
router.register(r'usuario_rol', usuario_rolViewSet)

urlpatterns = [
    path('', include(router.urls))
]