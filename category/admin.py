from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug_name': ('category_name',)}
    list_display = ('category_name', 'slug_name')

admin.site.register(Category,CategoryAdmin)

