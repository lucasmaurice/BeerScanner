from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'style', 'abv')


class RefillAdmin(admin.ModelAdmin):
    model=Refill
    list_display = ['pk', 'get_client', 'product', 'container']
    list_filter = ['user', 'product', 'container']

    def get_client(self, obj):
        if obj.user.first_name != '':
            return obj.user.first_name
        else:
            return obj.user
    get_client.short_description = "Client"


class ProductContainerAdmin(admin.ModelAdmin):
    model = ProductContainer
    list_display = ['get_title', 'get_remaining']

    def get_title(self, obj):
        return obj.product.name + " - " + obj.container.__str__()
    get_title.short_description = 'Name'

    def get_remaining(self, obj):
        refills = Refill.objects.all().filter(product=obj)
        consumed = 0 
        for r in refills:
            consumed += r.container.capacity
        return str(obj.container.capacity - consumed) + " L"
    get_remaining.short_description = 'Remaining'

class TapAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_ontap']
    def get_ontap(self, obj):
        return obj.onTap


admin.site.register(Container)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductContainer, ProductContainerAdmin)
admin.site.register(PersonalContainer)
admin.site.register(Tag)
admin.site.register(Refill, RefillAdmin)
admin.site.register(Tap, TapAdmin)
admin.site.register(Reader)
