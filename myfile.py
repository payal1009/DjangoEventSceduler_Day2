from django import forms

class eventform(forms.Form):
    i=forms.Index()
    name=forms.CharField()
    date=forms.DateField()
    time=forms.TimeField()
    description=forms.CharField()
