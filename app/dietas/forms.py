from .models import *
from django import forms
from django.forms import SelectDateWidget


class RepresentacionForm(forms.ModelForm):
    class Meta:
        model = Representaciones
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(RepresentacionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'



class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(PlatoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'



class DietaForm(forms.ModelForm):
    desayuno1=forms.ModelChoiceField(queryset=Plato.objects.filter(desayuno='SI'),required = False)
    desayuno2=forms.ModelChoiceField(queryset=Plato.objects.filter(desayuno='SI'),required = False)
    desayuno3=forms.ModelChoiceField(queryset=Plato.objects.filter(desayuno='SI'),required = False)
    dia1_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia1_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia2_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia3_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia4_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia5_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia6_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia7_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia1_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia2_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia3_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia4_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia5_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia6_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia7_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia1_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia2_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia3_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia4_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia5_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia6_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia7_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia1_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia2_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia3_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia4_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia5_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia6_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia7_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia1b_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia1b_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia2b_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia3b_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia4b_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia5b_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia6b_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia7b_media_manana=forms.ModelChoiceField(queryset=Plato.objects.filter(media_manana='SI'),required = False)
    dia1b_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia2b_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia3b_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia4b_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia5b_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia6b_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia7b_postre_almuerzo=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia1b_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia2b_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia3b_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia4b_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia5b_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia6b_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia7b_merienda=forms.ModelChoiceField(queryset=Plato.objects.filter(merienda='SI'),required = False)
    dia1b_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia2b_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia3b_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia4b_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia5b_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia6b_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)
    dia7b_postre_cena=forms.ModelChoiceField(queryset=Plato.objects.filter(postre='SI'),required = False)








    class Meta:
        model = Dieta
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(DietaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'
