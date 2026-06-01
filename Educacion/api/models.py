from django.db import models


class ModuloEducativo(models.Model):
    NIVEL_BASICO = "basico"
    NIVEL_INTERMEDIO = "intermedio"
    NIVEL_AVANZADO = "avanzado"

    NIVEL_CHOICES = [
        (NIVEL_BASICO, "Basico"),
        (NIVEL_INTERMEDIO, "Intermedio"),
        (NIVEL_AVANZADO, "Avanzado"),
    ]

    id_modulo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    contenido = models.TextField(null=True, blank=True)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default=NIVEL_BASICO)
    url_thumbnail = models.CharField(max_length=500, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "modulo_educativo"


class Contenido(models.Model):
    id_contenido = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    duracion_minutos = models.IntegerField(null=True, blank=True)
    url_video = models.CharField(max_length=500, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "contenido"


class Leccion(models.Model):
    id_leccion = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(
        ModuloEducativo,
        on_delete=models.CASCADE,
        db_column="id_modulo",
    )
    id_contenido = models.ForeignKey(
        Contenido,
        on_delete=models.CASCADE,
        db_column="id_contenido",
        null=True,
        blank=True,
    )
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    duracion_minutos = models.IntegerField(null=True, blank=True)
    url_video = models.CharField(max_length=500, null=True, blank=True)
    numero_leccion = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "leccion"


class ProgresoEducativo(models.Model):
    id_progreso = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_modulo = models.ForeignKey(
        ModuloEducativo,
        on_delete=models.CASCADE,
        db_column="id_modulo",
    )
    porcentaje_completado = models.IntegerField(default=0)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_completado = models.DateTimeField(null=True, blank=True)
    calificacion = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Progreso usuario {self.id_usuario} - modulo {self.id_modulo_id}"

    class Meta:
        db_table = "progreso_educativo"
        unique_together = ("id_usuario", "id_modulo")


class ProgresoLeccion(models.Model):
    id_progreso_leccion = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        db_column="id_leccion",
    )
    completado = models.BooleanField(default=False)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_completado = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Progreso usuario {self.id_usuario} - leccion {self.id_leccion_id}"

    class Meta:
        db_table = "progreso_leccion"
        unique_together = ("id_usuario", "id_leccion")
