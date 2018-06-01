from django.contrib import admin
from .models import TaxEdict
from .models import PromotionEdict
from .models import HolidayEdict
from .models import RecruitmentEdict
from .models import Month


class CustomModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


admin.site.register(TaxEdict, CustomModelAdmin)
admin.site.register(PromotionEdict, CustomModelAdmin)
admin.site.register(HolidayEdict, CustomModelAdmin)
admin.site.register(RecruitmentEdict, CustomModelAdmin)
admin.site.register(Month, CustomModelAdmin)
