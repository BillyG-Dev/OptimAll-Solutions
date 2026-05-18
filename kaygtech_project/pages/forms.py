from django import forms
from .models import DeploymentBrief

class DeploymentBriefForm(forms.ModelForm):
    class Meta:
        model = DeploymentBrief
        fields = ['name', 'email', 'service', 'message']
