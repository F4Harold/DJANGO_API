from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "categoria"


class MovimientoIngresoEgreso(models.Model):
    id_movimiento_dinero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    es_ingreso = models.BooleanField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "movimiento_ingreso_egreso"


class TipoIngreso(models.Model):
    id_tipo_ingreso = models.AutoField(primary_key=True)
    id_movimiento_dinero = models.ForeignKey(
        MovimientoIngresoEgreso,
        on_delete=models.CASCADE,
        db_column="id_movimiento_dinero",
        null=True,
        blank=True,
    )
    nombre_movimiento_pago = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_movimiento_pago

    class Meta:
        db_table = "tipo_ingreso"


class Finanzas(models.Model):
    id_finanzas = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_movimiento_dinero = models.ForeignKey(
        MovimientoIngresoEgreso,
        on_delete=models.CASCADE,
        db_column="id_movimiento_dinero",
        null=True,
        blank=True,
    )
    id_categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        db_column="id_categoria",
        null=True,
        blank=True,
    )
    monto_presupuesto = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    gasto = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    disponible = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    fecha = models.DateField(default=timezone.localdate)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Finanzas usuario {self.id_usuario}"

    class Meta:
        db_table = "finanzas"


class TipoInversion(models.Model):
    id_tipo_inversion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "tipo_inversion"


class NivelRiesgo(models.Model):
    id_nivel_riesgo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "nivel_riesgo"


class MovimientoInversion(models.Model):
    id_movimiento_dinero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    es_ingreso = models.BooleanField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "movimiento_inversion"


class TipoIngresoInversion(models.Model):
    id_tipo_ingreso = models.AutoField(primary_key=True)
    id_movimiento_dinero = models.ForeignKey(
        MovimientoInversion,
        on_delete=models.CASCADE,
        db_column="id_movimiento_dinero",
        null=True,
        blank=True,
    )
    nombre_movimiento_pago = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_movimiento_pago

    class Meta:
        db_table = "tipo_ingreso_inversion"


class Inversion(models.Model):
    id_inversion = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_tipo_inversion = models.ForeignKey(
        TipoInversion,
        on_delete=models.CASCADE,
        db_column="id_tipo_inversion",
    )
    id_nivel_riesgo = models.ForeignKey(
        NivelRiesgo,
        on_delete=models.CASCADE,
        db_column="id_nivel_riesgo",
    )
    id_movimiento_dinero = models.ForeignKey(
        MovimientoInversion,
        on_delete=models.CASCADE,
        db_column="id_movimiento_dinero",
        null=True,
        blank=True,
    )
    nombre = models.CharField(max_length=120, null=True, blank=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    rentabilidad = models.DecimalField(max_digits=8, decimal_places=4, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre or f"Inversion {self.id_inversion}"

    class Meta:
        db_table = "inversion"


class EditarMeta(models.Model):
    id_editar_meta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, null=True, blank=True)
    monto_actual = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    monto_objetivo = models.DecimalField(max_digits=18, decimal_places=2)
    ahorro_mensual = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    fecha_objetivo = models.DateField(default=timezone.localdate)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre or f"Meta editable {self.id_editar_meta}"

    class Meta:
        db_table = "editar_meta"


class MovimientoMeta(models.Model):
    id_movimiento_dinero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    es_ingreso = models.BooleanField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "movimiento_meta"


class TipoIngresoMeta(models.Model):
    id_tipo_ingreso = models.AutoField(primary_key=True)
    id_movimiento_dinero = models.ForeignKey(
        MovimientoMeta,
        on_delete=models.CASCADE,
        db_column="id_movimiento_dinero",
        null=True,
        blank=True,
    )
    nombre_movimiento_pago = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_movimiento_pago

    class Meta:
        db_table = "tipo_ingreso_meta"


class Meta(models.Model):
    id_meta = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_editar_meta = models.ForeignKey(
        EditarMeta,
        on_delete=models.CASCADE,
        db_column="id_editar_meta",
    )
    id_movimiento_dinero = models.ForeignKey(
        MovimientoMeta,
        on_delete=models.CASCADE,
        db_column="id_movimiento_dinero",
        null=True,
        blank=True,
    )
    nombre = models.CharField(max_length=120, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    monto_objetivo = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    monto_actual = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    fecha_limite = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre or f"Meta {self.id_meta}"

    class Meta:
        db_table = "meta"
