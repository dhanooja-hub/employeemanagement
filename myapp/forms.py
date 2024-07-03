from django import forms

class EmpForm(forms.Form):

    name=forms.CharField()

    department=forms.CharField()

    salary=forms.CharField()

    location=forms.CharField()

    email=forms.CharField()

    address=forms.CharField()