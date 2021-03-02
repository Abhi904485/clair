from django.forms import CharField, TextInput, IntegerField, forms

from .models import Namespace


class NamespaceForm(forms.Form):
    id = IntegerField(label="Search By Namespace ID", required=False, widget=TextInput(
        attrs={
            'filter_field': 'id',
            'filter_method': '__exact',
            'placeholder': "1",
        }
    ))

    namespace_name = CharField(label="Search By Namespace name", required=False, widget=TextInput(
        attrs={
            'filter_field': 'name',
            'filter_method': '__exact',
            'placeholder': "alpine:2.1.4",
        }
    ))

    version_format = CharField(label="Search By Namespace Version Format", required=False, widget=TextInput(
        attrs={
            'filter_field': 'version_format',
            'filter_method': '__exact',
            'placeholder': "5.0-4",
        }
    ))

    class Meta:
        model = Namespace
        fields = '__all__'
        model._meta.fields[0].verbose_name = "Namespace ID"
