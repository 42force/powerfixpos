from django.contrib import admin

from . models import Product, Cash, Order, Setting

from django.contrib.admin import SimpleListFilter

admin.site.site_header = "Powerfix Administration"
admin.site.site_title = "Powerfix Administration"


class SettingAdmin(admin.ModelAdmin):

    list_display=(
        'key',
        'value'
    )


#custom Filter for ProductAdmin
class LowStockFilter(SimpleListFilter):

    


admin.site.register(Cash)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Setting)
