from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Paciente
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import PacienteForm,MedicionForm
from django.http import HttpResponse,HttpResponseRedirect
import json
from datetime import date
import datetime
from mediciones.models import Medicion
from decimal import Decimal

# Create your views here.

class PacientesViews(ListView):


    model = Paciente
    template_name = "pacientes/pacienteslist.html"

def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year = today.year)

        # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year = today.year,
                                month = born.month + 1, day = 1)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


def pacienteficha(request,**kwargs):
    from .models import Paciente
    paciente = Paciente.objects.get(pk=kwargs['pk'])
    edad=calculateAge(paciente.fecha_nacimiento)
    fechas=[]
    pesos=[]
    pesos_objetivos=[]


    for consulta in Medicion.objects.filter(paciente=paciente):
        fechas.append(str(consulta.fecha.strftime("%d-%m-%y")))
        pesos.append(float(consulta.peso))
    i=0
    while i < len(Medicion.objects.filter(paciente=paciente)):
        pesos_objetivos.append(float(paciente.peso_objetivo))
        i+=1


    fechas=json.dumps(fechas[::-1])
    pesos=pesos[::-1]




    if request.method== 'POST' and 'nuevamedida' in request.POST:
            from datetime import datetime
            formmedicion=MedicionForm(request.POST)
            if formmedicion.is_valid():
                paciente = Paciente.objects.get(pk=kwargs['pk'])
                objeto=formmedicion.save(commit=False)
                objeto.paciente=paciente
                objeto.save()
                formmedicion=MedicionForm()
                return render(request,'pacientes/datospaciente.html',{'fechas':fechas,'pesos':pesos,'peso_objetivo':pesos_objetivos,'edad':edad,'formmedicion':formmedicion,'paciente':paciente})
    formmedicion =MedicionForm()
    return render(request,'pacientes/datospaciente.html',{'fechas':fechas,'pesos':pesos,'peso_objetivo':pesos_objetivos,'edad':edad,'formmedicion':formmedicion,'paciente':paciente})



def pacientedelete(request,*args,**kwargs):
    pk=kwargs['pk']
    paciente=Paciente.objects.get(pk=pk)
    paciente.delete()
    return HttpResponseRedirect(reverse('pacientes'))


class PacienteCreate(CreateView):
    template_name = "pacientes/crearpaciente.html"
    model = Paciente
    form_class= PacienteForm
    success_url = reverse_lazy('pacientes')

class PacienteUpdate(UpdateView):
    model = Paciente
    template_name = "pacientes/editarpaciente.html"
    form_class=PacienteForm
    def get_success_url(self):
        return reverse_lazy('paciente', args=[self.object.id])

