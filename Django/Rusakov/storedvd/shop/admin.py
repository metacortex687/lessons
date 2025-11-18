from django.contrib import admin
from shop.models import Section,Product,Discount,Order,OrderLine

admin.site.register(Section)
admin.site.register(Order)
admin.site.register(OrderLine)

class ProdactAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'imagr', 'price', 'date')
    actions_on_bottom = True
    list_per_page = 10
    search_fields = ('title','cast')

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code','value')

admin.site.register(Product,ProdactAdmin)
admin.site.register(Discount,DiscountAdmin)


