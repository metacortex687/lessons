from django.contrib import admin
from shop.models import Section, Product, Discount, Order, OrderLine

admin.site.register(Section)


class ProdactAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "imagr", "price", "date")
    actions_on_bottom = True
    list_per_page = 10
    search_fields = ("title", "cast")


class DiscountAdmin(admin.ModelAdmin):
    list_display = ("code", "value_percent")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "display_products",
        "display_amount",
        "name",
        "discount",
        "phone",
        "email",
        "adress",
        "notice",
        "date_order",
        "date_send",
        "status",
    )


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price", "count")


admin.site.register(Product, ProdactAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
