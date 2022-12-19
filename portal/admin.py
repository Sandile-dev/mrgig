from django.contrib import admin
from . import models

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['sender_name','sender_surname','sender_phone','receiver_name','receiver_surname','receiver_phone','notification','date_created']

admin.site.register(models.Customer,CustomerAdmin)


class ParcelAdmin(admin.ModelAdmin):
    list_display = ['refNumber','customer','origination','destination','status','date_created']

admin.site.register(models.Parcel, ParcelAdmin)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['parcel','name','phoneNumber','driver_route','taxiRegNumber','date_created']

admin.site.register(models.Partner, PartnerAdmin)


class DriverRouteAdmin(admin.ModelAdmin):
    list_display = ['province','city','town','rankName','date_created']

admin.site.register(models.DriverRoute, DriverRouteAdmin)

