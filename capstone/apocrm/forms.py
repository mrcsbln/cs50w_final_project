from django import forms 
from .models import Patient

class PatientForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=['%d.%m.%Y'], 
        widget=forms.DateInput(
            format='%d.%m.%Y', 
            attrs={'class': 'form-control datepicker', 'type': 'text'}
        )
    )
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'text'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'case_description': forms.Textarea(attrs={'class': 'form-control'}),
        }





