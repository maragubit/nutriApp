from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',PacientesViews.as_view(), name='pacientes'),
    path('paciente/<int:pk>',views.pacienteficha, name='paciente'),
    path('paciente/borrar/<int:pk>',views.pacientedelete, name='borrarpaciente'),
    path('paciente/crear',PacienteCreate.as_view(), name='crearpaciente'),
    path('paciente/editar/<int:pk>',PacienteUpdate.as_view(), name='editarpaciente'),





]