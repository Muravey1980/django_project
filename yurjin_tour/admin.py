from django.contrib import admin

# Register your models here.
from .models import Country, City, Airport, Office, Manager, Tourist, Status, Contract

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Office)
admin.site.register(Manager)
admin.site.register(Tourist)
admin.site.register(Status)
admin.site.register(Contract)