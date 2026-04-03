from django import forms
from .models import Info

GENDER=(
    ('male','male'),
    ('female','female'),
    ('LGBTQ','LGBTQ')
)
class InfoForm(forms.ModelForm):
    class Meta:
        model=Info
        fields='__all__'
        labels={
            'name':'Full Name',
            'email':'Email',
            'country':'Country',
            'address':'Address',
            'phone':'Phone',
            'gender':'Gender'
        }
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'email':forms.EmailInput(attrs={'class':'form-control','type':'email'}),
            'country':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'address':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'phone':forms.TextInput(attrs={'class':'form-control','type':'text'}),
            'gender':forms.RadioSelect(choices=GENDER)
        }