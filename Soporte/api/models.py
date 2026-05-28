from django.db import models


# modelo tabla estado_pqr
class EstadoPqr(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        # tabla sql
        db_table = 'soporte\".\"estado_pqr'


# modelo tabla pqr
class Pqr(models.Model):
    id_pqr = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    descripcion = models.TextField()
    id_estado = models.ForeignKey(
        EstadoPqr,
        on_delete=models.RESTRICT,
        db_column='id_estado'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PQR {self.id_pqr}"

    class Meta:
        # tabla sql
        db_table = 'soporte\".\"pqr'


# modelo tabla adjunto
class Adjunto(models.Model):
    id_adjunto = models.AutoField(primary_key=True)
    id_pqr = models.ForeignKey(
        Pqr,
        on_delete=models.RESTRICT,
        db_column='id_pqr'
    )
    nombre_archivo = models.CharField(max_length=255)
    ruta_archivo = models.CharField(max_length=500, null=True, blank=True)
    tipo_mime = models.CharField(max_length=100, null=True, blank=True)
    tamano_bytes = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_archivo

    class Meta:
        # tabla sql
        db_table = 'soporte\".\"adjunto'


# modelo tabla registro_actividad
class RegistroActividad(models.Model):
    id_registro = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    tipo_actividad = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    entidad_afectada = models.CharField(max_length=100, null=True, blank=True)
    fecha_actividad = models.DateTimeField(auto_now_add=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registro {self.id_registro} - {self.tipo_actividad}"

    class Meta:
        # tabla sql
        db_table = 'soporte\".\"registro_actividad'