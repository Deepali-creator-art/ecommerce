from django.contrib import admin 
from .models import Category,Product
class admincategoryclass(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(Category,admincategoryclass)

class adminproductclass(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','price','stock','available','created','updated']
    list_editable=['price','stock','available']
    list_per_page=20
admin.site.register(Product,adminproductclass)

