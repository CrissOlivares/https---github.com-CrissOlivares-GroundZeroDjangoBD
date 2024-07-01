from django import forms
from .models import PaymentInfo,Users

class PaymentInfoForm(forms.ModelForm):
    class Meta:
        model = PaymentInfo
        fields = ['nombre_titular', 'numero_tarjeta', 'fecha_vencimiento', 'cvv']
        widgets = {
            'nombre_titular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Titular'}),
            'numero_tarjeta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Tarjeta'}),
            'fecha_vencimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YY'}),
            'cvv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVV'}),
        }


class RegisterForm(forms.ModelForm):
    confirmacion_contrasena = forms.CharField(widget=forms.PasswordInput(), label="Repite tu contraseña")

    class Meta:
        model = Users
        fields = ['nombre', 'correo', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get("contrasena")
        confirmacion_contrasena = cleaned_data.get("confirmacion_contrasena")

        if contrasena != confirmacion_contrasena:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data