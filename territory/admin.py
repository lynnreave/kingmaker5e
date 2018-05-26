from django.contrib import admin
from .models import Territory
from .models import Type
from .models import Feature
from .models import Improvement


class CustomModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)

# Register your models here.


admin.site.register(Territory, CustomModelAdmin)
admin.site.register(Type, CustomModelAdmin)
admin.site.register(Feature, CustomModelAdmin)
admin.site.register(Improvement, CustomModelAdmin)
