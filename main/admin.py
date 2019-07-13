from django.contrib import admin
from django.utils.html import format_html
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "in_stock", "price"]
    list_filter = ["active", "in_stock", "date_updated"]
    list_editable = ["in_stock"]
    search_fields = ["name"]
    prepopulated_fields = {"slug" : ("name", )}  # it is populated AUTOMATICALLY

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_filter = ["active"]
    search_fields = ["name"]
    prepopulated_fields = {"slug" : ("name",)}
    autocomplete_fields = ("product",)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["thumbnail_tag", "product_name"]
    readonly_fields = ["thumbnail"]
    search_fields = ["product_name"]

    def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html('<img src="%s"/>' % obj.thumbnail.url)
        return "-"
    thumbnail_tag.short_description = "Thumbnail"

    def product_name(self, obj):
        return obj.product.name

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductTag, ProductTagAdmin)
admin.site.register(models.ProductImage, ProductImageAdmin)
