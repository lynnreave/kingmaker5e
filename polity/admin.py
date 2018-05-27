from django.contrib import admin
from .models import Polity, AlignmentLC, AlignmentGE, Government


class CustomModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


admin.site.register(Polity, CustomModelAdmin)
admin.site.register(AlignmentLC, CustomModelAdmin)
admin.site.register(AlignmentGE, CustomModelAdmin)
admin.site.register(Government, CustomModelAdmin)
