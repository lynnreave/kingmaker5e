from common import *
from .models import Settlement, Building
from .forms import SettlementForm, BuildingForm
from .vars import app_name


# PEOPLE
a_name = 'settlement'
a_plural = 'settlements'
a_obj = Settlement
a_form = SettlementForm

def settlements(request):
    obj_plural_s = a_plural
    obj_plural = a_plural.replace(' ', '_')
    items = a_obj.objects.order_by('territory__polity__name', 'name')
    for settlement in items:
        get_settlement_details(settlement)
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {'title': obj_plural_s.title(), obj_plural: items}
    )
def settlement_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def settlement_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def settlement_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)


# BUILDINGS
b_name = 'building'
b_plural = 'buildings'
b_obj = Building
b_form = BuildingForm


def buildings(request, settlement_id):
    obj_plural_s = b_plural
    obj_plural = b_plural.replace(' ', '_')
    settlement = Settlement.objects.get(pk=settlement_id)
    get_settlement_details(settlement)
    buildings = b_obj.objects.filter(settlement=settlement).order_by('name')
    for building in buildings:
        get_building_details(building)
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {
            'title': '%s %s' % (settlement.name.title(), obj_plural_s.title()),
            obj_plural: buildings, 'settlement_id': settlement_id
        }
    )


def building_new(request, settlement_id):
    obj_name_s = b_name
    obj_name = b_name.replace(' ', '_')
    obj_plural = b_plural.replace(' ', '_')
    settlement = Settlement.objects.get(pk=settlement_id)
    tgt = "%s:%s" % (app_name, obj_plural)
    if request.method == "POST":
        form = b_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.settlement = settlement
            instance.save()
            return redirect(tgt, settlement_id=settlement.pk)
    else:
        form = b_form()
    return render(
        request, '%s/edit.html' % app_name, {
            'title': obj_name_s.title(), 'form': form, 'settlement_id': settlement_id
        }
    )


def building_edit(request, pk, settlement_id):
    obj_name_s = b_name
    obj_name = b_name.replace(' ', '_')
    obj_plural = b_plural.replace(' ', '_')
    item = get_object_or_404(b_obj, pk=pk)
    tgt = "%s:%s" % (app_name, obj_plural)
    if request.method == "POST":
        form = b_form(request.POST, instance=item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.settlement = item.settlement
            instance.save()
            form.save_m2m()
            return redirect(tgt, settlement_id=settlement_id)
    else:
        form = b_form(instance=item)
    return render(
        request, '%s/edit.html' % app_name, {'title': obj_name_s.title(), 'form': form}
    )


def building_delete(request, pk, settlement_id):
    obj_plural = b_plural.replace(' ', '_')
    item = get_object_or_404(b_obj, pk=pk)
    tgt = "%s:%s" % (app_name, obj_plural)
    item.delete()
    return redirect(tgt, settlement_id=settlement_id)
