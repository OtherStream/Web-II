from django.shortcuts import render
from django.http import JsonResponse
from .models import Estado, Municipio
from .forms import LocalidadForm

def formulario_localidad(request):
    form = LocalidadForm()
    return render(request, 'localidades/localidad_forms.html', {'form': form})

def ajax_obtener_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = []
    if estado_id:
        municipios_qs = Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
        municipios = list(municipios_qs.values('id', 'nombre'))
    return JsonResponse({'municipios': municipios})
