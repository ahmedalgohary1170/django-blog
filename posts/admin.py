from django.contrib import admin

from .models import Post,Category,Comment


class ProductAdmin(admin.ModelAdmin):
    list_display=['title','category','draft']
    list_filter=['draft','category','tags']
    search_fields=['title','tags']



admin.site.register(Post,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)