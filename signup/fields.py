from django.forms import ModelChoiceField


class CityModelChoiceField(ModelChoiceField):

    def __init__(
        self, queryset, empty_label="Where do you live?",
        required=True, widget=None, label=None, initial=None,
        help_text='', to_field_name=None, limit_choices_to=None,
        *args, **kwargs):

        ModelChoiceField.__init__(
            self, queryset, empty_label,
            required, widget, label, initial,
            help_text, to_field_name, limit_choices_to,
           *args, **kwargs)

    def label_from_instance(self, city):
        return city.name + ', ' + city.state
