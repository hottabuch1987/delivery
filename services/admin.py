from django.contrib import admin
from . import models

admin.site.register(models.EquipmentType)
admin.site.register(models.Equipment)
admin.site.register(models.Promotion)
admin.site.register(models.UrgentConnection)
admin.site.register(models.Locality)
admin.site.register(models.ConnectionTypePlace)
admin.site.register(models.RequiredPayment)
