from django.contrib import admin

# Register your models here.
from .models import *


admin.site.site_header = "BurgerHouse"
admin.site.site_url = "BurgerHouse"
admin.site.site_title = "BurgerHouse"
admin.site.site_header = 'Admin'
admin.site.login_template = "login"

admin.site.register(Category)
admin.site.register(Additional)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Comment)


from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','preparation_time','category','get_image')
    list_editable = ('category')
    list_filter = ('category')
    list_display_links = ('name')
    search_fields = ('name','description','category__name')
    inlines = [
        ProductImageInline
    ]
    prepopulated_fields = {'slug':('name',)}

    def get_image(self,obj):
        images = ProductImage.objects.filter(product=obj)
        if images:
            product_image = images[0]
            return str(f'<img src="{product_image.image.url}" style="width:150px">')
        else:
            return "-"
