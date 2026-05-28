from django.db import models



class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.nombre_rol

    class Meta:
        db_table = '"auth"."rol"'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

   


class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10, unique=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = '"auth"."tipo_documento"'
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'

    def __str__(self):
        return f'{self.nombre} ({self.codigo})'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    tipo_documento = models.ForeignKey(
        TipoDocumento,
        on_delete=models.CASCADE,
        db_column='tipo_documento',
        null=True,
        blank=True
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    cedula = models.CharField(max_length=50, unique=True, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    fecha_registro = models.DateTimeField(auto_now_add=True, null=True)
    fecha_ultima_sesion = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = '"auth"."usuario"'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Credencial(models.Model):
    id_credencial = models.AutoField(primary_key=True)
    id_usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario'
    )
    contrasena_hash = models.CharField(max_length=255)
    salt = models.CharField(max_length=100)
    algoritmo = models.CharField(max_length=20, choices=ALGORITMO_CHOICES, default='bcrypt')
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True)
    fecha_ultimo_cambio = models.DateTimeField(null=True, blank=True)
    intentos_fallidos = models.IntegerField(default=0)
    bloqueado_hasta = models.DateTimeField(null=True, blank=True)
    requiere_cambio = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = '"auth"."credencial"'
        verbose_name = 'Credencial'
        verbose_name_plural = 'Credenciales'

    def __str__(self):
        return f'Credencial de {self.id_usuario}'


class UsuarioRol(models.Model):
    id_usuario_rol = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario'
    )
    id_rol = models.ForeignKey(
        Rol,
        on_delete=models.CASCADE,
        db_column='id_rol'
    )
    fecha_asignacion = models.DateTimeField(auto_now_add=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = '"auth"."usuario_rol"'
        unique_together = (('id_usuario', 'id_rol'),)
        verbose_name = 'Usuario Rol'
        verbose_name_plural = 'Usuarios Roles'

    def __str__(self):
        return f'{self.id_usuario} → {self.id_rol}'


class AuditoriaLogin(models.Model):
    id_auditoria = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        db_column='id_usuario'
    )
    tipo_evento = models.CharField(max_length=30, choices=TIPO_EVENTO_CHOICES, default='login')
    ip_address = models.CharField(max_length=45, null=True, blank=True)
    navegador = models.CharField(max_length=200, null=True, blank=True)
    fecha_evento = models.DateTimeField(auto_now_add=True, null=True)
    estado_evento = models.CharField(max_length=20, choices=ESTADO_EVENTO_CHOICES, default='exitoso')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '"auth"."auditoria_login"'
        verbose_name = 'Auditoría Login'
        verbose_name_plural = 'Auditorías Login'

    def __str__(self):
        return f'{self.tipo_evento} - {self.id_usuario} ({self.estado_evento})'