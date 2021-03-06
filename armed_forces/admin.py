from django.contrib import admin
from .models import ArmedForce, SoldierType, UnitType, Equipment, Boon, SpecialAbility, Tactic
from .models import Casualty


class CustomModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


admin.site.register(ArmedForce, CustomModelAdmin)
admin.site.register(SoldierType, CustomModelAdmin)
admin.site.register(UnitType, CustomModelAdmin)
admin.site.register(Equipment, CustomModelAdmin)
admin.site.register(Boon, CustomModelAdmin)
admin.site.register(SpecialAbility, CustomModelAdmin)
admin.site.register(Tactic, CustomModelAdmin)
admin.site.register(Casualty, CustomModelAdmin)
