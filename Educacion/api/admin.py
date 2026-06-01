from django.contrib import admin

from .models import (
    Contenido,
    Leccion,
    ModuloEducativo,
    ProgresoEducativo,
    ProgresoLeccion,
)


admin.site.register(ModuloEducativo)
admin.site.register(Contenido)
admin.site.register(Leccion)
admin.site.register(ProgresoEducativo)
admin.site.register(ProgresoLeccion)
