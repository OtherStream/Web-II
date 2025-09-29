from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Orden
from .forms import OrdenForm

class OrdenCreateView(View):
    def get(self, request):
        form = OrdenForm()
        return render(request, "forms/orden_form.html", {"form": form})

    def post(self, request):
        form = OrdenForm(request.POST, request.FILES)
        if form.is_valid():
            orden = form.save()
            return redirect("orden_detail", pk=orden.pk)
        return render(request, "forms/orden_form.html", {"form": form})

def orden_detail(request, pk):
    orden = get_object_or_404(Orden, pk=pk)

    if request.method == "POST" and "delete" in request.POST:
        orden.delete()
        return redirect("orden_list")  

    return render(request, "forms/orden_detail.html", {"orden": orden})

def orden_list(request):
    ordenes = Orden.objects.all()
    return render(request, "forms/orden_list.html", {"ordenes": ordenes})
