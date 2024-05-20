from django import forms

class PingForm(forms.Form):
    ip_address = forms.CharField(label='ip_address', max_length=50)