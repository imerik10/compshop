from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(Category)


@admin.register(PC)
class PCclass(admin.ModelAdmin):
    list_display = ['name','price','category','show_image']
    list_display_links = ['name','category']
    list_filter = ['category']
    list_editable = ['price']

    def show_image(self,photo):
        if photo.image1:
            return mark_safe(f"<img src='{photo.image1.url}' width=70 >")
        return None
    show_image.__name__='Suwret'