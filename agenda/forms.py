from django import forms
from django.core.exceptions import ValidationError


class EventAdminForm(forms.ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['end_time'] <= cleaned_data['start_time']:
            raise ValidationError("End time should be after start time")
        super(EventAdminForm, self).clean()
        return cleaned_data
