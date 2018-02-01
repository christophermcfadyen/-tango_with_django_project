from django.contrib import admin
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
# Register your models here.
admin.site.register(Page)
admin.site.register(Category, CategoryAdmin)