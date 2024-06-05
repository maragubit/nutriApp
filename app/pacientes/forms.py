from .models import Paciente
from mediciones.models import Medicion
from django import forms
import datetime
from django.forms import SelectDateWidget


class PacienteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=SelectDateWidget(years=range(1900, 2020),
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),)
    altura=forms.DecimalField()
    peso_inicial=forms.DecimalField()
    class Meta:
        model = Paciente
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'

class MedicionForm(forms.ModelForm):
    fecha=forms.DateField(widget=SelectDateWidget(
                                                  empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                                  ),initial=datetime.date.today())
    class Meta:
        model = Medicion
        fields = ('fecha','peso','perimetro_cintura','masa_muscular','grasa_visceral','grasa_subcutanea','dieta',)



    def __init__(self, *args, **kwargs):
        super(MedicionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'