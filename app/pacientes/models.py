from django.db import models

# Create your models here.
class Paciente (models.Model):

    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(max_length=75, blank=True, null=True)
    observaciones = models.TextField(blank=True,null=True)
    enfermedades = models.TextField(blank=True,null=True)
    medicamentos = models.TextField(blank=True,null=True)
    actividad_fisica=models.TextField(blank=True,null=True)
    telefono= models.CharField(max_length=100, blank=True, null=True)
    altura = models.DecimalField(blank=True, null=True,max_digits=3, decimal_places=2)
    peso_inicial=models.DecimalField(blank=True, null=True,max_digits=4, decimal_places=1)
    peso_objetivo=models.DecimalField(blank=True, null=True,max_digits=4, decimal_places=1)
    foto_inicial=models.ImageField(upload_to='fotos_pacientes/',blank=True,null=True)

    def save(self, *args, **kwargs):
        if self.altura:
            self.peso_objetivo= 25*(self.altura*self.altura)
            super().save(*args, **kwargs)



        super().save(*args, **kwargs)



    def __str__(self):
        return ('{} {}').format(self.nombre,self.apellidos)
