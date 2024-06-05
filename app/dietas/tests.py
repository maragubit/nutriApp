from django.test import TestCase
from .models import *
# Create your tests here.
 class DietasTest(TestCase):
     def setUp(self):
         self.representacion=Representaciones.objects.create(nombre='representaciontest')
