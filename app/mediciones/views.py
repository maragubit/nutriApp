from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from pacientes.forms import MedicionForm
from mediciones.models import Medicion

# Create your views here.
def mediciondelete(request,*args,**kwargs):
    pk=kwargs['pk']
    medicion=Medicion.objects.get(pk=pk)
    paciente=medicion.paciente.pk
    medicion.delete()
    return HttpResponseRedirect(reverse('paciente', args=[paciente]))




class MedicionUpdate(UpdateView):
    model = Medicion
    template_name = "mediciones/editarmedicion.html"
    form_class= MedicionForm
    def get_success_url(self):
        return reverse_lazy('paciente', args=[self.object.paciente.id])