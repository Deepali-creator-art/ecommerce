from django.contrib import admin 
from .models import Category,Product
class admincategoryclass(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,admincategoryclass)

class adminproductclass(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(Product,adminproductclass)

