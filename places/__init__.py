# -*- coding: utf-8 -*-
from __future__ import unicode_literals

default_app_config = 'places.apps.PlacesConfig'
__version__ = '5.2.1'


class Places(object):
    def __init__(self, country, city, state, latitude, longitude, name=None, formatted_address=None):

        if isinstance(latitude, float) or isinstance(latitude, int):
            latitude = str(latitude)
        if isinstance(longitude, float) or isinstance(longitude, int):
            longitude = str(longitude)

        self.country = country
        self.city = city
        self.name = name 
        self.state = state
        self.formatted_address = formatted_address
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        return {
            'country': self.country,
            'city': self.city,
            'state': self.state,
            'latitude': float(self.latitude), # Convert Decimal to float
            'longitude': float(self.longitude), # Convert Decimal to float
            'name': self.name,
            'formatted_address': self.formatted_address
        }

    @staticmethod
    def from_dict(data):
        return Places(
            country=data.get('country'),
            city=data.get('city'),
            state=data.get('state'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            name=data.get('name'),
            formatted_address=data.get('formatted_address')
        )

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.country, self.city, self.state, self.latitude, self.longitude, self.name, self.formatted_address)

    def __repr__(self):
        return "Places(%s)" % str(self)

    def __len__(self):
        return len(str(self))

    def __eq__(self, other):
        return (
            isinstance(other, Places)
            and self.latitude == other.latitude
            and self.longitude == other.longitude
        )

    def __ne__(self, other):
        return (
            not isinstance(other, Places)
            or self.latitude != other.latitude
            or self.longitude != other.longitude
        )
