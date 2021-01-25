from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'quantity', 'category','vendor','discount','sales','post_date'
    ]


admin.site.register(Order_item)
admin.site.register(Place_order)
admin.site.register(Vendor)
admin.site.register(Contat_us)
admin.site.register(Subscriber)
