from django.db import models

class Plato(models.Model):
    SI_CHOICES = (
        ('SI','sí'),
        ('NO','no')
        )
    nombre=models.CharField(max_length=100)
    representacion= models.ForeignKey('dietas.Representaciones',null=True,blank=True,related_name='representacion_plato',on_delete=models.SET_NULL)
    ingredientes= models.TextField(blank=True,null=True)
    foto=models.ImageField(upload_to='fotos_platos/',blank=True,null=True)
    desayuno=models.CharField(max_length=5, choices=SI_CHOICES, default='NO')
    media_manana=models.CharField(max_length=5, choices=SI_CHOICES, default='NO')
    postre=models.CharField(max_length=5, choices=SI_CHOICES, default='NO')
    merienda=models.CharField(max_length=5, choices=SI_CHOICES, default='NO')




    def __str__(self):
            return self.nombre
    class Meta():
        ordering=['nombre']


    def save(self,*args,**kwargs):
        self.nombre=self.nombre.capitalize()
        super().save(*args, **kwargs)


class Representaciones(models.Model):
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='fotos_representaciones/',blank=True,null=True)
    descripcion= models.TextField(blank=True,null=True)

    def __str__(self):
            return self.nombre

    def save(self,*args,**kwargs):
        self.nombre=self.nombre.capitalize()
        super().save(*args, **kwargs)

class Dieta(models.Model):
    nombre=models.CharField(max_length=50, unique=True)
    desayuno1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    desayuno2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    desayuno3=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1b_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1b_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1b_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1b_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1b_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1b_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1b_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia1b_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2b_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2b_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2b_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2b_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2b_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2b_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2b_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia2b_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3b_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3b_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3b_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3b_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3b_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3b_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3b_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia3b_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4b_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4b_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4b_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4b_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4b_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4b_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4b_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia4b_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5b_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5b_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5b_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5b_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5b_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5b_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5b_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia5b_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6b_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6b_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6b_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6b_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6b_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6b_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6b_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia6b_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7b_media_manana=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7b_almuerzo1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7b_almuerzo2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7b_postre_almuerzo=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7b_merienda=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7b_cena1=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7b_cena2=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    dia7b_postre_cena=models.ForeignKey('dietas.Plato',related_name='+',null=True,blank=True,on_delete=models.SET_NULL)
    descripcion= models.TextField(blank=True,null=True)

    def __str__(self):
        return self.nombre
    class Meta():
        ordering=['nombre']


    def save(self,*args,**kwargs):
        self.nombre=self.nombre.capitalize()
        super().save(*args, **kwargs)