from django.db import models

# Create your models here.
class Medicion(models.Model):
    paciente= models.ForeignKey('pacientes.Paciente',on_delete=models.CASCADE, related_name='paciente_mediciones')
    fecha = models.DateField()
    peso = models.DecimalField(blank=True, null=True,max_digits=4, decimal_places=1)
    imc = models.DecimalField(blank=True, null=True,max_digits=4, decimal_places=2)
    perimetro_cintura = models.DecimalField(blank=True, null=True,max_digits=5, decimal_places=2)
    masa_muscular = models.DecimalField(blank=True, null=True,max_digits=4, decimal_places=2)
    grasa_visceral = models.DecimalField(blank=True, null=True,max_digits=4, decimal_places=2)
    grasa_subcutanea = models.DecimalField(blank=True, null=True,max_digits=4, decimal_places=2)
    grasa_kg=models.DecimalField(blank=True, null=True,max_digits=3, decimal_places=1)
    dieta=models.ForeignKey('dietas.Dieta',blank=True, null=True, on_delete=models.SET_NULL, related_name='medicion_dieta')

    class Meta():
        ordering = ['-fecha']

    def __str__(self):
        return ('Medición de {} {} del día {}').format(self.paciente.nombre,self.paciente.apellidos,self.fecha)


    def save(self, *args, **kwargs):
        if self.peso and self.grasa_subcutanea:
            grasa=(self.grasa_subcutanea/100)*self.peso
            self.grasa_kg= round(grasa,1)
            print(self.grasa_kg)
            super().save(*args, **kwargs)

        if self.peso and self.paciente.altura:
            self.imc= self.peso/(self.paciente.altura*self.paciente.altura)
            super().save(*args, **kwargs)

        super().save(*args, **kwargs)
