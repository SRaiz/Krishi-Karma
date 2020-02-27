from django.contrib import admin

from .models import Crop


class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url')


admin.site.register(Crop, CropAdmin)
