from django import forms
from django.core.exceptions import ValidationError

from signup.models import Subscriber
from signup.fields import CityModelChoiceField


class SubscriberForm(forms.models.ModelForm):

    class Meta:
        model = Subscriber
        fields = ('email', 'city')
        field_classes = {
            'city': CityModelChoiceField,
        }
        widgets = {
            'email': forms.fields.EmailInput(
                attrs={
                    'placeholder': 'Enter your email',
                    'class': 'form-control input-lg',
                }),
            'city': forms.fields.Select(
                attrs={
                    'class': 'form-control input-lg'
                })
        }
        error_message = {
            'email': {'required': 'Your email is required!'},
            'city': {'required': 'Your city is required!'}
        }

        def validate_unique(self):
            try:
                self.instance.validate_unique()
            except ValidationError as e:
                e.error_dict = {'name': ['That email is already registered!']}
                self._update_errors(e)
