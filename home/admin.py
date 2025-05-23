from django.contrib import admin
from home.models import Pizza

# admin.site.register(Pizza)

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display=["name", "size", "price", "date_created"]
    list_filter=["size"]
    ordering=["-date_created"]