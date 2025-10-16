from django import forms
from .models import Estado, Municipio

class LocalidadForm(forms.Form):
    estado = forms.ModelChoiceField(queryset=Estado.objects.all())
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si el estado fue enviado, ajustar el queryset de municipios
        if 'estado' in self.data:
            try:
                estado_id = int(self.data.get('estado'))
                self.fields['municipio'].queryset = Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.initial.get('estado'):
            estado = self.initial.get('estado')
            self.fields['municipio'].queryset = Municipio.objects.filter(estado=estado).order_by('nombre')
