from django.contrib import admin
from .models import Category, Product, ProductImage, Brand, Size, Color, Tags, Blog, Contact, Users, Banner
# Register your models here.

admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Tags)
admin.site.register(Contact)

admin.site.register(Banner)
admin.site.register(Users)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'status')


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'rating')
    search_fields = ('name', 'rating')
    inlines = [ProductImageInline, ]
    
