from django.forms import CharField, TextInput, IntegerField, forms

from .models import Feature


class FeatureSearchForm(forms.Form):
    id = IntegerField(label="Search By Feature ID", required=False, widget=TextInput(
        attrs={
            'filter_field': 'id',
            'filter_method': '__exact',
            'placeholder': "1"
        }
    ))
    name = CharField(label="Search By Feature Name", required=False, widget=TextInput(
        attrs={
            'filter_field': 'name',
            'filter_method': '__exact',
            'placeholder': "xen",
        }
    ))

    namespace = CharField(label="Search By Namespace", required=False, widget=TextInput(
        attrs={
            'filter_field': 'namespace__name',
            'filter_method': '__exact',
            'placeholder': "alpine:2.14",
        }
    ))

    version_format = CharField(label="Search By Version Format", required=False, widget=TextInput(
        attrs={
            'filter_field': 'namespace__version_format',
            'filter_method': '__exact',
            'placeholder': "dpkg",
        }
    ))
    # version = CharField(label="Search By Version", required=False, widget=TextInput(
    #     attrs={
    #         'filter_field': 'vulnerabilityfixedinfeature__version',
    #         'filter_method': '__exact',
    #         'placeholder': "9.5.5-1quantal1",
    #     }
    # ))
    # vulnerability = CharField(required=False, widget=TextInput(
    #     attrs={
    #         'filter_field': 'vulnerabilityfixedinfeature__vulnerability__name',
    #         'filter_method': '__exact',
    #         'placeholder': "CVE-2005-4890",
    #     }
    # ))

    class Meta:
        model = Feature
        fields = '__all__'
        model._meta.fields[0].verbose_name = "Feature ID"
