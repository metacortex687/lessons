from django.contrib import admin
from shop.models import Section, Product, Discount, Order, OrderLine

admin.site.register(Section)

class SectionAdmin(admin.ModelAdmin):
      list_display = ("title", "slug")

class PriceFilter(admin.SimpleListFilter):
    title = "Цена"
    parameter_name = "price"
    round_value = 100

    def lookups(self, request, model_admin):
        """
         return (
            ('100', '0-100'),
            ('200', '100-200'),
            ('300', '200-300'),
            ('400', '300-400'),
            ('500', '400-500'),
            ('600', '500-600'),
            ('700', '600-700'),

        )
        """
        filters = []
        product = Product.objects.order_by("price").last()
        if product:
            max_price = round(product.price / self.round_value) * self.round_value + self.round_value
            price = self.round_value
            while price <= max_price:
                start = price
                end = f"{price-self.round_value} - {price}"
                filters.append((start, end))
                price += self.round_value
        return filters

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        value = int(self.value())
        return queryset.filter(price__gte=(value - 100), price__lte=value)


class ProdactAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "section", "imagr", "price", "date")
    list_filter = ("section", PriceFilter)
    actions_on_bottom = True
    list_per_page = 10
    search_fields = ("title", "cast")


class DiscountAdmin(admin.ModelAdmin):
    list_display = ("code", "value_percent")

    def save_model(self, request, obj, form, change):
        print("Request ", request)
        print("Obj ", obj)
        print("Form ", form)
        print("Change ", change)
        super().save_model(request, obj, form, change)
        # return super().save_model(request, obj, form, change)
        print("Request ", request)
        print("Obj ", obj)
        print("Form ", form)
        print("Change ", change)


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

    fieldsets = (
        ("Информация о заказе", {"fields": ("need_delivery", "discount")}),
        (
            "Информация о клиенте",
            {
                "fields": (
                    "name",
                    "phone",
                    "email",
                    "adress",
                ),
                "description": "Контактная информация",
            },
        ),
        ("Доставка и оплата", {"fields": ("date_send", "status")}),
    )

    list_filter = ("status", "date_order")

    date_hierarchy = "date_order"


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price", "count")
    list_filter = ("order", "product")


admin.site.register(Product, ProdactAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
