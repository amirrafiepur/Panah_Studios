from django import forms
from webb.models import Human

class add_human(forms.ModelForm):
    class meta:
        model=Human
        fields=["first_name","last_name"]