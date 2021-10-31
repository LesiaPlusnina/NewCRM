from django.contrib.gis.admin import OSMGeoAdmin
from .models import Geo_crm


@admin.register(Geo_crm)
class Geo_crmAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')