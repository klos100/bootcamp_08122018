from django.contrib import admin

# Register your models here.


from cars.models import Car, Engine


class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "prod_year"]
    filter = ['brand']


admin.site.register(Car, CarAdmin)


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ["type", "power"]
