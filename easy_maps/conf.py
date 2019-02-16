# -*- coding: utf-8 -*-

from django.conf import settings  # pylint: disable=W0611
from appconf import AppConf


class EasyMapsSettings(AppConf):
    CENTER = (-41.3, 32)
    GEOCODE = 'easy_maps.geocode.google_v3'
    GOOGLE_MAPS_API_KEY = None

    class Meta:
        prefix = 'easy_maps'
        holder = 'easy_maps.conf.settings'
