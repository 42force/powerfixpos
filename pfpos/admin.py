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

    title = 'Available Stocks'
    parameter_name = 'stock_available'

    def lookups(self, request, model_admin):

        return(
            ('low', 'Low Stock'),
            ('high', 'High Stock' )
        )

    def queryset(self, request, queryset):


        if self.value() == 'low':
            return queryset.filter(stock__lte=F('minimum_stock'))
        if self.value() == 'high':
            return queryset.filter(stock__gte=F('minimum_stock'))


class ProductAdmin(admin.ModelAdmin):
    actions = ['delete_selected']


    list_display = (
        'name',
        'description',
        'code',
        'price',
        'stock',
        'minimum_stock',
        'stock_applies'
    )

    list_display_links = (
        'code',
        'name',
    )

    search_fields = (
        'code',
        'name'

    )

    list_filter = (
        LowStockFilter,
    )

def safe_delete_order(modeladmin, request, queryset):
        queryset.filter(done=True).delete()
        safe_delete_order.short_description = "Safely Delete Completed Orders"


class OrderAdmin(admin.ModelAdmin):

    actions = [safe_delete_order]

    list_display = (
        'user',
        'total_price',
        'done',
        'last_change'
    )

    #sidebar Filter
    list_filter = (
        'done'
    )

    ordering = ('done',)

admin.site.register(Cash)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Setting)
