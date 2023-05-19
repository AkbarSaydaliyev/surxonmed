from django import forms
from django_json_widget.widgets import JSONEditorWidget
from .models import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization

        fields = ('working_time',)

        widgets = {
            'working_time': JSONEditorWidget
        }