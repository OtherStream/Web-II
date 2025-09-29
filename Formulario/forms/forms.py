from django import forms
from .models import Orden

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = [
            "numero_orden", "modelo", "color",
            "talla_inicio", "talla_fin", "total_piezas",
            "foto_modelo", "especificaciones_pdf"
        ]

    def clean_foto_modelo(self):
        foto = self.cleaned_data.get("foto_modelo")
        if foto:
            if not foto.content_type in ["image/jpeg", "image/png"]:
                raise forms.ValidationError("La foto del modelo debe ser JPG o PNG.")
        return foto

    def clean_especificaciones_pdf(self):
        pdf = self.cleaned_data.get("especificaciones_pdf")
        if pdf:
            if pdf.content_type != "application/pdf":
                raise forms.ValidationError("El archivo de especificaciones debe ser un PDF.")
        return pdf