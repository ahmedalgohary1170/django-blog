from django.contrib import admin

from .models import Post


class ProductAdmin(admin.ModelAdmin):
    list_display=['title','draft']
    list_filter=['draft','tags']
    search_fields=['title','tags']



admin.site.register(Post,ProductAdmin)
