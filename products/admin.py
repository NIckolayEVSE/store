from django.contrib import admin

# Register your models here.
from products.models import ProductCategory, Product, Basket


# admin.site.register(ProductCategory)
# admin.site.register(Product

@admin.register(ProductCategory)
class ProdictCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProdictAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'quantity', 'category')
    list_editable = ('name', 'price', 'quantity', 'category')
    fields = (('name', 'category'), 'description', ('price', 'quantity'), 'image',)
    search_fields = ('name',)
    ordering = ('-name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
