from django.urls import path
from . import views

urlpatterns = [
    path('localidad-form/', views.formulario_localidad, name='localidad_forms'),
    path('ajax/municipios/', views.ajax_obtener_municipios, name='ajax_municipios'),
]
