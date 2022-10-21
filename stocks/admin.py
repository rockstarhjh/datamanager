from django.contrib import admin

# Register your models here.


class StocksAdmin(admin.ModelAdmin):
    list_display = (
    "idstocks", "idproducts", "category", "p_name", "company", "in_field", "out_field", "return_field", 'lost_field', 'location', 'remark')
    search_fields = ['products__idproducts', 'category', 'p_name']