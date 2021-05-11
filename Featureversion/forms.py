from django.forms import CharField, TextInput, IntegerField, forms

from .models import Featureversion


class FeatureVersionSearchForm(forms.Form):
    id = IntegerField(label="Search By Feature Version Id", required=False, widget=TextInput(
        attrs={
            'filter_field': 'id',
            'filter_method': '__exact',
            'placeholder': "1",
        }
    ))
    version = CharField(label="Search By Feature Version", required=False, widget=TextInput(
        attrs={
            'filter_field': 'version',
            'filter_method': '__exact',
            'placeholder': "0.23.15-2",
        }
    ))

    feature = CharField(label="Search By Feature Name", required=False, widget=TextInput(
        attrs={
            'filter_field': 'feature__name',
            'filter_method': '__exact',
            'placeholder': "p11-kit",
        }
    ))

    namespace = CharField(label="Search By Namespace Name", required=False, widget=TextInput(
        attrs={
            'filter_field': 'feature__namespace__name',
            'filter_method': '__exact',
            'placeholder': "0.23.15-2",
        }
    ))

    class Meta:
        model = Featureversion
        fields = '__all__'
        model._meta.fields[0].verbose_name = "Feature Version ID"
