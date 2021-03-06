from common import *
from .models import Settlement, Building, Stronghold, Expansion, District, Lot
from .forms import SettlementForm, BuildingForm, StrongholdForm, ExpansionForm, DistrictForm, LotForm
from .vars import app_name


# SETTLEMENT
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


# STRONGHOLDS
c_name = 'stronghold'
c_plural = 'strongholds'
c_obj = Stronghold
c_form = StrongholdForm

def strongholds(request):
    return show_all_items(
        request, app_name, c_obj, c_plural, sort='polity__name',
        get_details=get_stronghold_details,
    )
def stronghold_new(request):
    return create_item(request, app_name, c_name, c_form, c_plural, fast_commit=True)
def stronghold_edit(request, pk):
    return edit_item(request, app_name, pk, c_obj, c_name, c_form, c_plural, fast_commit=True)
def stronghold_delete(request, pk): return delete_item(request, app_name, pk, c_obj, c_plural)


# EXPANSIONS
d_name = 'expansion'
d_plural = 'expansions'
d_obj = Expansion
d_form = ExpansionForm


def expansions(request, stronghold_id):
    obj_plural_s = d_plural
    obj_plural = d_plural.replace(' ', '_')
    stronghold = Stronghold.objects.get(pk=stronghold_id)
    get_stronghold_details(stronghold)
    expansions = d_obj.objects.filter(stronghold=stronghold).order_by('type__name')
    for expansion in expansions:
        get_expansion_details(expansion)
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {
            'title': '%s %s' % (stronghold.name.title(), obj_plural_s.title()),
            obj_plural: expansions, 'stronghold_id': stronghold_id
        }
    )
def expansion_new(request, stronghold_id):
    obj_name_s = d_name
    obj_name = d_name.replace(' ', '_')
    obj_plural = d_plural.replace(' ', '_')
    stronghold = Stronghold.objects.get(pk=stronghold_id)
    get_stronghold_details(stronghold)
    tgt = "%s:%s" % (app_name, obj_plural)
    if request.method == "POST":
        form = d_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.stronghold = stronghold
            instance.save()
            return redirect(tgt, stronghold_id=stronghold.pk)
    else:
        form = d_form()
    return render(
        request, '%s/edit.html' % app_name, {
            'title': obj_name_s.title(), 'form': form, 'stronghold_id': stronghold_id
        }
    )
def expansion_edit(request, pk, stronghold_id):
    obj_name_s = d_name
    obj_name = d_name.replace(' ', '_')
    obj_plural = d_plural.replace(' ', '_')
    item = get_object_or_404(d_obj, pk=pk)
    tgt = "%s:%s" % (app_name, obj_plural)
    get_expansion_details(item)
    if request.method == "POST":
        form = d_form(request.POST, instance=item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.stronghold = item.stronghold
            instance.save()
            form.save_m2m()
            return redirect(tgt, stronghold_id=stronghold_id)
    else:
        form = d_form(instance=item)
    return render(
        request, '%s/edit.html' % app_name, {'title': obj_name_s.title(), 'form': form}
    )
def expansion_delete(request, pk, stronghold_id):
    obj_plural = d_plural.replace(' ', '_')
    item = get_object_or_404(d_obj, pk=pk)
    tgt = "%s:%s" % (app_name, obj_plural)
    item.delete()
    return redirect(tgt, stronghold_id=stronghold_id)


# DISTRICTS
e_name = 'district'
e_plural = 'districts'
e_obj = District
e_form = DistrictForm


def districts(request, settlement_id):
    obj_plural_s = e_plural
    obj_plural = e_plural.replace(' ', '_')
    settlement = Settlement.objects.get(pk=settlement_id)
    districts = e_obj.objects.filter(settlement=settlement).order_by('name')
    #for district in districts:
    #    get_district_details(district)
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {
            'title': '%s: %s' % (settlement.name.title(), obj_plural_s.title()),
            obj_plural: districts, 'settlement_id': settlement_id
        }
    )
