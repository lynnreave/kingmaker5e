from django.contrib import admin
from .models import BuildingType, Type, BuildingEnhancement, Deity, Stronghold, StrongholdType
from .models import Expansion, ExpansionType, ExpansionFeature


class CustomModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


admin.site.register(BuildingType, CustomModelAdmin)
admin.site.register(Type, CustomModelAdmin)
admin.site.register(BuildingEnhancement, CustomModelAdmin)
admin.site.register(Deity, CustomModelAdmin)
admin.site.register(Stronghold, CustomModelAdmin)
admin.site.register(StrongholdType, CustomModelAdmin)
admin.site.register(Expansion, CustomModelAdmin)
admin.site.register(ExpansionType, CustomModelAdmin)
admin.site.register(ExpansionFeature, CustomModelAdmin)
