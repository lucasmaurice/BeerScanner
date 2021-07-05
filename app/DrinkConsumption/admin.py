from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Container)
admin.site.register(Product)
admin.site.register(ProductContainer)
admin.site.register(PersonnalContainer)
admin.site.register(PersonnalTag)
admin.site.register(PersonnalConsumption)
