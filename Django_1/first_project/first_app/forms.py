from django import forms
from django.core import validators


# def check_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError('Nmae need ot start with z')


class FormName(forms.Form):
    name = forms.CharField() #validators=[check_for_z]
    email= forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again:')
    text = forms.CharField(widget = forms.Textarea)
    # boatcatcher = forms.CharField(required =False,
    #                             widget = forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        # print(all_clean_data)
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email don't match ")

    # This can be done with build-in VALIDATION
    # def clean_boatcatcher(self):
    #     boatcatcher = self.cleaned_data['boatcatcher']
    #     if len(boatcatcher)>0:
    #         raise forms.ValidationError("Gotcha BOT")
    #     return boatcatcher
