from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    rfc = models.CharField(max_length=120, unique=True)
    direccion = models.CharField(max_length=255)
    foto_cliente = models.ImageField(upload_to='img_clientes/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
        
class Vehiculo(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos')
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    kilometraje = models.PositiveIntegerField()
    foto_vehiculo = models.ImageField(upload_to='img_vehiculos/', blank=True, null=True)


    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.cliente.nombre}"
    
    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"