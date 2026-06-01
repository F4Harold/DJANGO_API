from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EstadoPqrViewSet,
    PqrViewSet,
    AdjuntoViewSet,
    RegistroActividadViewSet
)

router = DefaultRouter()
# registro de endpoints del api
router.register(r'estado_pqr', EstadoPqrViewSet)
router.register(r'pqr', PqrViewSet)
router.register(r'adjuntos', AdjuntoViewSet)
router.register(r'registro_actividad', RegistroActividadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]