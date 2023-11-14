from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post,Category,Comment


class ProductAdmin(SummernoteModelAdmin):
    list_display=['title','category','draft']
    list_filter=['draft','category','tags']
    search_fields=['title','tags']
    summernote_fields = ['content']



admin.site.register(Post,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)