def district_new(request, settlement_id):
    obj_name_s = e_name
    obj_name = e_name.replace(' ', '_')
    obj_plural = e_plural.replace(' ', '_')
    settlement = Settlement.objects.get(pk=settlement_id)
    tgt = "%s:%s" % (app_name, obj_plural)
    if request.method == "POST":
        form = d_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.settlement = settlement
            instance.save()
            return redirect(tgt, settlement_id=settlement.pk)
    else:
        form = d_form()
    return render(
        request, '%s/edit.html' % app_name, {
            'title': obj_name_s.title(), 'form': form, 'settlement_id': settlement_id
        }
    )
def district_edit(request, pk, settlement_id):
    obj_name_s = e_name
    obj_name = e_name.replace(' ', '_')
    obj_plural = e_plural.replace(' ', '_')
    item = get_object_or_404(e_obj, pk=pk)
    tgt = "%s:%s" % (app_name, obj_plural)
    if request.method == "POST":
        form = e_form(request.POST, instance=item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.settlement = item.settlement
            instance.save()
            form.save_m2m()
            return redirect(tgt, settlement_id=settlement_id)
    else:
        form = e_form(instance=item)
    return render(
        request, '%s/edit.html' % app_name, {'title': obj_name_s.title(), 'form': form}
    )
def district_delete(request, pk, settlement_id):
    obj_plural = e_plural.replace(' ', '_')
    item = get_object_or_404(e_obj, pk=pk)
    tgt = "%s:%s" % (app_name, obj_plural)
    item.delete()
    return redirect(tgt, settlement_id=settlement_id)


# LOTS
f_name = 'lot'
f_plural = 'lots'
f_obj = Lot
f_form = LotForm


def lots(request, settlement_id, district_id):
    obj_plural_s = f_plural
    obj_plural = f_plural.replace(' ', '_')
    settlement = Settlement.objects.get(pk=settlement_id)
    district = District.objects.get(pk=district_id)
    lots = f_obj.objects.filter(district=district).order_by('grid')
    for lot in lots:
        get_lot_details(lot)
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {
            'title': '%s: %s District' % (settlement.name.title(), district.name.title()),
            obj_plural: lots, 'settlement_id': settlement_id, 'district_id': district_id
        }
    )
def lot_new(request, settlement_id, district_id):
    obj_name_s = f_name
    obj_name = f_name.replace(' ', '_')
    obj_plural = f_plural.replace(' ', '_')
    settlement = Settlement.objects.get(pk=settlement_id)
    district = District.objects.get(pk=district_id)
    tgt = "%s:%s" % (app_name, obj_plural)
    if request.method == "POST":
        form = d_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.district = district
            instance.save()
            return redirect(tgt, settlement_id=settlement.pk, district_id=district.pk)
    else:
        form = d_form()
    return render(
        request, '%s/edit.html' % app_name, {
            'title': obj_name_s.title(), 'form': form, 'settlement_id': settlement_id,
            'district_id': district_id
        }
    )
def lot_edit(request, pk, settlement_id, district_id):
    obj_name_s = f_name
    obj_name = f_name.replace(' ', '_')
    obj_plural = f_plural.replace(' ', '_')
    settlement = Settlement.objects.get(pk=settlement_id)
    item = get_object_or_404(f_obj, pk=pk)
    tgt = "%s:%s" % (app_name, obj_plural)
    if request.method == "POST":
        form = f_form(request.POST, instance=item)
        form.fields["building"].queryset = Building.objects.filter(settlement=settlement)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.district = item.district
            instance.save()
            form.save_m2m()
            return redirect(tgt, settlement_id=settlement_id, district_id=district_id)
    else:
        form = f_form(instance=item)
        form.fields["building"].queryset = Building.objects.filter(settlement=settlement)
    return render(
        request, '%s/edit.html' % app_name, {'title': obj_name_s.title(), 'form': form}
    )
def lot_delete(request, pk, settlement_id, district_id):
    obj_plural = f_plural.replace(' ', '_')
    item = get_object_or_404(f_obj, pk=pk)
    tgt = "%s:%s" % (app_name, obj_plural)
    item.delete()
    return redirect(tgt, settlement_id=settlement_id, district_id=district_id)
