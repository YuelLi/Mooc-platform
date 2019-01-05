import re
from django import forms
from operation.models import UserConsult


class UserConsultForm(forms.ModelForm):

    class Meta:
        model= UserConsult
        fields=['name','mobile','course_name']

    def clean_mobile(self):
        mobile =self.cleaned_data['mobile']
        REGEX_MOBILE='(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
        p=re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("invalid phone number")