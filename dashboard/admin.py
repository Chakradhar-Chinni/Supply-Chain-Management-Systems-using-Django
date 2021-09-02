from django.contrib import admin
from .models import SupplierRegistration,UserRegistration,AdminRegistration,UserOrder,tud,tmd

# Register your models here.
admin.site.register(SupplierRegistration)
admin.site.register(AdminRegistration)
admin.site.register(UserRegistration)
admin.site.register(UserOrder)
admin.site.register(tud)
admin.site.register(tmd)