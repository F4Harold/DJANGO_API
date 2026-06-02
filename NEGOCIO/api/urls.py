from rest_framework.routers import DefaultRouter
from .views import (
    BancoViewSet, ProductoCrediticioViewSet, AsesorBancarioViewSet,
    ContactoAsesorViewSet, LeadViewSet, ConversacionUsuarioAsesorViewSet,
    CreditoDesembolsadoViewSet, TransaccionComisionViewSet,
)

router = DefaultRouter()
router.register(r'bancos',         BancoViewSet,                     basename='banco')
router.register(r'productos',      ProductoCrediticioViewSet,        basename='producto')
router.register(r'asesores',       AsesorBancarioViewSet,            basename='asesor')
router.register(r'contactos',      ContactoAsesorViewSet,            basename='contacto')
router.register(r'leads',          LeadViewSet,                      basename='lead')
router.register(r'conversaciones', ConversacionUsuarioAsesorViewSet, basename='conversacion')
router.register(r'creditos',       CreditoDesembolsadoViewSet,       basename='credito')
router.register(r'transacciones',  TransaccionComisionViewSet,       basename='transaccion')

urlpatterns = router.urls
 