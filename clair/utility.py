from abc import ABC
from datetime import datetime

import pytz
from django.contrib import messages
from django.contrib.admin import FieldListFilter
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.html import format_html


def get_value(obj, attr, default="-"):
    return getattr(obj, attr, default)


def get_meta(obj):
    return get_value(obj, '_meta')


def get_app_name(obj, prev_table):
    return get_value(get_meta(obj), 'app_label', get_value(get_meta(prev_table), 'app_label'))


def get_db_table(obj, prev_table):
    return get_app_name(obj, prev_table).lower()


def get_table_primary_key(obj, prev_table):
    return get_value(obj, 'id')


def get_table_column_value(obj, prev_table, column):
    return get_value(obj, column)


def get_final_table(model, tables):
    prev_table = model
    for table in tables:
        model = get_value(model, table)
        if model is None:
            return table, prev_table
        else:
            continue
    return model, prev_table


def build_navigable_link(app_name, db_table, db_table_primary_key, db_table_column_value):
    return format_html(
        '<a href="/admin/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_column_value}</a>'.format(
            app_name=app_name, db_table=db_table,
            db_table_primary_key=db_table_primary_key, db_table_column_value=db_table_column_value))


def build_non_navigable_link(db_table_column_value):
    return format_html(
        '<p>{db_table_column_value}</p>'.format(db_table_column_value=db_table_column_value))


def get_link(model, column, tables):
    table, previous_table = get_final_table(model, tables)
    app_name = get_app_name(table, previous_table)
    db_table = get_db_table(table, previous_table)
    db_table_primary_key = get_table_primary_key(table, previous_table)
    db_table_column_value = get_table_column_value(table, previous_table, column)
    if db_table_column_value != "-":
        return build_navigable_link(app_name=app_name, db_table=db_table, db_table_primary_key=db_table_primary_key,
                                    db_table_column_value=db_table_column_value)
    else:
        return build_non_navigable_link(db_table_column_value=db_table_column_value)


def get_string_to_datetime(string):
    return datetime.strptime(string, "%Y-%m-%d").replace(tzinfo=pytz.UTC)


def sanitize_date(value):
    year, month, day = value.split("-")
    year = year.rstrip(year[-1])
    month = month.rstrip(month[-2:])
    day = day.rstrip(day[-1])
    return "-".join([year, month, day])


def get_date_time(sd=None, ed=None):
    first_date = None
    second_date = None
    if sd:
        sd = sanitize_date(sd)
        first_date = get_string_to_datetime(sd)
    if ed:
        ed = sanitize_date(ed)
        second_date = get_string_to_datetime(ed)
    return first_date, second_date


def split_field_value(field_value):
    if field_value:
        return field_value.split(" "), len(field_value.split(" "))
    return None


def get_field_name_and_field_filter(form_field, field):
    return form_field.widget.attrs.get('filter_field', field) + form_field.widget.attrs.get('filter_method', '')


def get_field_value(field, advanced_search_fields):
    if field in advanced_search_fields:
        return True, advanced_search_fields[field][0]
    return False, None


def before_exact_after(field, field_value, form_field, request, advanced_search_fields):
    if get_field_value(field, advanced_search_fields)[0]:
        try:
            (sd, length) = split_field_value(field_value)
            start_date, _ = get_date_time(sd[0])
            return Q(**{get_field_name_and_field_filter(form_field, field): start_date})
        except ValidationError:
            messages.add_message(request, messages.ERROR, 'Date time should be in yyyy[y]-mm[mo]-dd[d]')
            return None
    else:
        return Q()


def between_date_range(field, field_value, form_field, request, advanced_search_fields):
    if field_value:
        try:
            ((sd, ed), length) = split_field_value(field_value)
            start_date, end_date = get_date_time(sd, ed)
            return Q(**{get_field_name_and_field_filter(form_field, field): [start_date, end_date]})
        except ValidationError:
            messages.add_message(request, messages.ERROR, 'Both Date should be in yyyy[y]-mm[mo]-dd[d] with space separated ')
            return None
    else:
        return Q()


