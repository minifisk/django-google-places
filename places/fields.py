
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField

try:
    from django.utils.encoding import smart_text
except ImportError:
    from django.utils.encoding import smart_str as smart_text

from . import Places
from .forms import PlacesField as PlacesFormField


class PlacesField(JSONField):
    description = _('A geoposition field (latitude and longitude)')

    def __init__(self, *args, **kwargs):
        super(PlacesField, self).__init__(*args, **kwargs)

    def to_python(self, value):

        if isinstance(value, Places):
            value = value

        if isinstance(value, str):
            value = json.loads(value)

        if isinstance(value, list):
            if len(value) >= 8:
                value = Places(
                    country=value[5],
                    city=value[6],
                    state=value[7],
                    latitude=value[1],
                    longitude=value[2],
                    name=value[3],
                    formatted_address=value[4]
                )

        if isinstance(value, dict):
            value = Places(
                country=value.get('country', None),
                city=value.get('city', None),
                state=value.get('state', None),
                latitude=value.get('latitude', None),
                longitude=value.get('longitude', None),
                name=value.get('name', None),
                formatted_address=value.get('formatted_address', None),
            )

        return value

    def get_prep_value(self, value):
        if isinstance(value, Places):
            return value.to_dict()
        return value
    
    def clean(self, value, model_instance):
        return value

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.to_python(value)

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return smart_text(value)

    def formfield(self, **kwargs):
        defaults = {'form_class': PlacesFormField}
        defaults.update(kwargs)
        return super(PlacesField, self).formfield(**defaults)
