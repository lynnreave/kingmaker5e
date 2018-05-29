from common import *
from .models import ArmedForce
from .forms import ArmedForceForm
from .vars import app_name


# PEOPLE
a_name = 'armed force'
a_plural = 'armed forces'
a_obj = ArmedForce
a_form = ArmedForceForm

def armed_forces(request):
    obj_plural_s = a_plural
    obj_plural = a_plural.replace(' ', '_')
    items = a_obj.objects.order_by('polity__name', 'name')
    for armed_force in items:
        get_armed_force_details(armed_force)
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {'title': obj_plural_s.title(), obj_plural: items}
    )
def armed_force_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def armed_force_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def armed_force_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)
