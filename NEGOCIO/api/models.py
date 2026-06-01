# models/negocio.py

from django.db import models


# ── negocio.banco ─────────────────────────────────────────────
class Banco(models.Model):
    ESTADO_CHOICES = [
        ('activo',   'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    id_banco             = models.AutoField(primary_key=True)
    nombre_banco         = models.CharField(max_length=100, unique=True)
    ciudad               = models.CharField(max_length=100, blank=True, null=True)
    contacto             = models.CharField(max_length=100, blank=True, null=True)
    telefono             = models.CharField(max_length=20,  blank=True, null=True)
    email                = models.EmailField(max_length=150, blank=True, null=True)
    comision_porcentaje  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    url_logo             = models.CharField(max_length=500, blank=True, null=True)
    descripcion          = models.TextField(blank=True, null=True)
    sitio_web            = models.CharField(max_length=300, blank=True, null=True)
    estado               = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    fecha_registro       = models.DateTimeField(auto_now_add=True)
    activo               = models.BooleanField(default=True)
    fecha_creacion       = models.DateTimeField(auto_now_add=True)
    fecha_modificacion   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_banco

    class Meta:
        db_table = 'negocio\".\"banco'


# ── negocio.producto_crediticio ───────────────────────────────
class ProductoCrediticio(models.Model):
    id_producto      = models.AutoField(primary_key=True)
    id_banco         = models.ForeignKey(
        Banco,
        on_delete=models.RESTRICT,
        db_column='id_banco'
    )
    nombre_producto  = models.CharField(max_length=150)
    descripcion      = models.TextField(blank=True, null=True)
    monto_minimo     = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    monto_maximo     = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tasa_minima      = models.DecimalField(max_digits=5,  decimal_places=2, blank=True, null=True)
    tasa_maxima      = models.DecimalField(max_digits=5,  decimal_places=2, blank=True, null=True)
    plazo_minimo     = models.IntegerField(blank=True, null=True)
    plazo_maximo     = models.IntegerField(blank=True, null=True)
    requisitos       = models.TextField(blank=True, null=True)
    activo           = models.BooleanField(default=True)
    fecha_creacion   = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'negocio\".\"producto_crediticio'


# ── negocio.asesor_bancario ───────────────────────────────────
class AsesorBancario(models.Model):
    id_asesor          = models.AutoField(primary_key=True)
    id_banco           = models.ForeignKey(
        Banco,
        on_delete=models.RESTRICT,
        db_column='id_banco'
    )
    nombre             = models.CharField(max_length=100)
    apellido           = models.CharField(max_length=100)
    email              = models.EmailField(max_length=150)
    telefono           = models.CharField(max_length=20, blank=True, null=True)
    especialidad       = models.CharField(max_length=100, blank=True, null=True)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = 'negocio\".\"asesor_bancario'


# ── negocio.contacto_asesor ───────────────────────────────────
class ContactoAsesor(models.Model):
    id_contacto        = models.AutoField(primary_key=True)
    id_asesor          = models.ForeignKey(
        AsesorBancario,
        on_delete=models.RESTRICT,
        db_column='id_asesor'
    )
    whatsapp           = models.CharField(max_length=20,  blank=True, null=True)
    email              = models.EmailField(max_length=150, blank=True, null=True)
    telefono           = models.CharField(max_length=20,  blank=True, null=True)
    disponible_desde   = models.TimeField(blank=True, null=True)
    disponible_hasta   = models.TimeField(blank=True, null=True)
    dias_disponibles   = models.CharField(max_length=100, blank=True, null=True)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contacto asesor {self.id_asesor_id}"

    class Meta:
        db_table = 'negocio\".\"contacto_asesor'


# ── negocio.lead ──────────────────────────────────────────────
class Lead(models.Model):
    ESTADO_CHOICES = [
        ('nuevo',       'Nuevo'),
        ('contactado',  'Contactado'),
        ('en_proceso',  'En proceso'),
        ('aprobado',    'Aprobado'),
        ('rechazado',   'Rechazado'),
        ('cancelado',   'Cancelado'),
    ]

    id_lead            = models.AutoField(primary_key=True)
    id_usuario         = models.IntegerField()              # FK a auth.usuario (esquema externo)
    id_producto        = models.ForeignKey(
        ProductoCrediticio,
        on_delete=models.RESTRICT,
        db_column='id_producto'
    )
    id_asesor          = models.ForeignKey(
        AsesorBancario,
        on_delete=models.RESTRICT,
        db_column='id_asesor',
        blank=True, null=True
    )
    tipo_credito       = models.CharField(max_length=100, blank=True, null=True)
    monto_interes      = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    plazo_interes      = models.IntegerField(blank=True, null=True)
    estado_lead        = models.CharField(max_length=30, choices=ESTADO_CHOICES, default='nuevo')
    fecha_generacion   = models.DateTimeField(auto_now_add=True)
    fecha_contacto     = models.DateTimeField(blank=True, null=True)
    observaciones      = models.TextField(blank=True, null=True)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lead {self.id_lead} - {self.estado_lead}"

    class Meta:
        db_table = 'negocio\".\"lead'


# ── negocio.conversacion_usuario_asesor ───────────────────────
class ConversacionUsuarioAsesor(models.Model):
    TIPO_CONTACTO_CHOICES = [
        ('email',      'Email'),
        ('telefono',   'Teléfono'),
        ('whatsapp',   'WhatsApp'),
        ('presencial', 'Presencial'),
    ]

    id_conversacion    = models.AutoField(primary_key=True)
    id_lead            = models.ForeignKey(
        Lead,
        on_delete=models.RESTRICT,
        db_column='id_lead'
    )
    id_usuario         = models.IntegerField()              # FK a auth.usuario (esquema externo)
    id_asesor          = models.ForeignKey(
        AsesorBancario,
        on_delete=models.RESTRICT,
        db_column='id_asesor'
    )
    tipo_contacto      = models.CharField(max_length=30, choices=TIPO_CONTACTO_CHOICES, default='email')
    asunto             = models.CharField(max_length=200, blank=True, null=True)
    contenido          = models.TextField(blank=True, null=True)
    fecha_mensaje      = models.DateTimeField(auto_now_add=True)
    activo             = models.BooleanField(default=True)
    fecha_creacion     = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversación {self.id_conversacion} - Lead {self.id_lead_id}"

    class Meta:
        db_table = 'negocio\".\"conversacion_usuario_asesor'


# ── negocio.credito_desembolsado ──────────────────────────────
class CreditoDesembolsado(models.Model):
    ESTADO_CHOICES = [
        ('activo',    'Activo'),
        ('pagado',    'Pagado'),
        ('vencido',   'Vencido'),
        ('cancelado', 'Cancelado'),
    ]

    id_credito           = models.AutoField(primary_key=True)
    id_lead              = models.ForeignKey(
        Lead,
        on_delete=models.RESTRICT,
        db_column='id_lead'
    )
    id_usuario           = models.IntegerField()            # FK a auth.usuario (esquema externo)
    id_producto          = models.ForeignKey(
        ProductoCrediticio,
        on_delete=models.RESTRICT,
        db_column='id_producto'
    )
    id_banco             = models.ForeignKey(
        Banco,
        on_delete=models.RESTRICT,
        db_column='id_banco'
    )
    numero_credito       = models.CharField(max_length=50, unique=True, blank=True, null=True)
    monto_aprobado       = models.DecimalField(max_digits=12, decimal_places=2)
    tasa_interes_final   = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    plazo_meses          = models.IntegerField(blank=True, null=True)
    fecha_aprobacion     = models.DateField(blank=True, null=True)
    fecha_desembolso     = models.DateField(blank=True, null=True)
    estado_credito       = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    saldo_actual         = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    activo               = models.BooleanField(default=True)
    fecha_creacion       = models.DateTimeField(auto_now_add=True)
    fecha_modificacion   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Crédito {self.numero_credito or self.id_credito}"

    class Meta:
        db_table = 'negocio\".\"credito_desembolsado'


# ── negocio.transaccion_comision ──────────────────────────────
class TransaccionComision(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagada',    'Pagada'),
        ('cancelada', 'Cancelada'),
    ]

    id_transaccion       = models.AutoField(primary_key=True)
    id_credito           = models.ForeignKey(
        CreditoDesembolsado,
        on_delete=models.RESTRICT,
        db_column='id_credito'
    )
    id_banco             = models.ForeignKey(
        Banco,
        on_delete=models.RESTRICT,
        db_column='id_banco'
    )
    monto_comision       = models.DecimalField(max_digits=12, decimal_places=2)
    porcentaje_aplicado  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fecha_transaccion    = models.DateTimeField(auto_now_add=True)
    estado               = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    referencia_pago      = models.CharField(max_length=100, blank=True, null=True)
    activo               = models.BooleanField(default=True)
    fecha_creacion       = models.DateTimeField(auto_now_add=True)
    fecha_modificacion   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comisión {self.id_transaccion} - {self.estado}"

    class Meta:
        db_table = 'negocio\".\"transaccion_comision'