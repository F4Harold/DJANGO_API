from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoriaViewSet,
    EditarMetaViewSet,
    FinanzasViewSet,
    InversionViewSet,
    MetaViewSet,
    MovimientoIngresoEgresoViewSet,
    MovimientoInversionViewSet,
    MovimientoMetaViewSet,
    NivelRiesgoViewSet,
    TipoIngresoInversionViewSet,
    TipoIngresoMetaViewSet,
    TipoIngresoViewSet,
    TipoInversionViewSet,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"movimientos-ingreso-egreso", MovimientoIngresoEgresoViewSet)
router.register(r"tipos-ingreso", TipoIngresoViewSet)
router.register(r"finanzas", FinanzasViewSet)
router.register(r"tipos-inversion", TipoInversionViewSet)
router.register(r"niveles-riesgo", NivelRiesgoViewSet)
router.register(r"movimientos-inversion", MovimientoInversionViewSet)
router.register(r"tipos-ingreso-inversion", TipoIngresoInversionViewSet)
router.register(r"inversiones", InversionViewSet)
router.register(r"editar-metas", EditarMetaViewSet)
router.register(r"movimientos-meta", MovimientoMetaViewSet)
router.register(r"tipos-ingreso-meta", TipoIngresoMetaViewSet)
router.register(r"metas", MetaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
