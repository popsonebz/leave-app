from django import forms
from django.contrib.auth.models import User
from functools import partial
from Hr import settings


DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class EmployeeForm(forms.ModelForm): 
    employment_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password'] 

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(EmployeeForm, self).clean()
        employment_date = cleaned_data.get("employment_date")
        
        return cleaned_data
        
    