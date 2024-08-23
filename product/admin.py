from django.contrib import admin
from .models import Product , Category , File
# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title','is_enable','created_time']
    search_fields = ['title']
    list_filter = ['is_enable', 'parent']

class fileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file', 'is_enable']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable', 'created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    inlines = [fileInlineAdmin]
    filter_horizontal = ['categories']



