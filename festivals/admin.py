from django.contrib import admin
from .models import Festival, Type, SuccessLevel


class CustomModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


admin.site.register(Festival, CustomModelAdmin)
admin.site.register(Type, CustomModelAdmin)
admin.site.register(SuccessLevel, CustomModelAdmin)
