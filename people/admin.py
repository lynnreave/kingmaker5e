from django.contrib import admin
from .models import Person
from .models import Award
from .models import Gender
from .models import NobleRank
from .models import LeadershipRole


class CustomModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)

# Register your models here.


admin.site.register(Person, CustomModelAdmin)
admin.site.register(Award, CustomModelAdmin)
admin.site.register(Gender, CustomModelAdmin)
admin.site.register(NobleRank, CustomModelAdmin)
admin.site.register(LeadershipRole, CustomModelAdmin)
