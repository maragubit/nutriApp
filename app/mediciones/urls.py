from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('borrar/<int:pk>',views.mediciondelete, name='borrarmedicion'),
    path('editar/<int:pk>',MedicionUpdate.as_view(), name='editarmedicion'),
]