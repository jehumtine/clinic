from django import forms
from .models import patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ['patient_id','name','initials','sex','address','post_card','admission','DOB','ward_id','next_of_kin']
        labels = {
            'patient_id':'Patient ID',
            'name': 'Name',
            'initials': 'Initials',
            'sex': 'SEX',
            'address':'Address',
            'post_card':'Post Card',
            'admission': 'Admission',
            'DOB':'Date Of Birth',
            'ward_id': 'Ward ID',
            'next_of_kin':'Next of Kin'
        }
        widgets= {
            'patient_id':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'initials': forms.TextInput(attrs={'class':'form-control'}),
            'sex': forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'post_card':forms.TextInput(attrs={'class':'form-control'}),
            'admission': forms.TextInput(attrs={'class':'form-control'}),
            'DOB':forms.DateInput(attrs={'class':'form-control'}),
            'ward_id': forms.TextInput(attrs={'class':'form-control'}),
            'next_of_kin':forms.TextInput(attrs={'class':'form-control'}),
        }   