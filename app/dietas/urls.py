from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.dietasindex, name='dietasindex'),
    path('crear/representacion',RepresentacionCreate.as_view(), name='crear_representacion'),
    path('crear/plato',PlatoCreate.as_view(), name='crear_plato'),
    path('crear/dieta',DietaCreate.as_view(), name='crear_dieta'),
    path('editar/dieta/<int:pk>',DietaUpdate.as_view(), name='editar_dieta'),
    path('ver/dieta/<int:pk>',DietaDetailView.as_view(), name='ver_dieta'),
    path('editar/dietadedieta/<int:pk>',views.crearnuevadeotradieta, name='crearnuevadeotra'),
    path('borrar/dieta/<int:pk>',views.dietadelete, name='borrar_dieta'),
    path('editar/plato/<int:pk>',PlatoUpdate.as_view(), name='editar_plato'),
    path('borrar/plato/<int:pk>',views.platodelete, name='borrar_plato'),
    path('editar/representacion/<int:pk>',RepresentacionUpdate.as_view(), name='editar_representacion'),
    path('borrar/plato/<int:pk>',views.representaciondelete, name='borrar_representacion'),








]