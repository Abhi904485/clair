from django.forms import CharField, TextInput, IntegerField, forms, DateTimeField

from .models import Layer


class LayerSearchForm(forms.Form):
    id = IntegerField(label="Search By ID", required=False, widget=TextInput(
        attrs={
            'filter_field': 'id',
            'filter_method': '__exact',
            'placeholder': "1",
        }
    ))
    name = CharField(label="Search By Layer Name", required=False, widget=TextInput(
        attrs={
            'filter_field': 'name',
            'filter_method': '__exact',
            'placeholder': "84c5f6e03bf04e139705ceb2612ae274aad94f8dcf8cc630fbf6d91975f2e1c9d121f8d1c4128ebc1e95e5bfad90a0189b84eadbbb2fbaad20cbb26d20b2c8a2",
            'size': '150',
        }
    ))

    engine_version = CharField(label="Search By Engine Version", required=False, widget=TextInput(
        attrs={
            'filter_field': 'engineversion',
            'filter_method': '__exact',
            'placeholder': "3",
        }
    ))

    parent = CharField(label="Search By Layer Parent Name", required=False, widget=TextInput(
        attrs={
            'filter_field': 'parent__name',
            'filter_method': '__exact',
            'placeholder': "84c5f6e03bf04e139705ceb2612ae274aad94f8dcf8cc630fbf6d91975f2e1c9d121f8d1c4128ebc1e95e5bfad90a0189b84eadbbb2fbaad20cbb26d20b2c8a2",
        }
    ))

    parent_is_null = CharField(label="Search Layer where parent is null", required=False, widget=TextInput(
        attrs={
            'filter_field': 'parent__name',
            'filter_method': '__isnull',
            'placeholder': "True or False (Case Does not Matter)",
        }
    ))

    namespace = CharField(label="Search By Namespace", required=False, widget=TextInput(
        attrs={
            'filter_field': 'namespace__name',
            'filter_method': '__exact',
            'placeholder': 'alpine:3.1.4',
        }
    ))

    # CHOICES = (
    #     ('__exact', "exact"),
    #     ('__iexact', "iexact"),
    #     ('__gt', "gt"),
    #     ('__gte', "gte"),
    #     ('__lt', "lt"),
    #     ('__lte', "lte"),
    #     ('__contains', "contains"),
    #     ('__icontains', "icontains"),
    #     ('__startswith', "startswith"),
    #     ('__istartswith', "istartswith"),
    #     ('__endswith', "endswith"),
    #     ('__iendswith', "iendswith"),
    #     ('__range', "range")
    # )
    #
    # select_box = ChoiceField(choices=CHOICES, widget=Select())

    created_layer_between_date = DateTimeField(label="Search In Date Range", required=False, widget=TextInput(
        attrs={
            'filter_field': 'created_at',
            'filter_method': '__range',
            'placeholder': 'yyyy[y]-mm[mo]-dd[d] yyyy[y]-mm[mo]-dd[d]',
        }

    ))

    created_before_date = DateTimeField(label="Search By Layer Created before date", required=False,
                                                   widget=TextInput(
                                                       attrs={
                                                           'filter_field': 'created_at',
                                                      'filter_method': '__lt',
                                                      'placeholder': 'yyyy[y]-mm[mo]-dd[d]',
                                                       }
                                                   ))
    created_after_date = DateTimeField(label="Search By Layer Created after date", required=False,
                                               widget=TextInput(
                                                   attrs={
                                                       'filter_field': 'created_at',
                                                  'filter_method': '__gt',
                                                  'placeholder': 'yyyy[y]-mm[mo]-dd[d]',
                                                   }
                                               ))
    created_on_exact_date = DateTimeField(label="Search by Layer created on Exact Date", required=False, widget=TextInput(
        attrs={
            'filter_field': 'created_at',
            'filter_method': '__date',
            'placeholder': 'yyyy[y]-mm[mo]-dd[d] hh[h]:mm[m]:ss[s]',
        }
    ))
    created_on_year_month_day_hour_minute_second_and_or = DateTimeField(
        label="Search by Day Month Year hour minute second", required=False, widget=TextInput(
        attrs={
            'filter_field': 'created_at',
                'filter_method': '',
                'placeholder': 'yyyy[y]-mm[mo]-dd[d] hh[h]:mm[m]:ss[s]  or yyyy[y] ,mm[mo], dd[d],  hh[h], mm[m], ss[s]',
        }
    ))

    class Meta:
        model = Layer
        fields = '__all__'
        model._meta.fields[0].verbose_name = "Layer ID"
