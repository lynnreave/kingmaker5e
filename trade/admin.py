from django.contrib import admin
from .models import TradeRoute, RouteType, SuccessLevel


class CustomModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


admin.site.register(TradeRoute, CustomModelAdmin)
admin.site.register(RouteType, CustomModelAdmin)
admin.site.register(SuccessLevel, CustomModelAdmin)
