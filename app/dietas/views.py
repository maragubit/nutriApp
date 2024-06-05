from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView


# Create your views here.
def dietasindex(request):
    dietas= Dieta.objects.all()
    platos=Plato.objects.all()
    representaciones=Representaciones.objects.all()
    return render(request,'dietas/dietasindex.html',{'dietas':dietas,'platos':platos,'representaciones':representaciones})

#Vistas de representaciones:

      #crear representacion


class RepresentacionCreate(CreateView):
    model=Representaciones
    form_class= RepresentacionForm
    template_name="dietas/crear_representacion.html"
    success_url = reverse_lazy('dietasindex')

class RepresentacionUpdate(UpdateView):
    model=Representaciones
    form_class= RepresentacionForm
    template_name="dietas/editar_representacion.html"
    def get_success_url(self):
        return reverse_lazy('dietasindex')+'#representaciones'

def representaciondelete(request,*args,**kwargs):
    pk=kwargs['pk']
    representacion=Representaciones.objects.get(pk=pk)
    representacion.delete()
    return HttpResponseRedirect(reverse('dietasindex')+'#representaciones')

class PlatoCreate(CreateView):
    model=Plato
    form_class= PlatoForm
    template_name="dietas/crear_plato.html"

    def get_success_url(self):
        return reverse_lazy('crear_plato') + '?ok'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['representaciones'] = Representaciones.objects.all()
        return context
class PlatoUpdate(UpdateView):
    model=Plato
    form_class= PlatoForm
    template_name="dietas/editar_plato.html"
    def get_success_url(self):
        return reverse_lazy('dietasindex')+'#platos'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['representaciones'] = Representaciones.objects.all()
        return context


class DietaCreate(CreateView):
    model=Dieta
    form_class= DietaForm
    template_name="dietas/crear_dieta.html"
    def get_success_url(self):
        return reverse_lazy('dietasindex')+'#platos'

def platodelete(request,*args,**kwargs):
    pk=kwargs['pk']
    plato=Plato.objects.get(pk=pk)
    plato.delete()
    return HttpResponseRedirect(reverse('dietasindex')+'#platos')

class DietaUpdate(UpdateView):
    model=Dieta
    form_class= DietaForm
    template_name="dietas/editar_dieta.html"
    def get_success_url(self):
        return reverse_lazy('ver_dieta',args=[self.object.id])


class DietaDetailView(DetailView):

    model = Dieta
    template_name='dietas/ver_dieta.html'

def dietadelete(request,*args,**kwargs):
    pk=kwargs['pk']
    dieta=Dieta.objects.get(pk=pk)
    dieta.delete()
    return HttpResponseRedirect(reverse('dietasindex'))

def crearnuevadeotradieta(request,*args,**kwargs):
    pk=kwargs['pk']
    dieta=Dieta.objects.get(pk=pk)
    form= DietaForm(instance=dieta)
    if request.method == 'POST':
        form=DietaForm(request.POST)
        if form.is_valid():
            form.save()
            dieta=Dieta.objects.first()
            dietapk=dieta.id
            return HttpResponseRedirect(reverse('ver_dieta', args=[dietapk]))



    return render(request,'dietas/crearnuevadeotra.html',{'form':form})