def generate_query_for_date(field, field_value, form_field, request, advanced_search_fields):
    if field_value:
        if split_field_value(field_value)[1] == 1:
            return before_exact_after(field, field_value, form_field, request, advanced_search_fields)
        elif split_field_value(field_value)[1] == 2:
            return between_date_range(field, field_value, form_field, request, advanced_search_fields)
        else:
            messages.add_message(request, messages.ERROR,'Entered Date should be in yyyy[y]-mm[mo]-dd[d]')
            return None
    else:
        return Q()


def check_year_month_day_hour_minute_second(value):
    entity = ""
    if value.lower().endswith("y"):
        entity = value[-1]
        return value.rstrip(value[-1]), entity
    elif value.lower().endswith("mo"):
        entity = value[-2:]
        return value.rstrip(value[-2:]), entity
    elif value.lower().endswith("d"):
        entity = value[-1]
        return value.rstrip(value[-1]), entity
    elif value.lower().endswith("h"):
        entity = value[-1]
        return value.rstrip(value[-1]), entity
    elif value.lower().endswith("m"):
        entity = value[-1]
        return value.rstrip(value[-1]), entity
    elif value.lower().endswith("s"):
        entity = value[-1]
        return value.rstrip(value[-1]), entity
    return value, entity


def get_year_month_day_hour_minute_second(value):
    if value.lower() == "h":
        return "__hour"
    elif value.lower() == "m":
        return "__minute"
    elif value.lower() == "s":
        return "__second"
    elif value.lower() == "y":
        return "__year"
    elif value.lower() == "mo":
        return "__month"
    elif value.lower() == "d":
        return "__day"


def generate_dynamic_dict(values, final_dict, filter_field):
    for value in values:
        v, e = check_year_month_day_hour_minute_second(value)
        final_dict[filter_field + get_year_month_day_hour_minute_second(e)] = v
    return final_dict


def generate_query_year_month_day_hour_minute_second_and_or(field_value, form_field, field):
    filter_field = form_field.widget.attrs.get('filter_field', field)
    final_dict = {}
    if len(field_value.split(" ")) == 2:
        d, t = field_value.split(" ")
        d_values = d.split("-")
        generate_dynamic_dict(d_values, final_dict, filter_field)
        t_values = t.split(":")
        return generate_dynamic_dict(t_values, final_dict, filter_field)

    elif len(field_value.split(" ")) == 1:
        d_or_t = field_value.split(" ")
        lower_value1 = d_or_t[0].lower()
        if 'y' in lower_value1 or 'mo' in lower_value1 or 'd' in lower_value1:
            d_values = lower_value1.split("-")
            return generate_dynamic_dict(d_values, final_dict, filter_field)
        elif 'h' in lower_value1 or 'm' in lower_value1 or 's' in lower_value1:
            t_values = lower_value1.split(":")
            return generate_dynamic_dict(t_values, final_dict, filter_field)


def is_null(field, field_value, form_field, request, advanced_search_fields):
    if field_value:
        field_name = form_field.widget.attrs.get('filter_field', field)
        field_filter = field_name + form_field.widget.attrs.get('filter_method', '')
        if field_value.lower() == "true":
            field_value = True
            return Q(**{field_filter: bool(field_value)})
        elif field_value.lower() == "false":
            field_value = False
            return Q(**{field_filter: bool(field_value)})
        else:
            messages.add_message(request, messages.ERROR, "Input Should be True or false (Not Case Sensitive)")
            return None
    else:
        return Q()


def day_month_year_and_or(field, field_value, form_field, request, advanced_search_fields):
    if field_value:
        return Q(**generate_query_year_month_day_hour_minute_second_and_or(field_value, form_field, field))
    else:
        return Q()


def custom_titled_filter(title):
    class Wrapper(FieldListFilter, ABC):
        def __new__(cls, *args, **kwargs):
            instance = FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper
