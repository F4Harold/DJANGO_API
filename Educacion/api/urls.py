from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ContenidoViewSet,
    LeccionViewSet,
    ModuloEducativoViewSet,
    ProgresoEducativoViewSet,
    ProgresoLeccionViewSet,
)

router = DefaultRouter()
router.register(r"modulos-educativos", ModuloEducativoViewSet)
router.register(r"contenidos", ContenidoViewSet)
router.register(r"lecciones", LeccionViewSet)
router.register(r"progresos-educativos", ProgresoEducativoViewSet)
router.register(r"progresos-lecciones", ProgresoLeccionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
