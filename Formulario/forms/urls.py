from django.urls import path
from .views import OrdenCreateView, orden_detail, orden_list

urlpatterns = [
    path("", orden_list, name="orden_list"),
    path("nueva/", OrdenCreateView.as_view(), name="orden_create"),
    path("orden/<int:pk>/", orden_detail, name="orden_detail"),
]