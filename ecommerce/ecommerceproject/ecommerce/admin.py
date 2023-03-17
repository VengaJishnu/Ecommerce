from django.contrib import admin
from .models import categoty, product


# Register your models here.

class categoryadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  # it will show only these 2 data in admin
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(categoty,categoryadmin) # model+class need to add

class productadmin(admin.ModelAdmin):
    list_display = ['name', 'slug','stock','available','created','updated','price']  # it will show only these 2 data in admin
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price','stock','available'] # which is defineing we can edit in main window
    list_per_page = 20

admin.site.register(product,productadmin)
