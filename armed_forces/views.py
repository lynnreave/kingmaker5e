from common import *
from .models import ArmedForce, Equipment, Casualty
from .forms import ArmedForceForm, EquipmentForm, CasualtyForm
from .vars import app_name


# ARMED FORCES
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


# EQUIPMENT
b_name = 'item'
b_plural = 'equipment'
b_obj = Equipment
b_form = EquipmentForm

def equipment(request):
    obj_plural_s = b_plural
    obj_plural = b_plural.replace(' ', '_')
    items = b_obj.objects.order_by('name')
    for item in items:
        get_equipment_details(item)
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {'title': obj_plural_s.title(), obj_plural: items}
    )
def item_new(request):
    return create_item(request, app_name, b_name, b_form, b_plural, fast_commit=True)
def item_edit(request, pk):
    return edit_item(request, app_name, pk, b_obj, b_name, b_form, b_plural, fast_commit=True)
def item_delete(request, pk): return delete_item(request, app_name, pk, b_obj, b_plural)


# CASUALTIES
c_name = 'casualty'
c_plural = 'casualties'
c_obj = Casualty
c_form = CasualtyForm

def casualties(request):
    return show_all_items(request, app_name, c_obj, c_plural, sort='months')
def casualty_new(request):
    return create_item(request, app_name, c_name, c_form, c_plural, fast_commit=True)
def casualty_edit(request, pk):
    return edit_item(request, app_name, pk, c_obj, c_name, c_form, c_plural, fast_commit=True)
def casualty_delete(request, pk): return delete_item(request, app_name, pk, c_obj, c_plural)
