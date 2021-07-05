from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'style', 'abv')


class RefillAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'container']
    list_filter = ['user', 'product', 'container']


admin.site.register(Container)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductContainer)
admin.site.register(PersonnalContainer)
admin.site.register(PersonnalTag)
admin.site.register(Refill, RefillAdmin)
