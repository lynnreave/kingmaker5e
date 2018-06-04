from common import *
from .models import Territory, Type, Feature, Improvement, Map
from .forms import TerritoryForm, TypeForm, FeatureForm, ImprovementForm, MapForm
from .vars import app_name

# TERRITORIES
a_name = 'territory'
a_plural = 'territories'
a_obj = Territory
a_form = TerritoryForm

def territories(request):
    obj_plural = a_plural.replace(' ', '_')
    items = a_obj.objects.order_by('polity', 'hex', 'type')
    items = get_territory_effects(items)['territories']
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {'title': obj_plural.capitalize(), obj_plural: items}
    )
def territory_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def territory_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def territory_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)

# TERRAIN TYPES
b_name = 'type'
b_plural = 'types'
b_obj = Type
b_form = TypeForm

def types(request): return show_all_items(request, app_name, b_obj, b_plural, sort='name')
def type_new(request): return create_item(request, app_name, b_name, b_form, b_plural)
def type_edit(request, pk): return edit_item(
    request, app_name, pk, b_obj, b_name, b_form, b_plural)
def type_delete(request, pk): return delete_item(request, app_name, pk, b_obj, b_plural)

# TERRAIN FEATURES
c_name = 'feature'
c_plural = 'features'
c_obj = Feature
c_form = FeatureForm

def features(request): return show_all_items(request, app_name, c_obj, c_plural, sort='name')
def feature_new(request): return create_item(request, app_name, c_name, c_form, c_plural)
def feature_edit(request, pk): return edit_item(
    request, app_name, pk, c_obj, c_name, c_form, c_plural)
def feature_delete(request, pk): return delete_item(request, app_name, pk, c_obj, c_plural)

# TERRAIN IMPROVEMENTS
d_name = 'improvement'
d_plural = 'improvements'
d_obj = Improvement
d_form = ImprovementForm

def improvements(request): return show_all_items(request, app_name, d_obj, d_plural, sort='name')
def improvement_new(request): return create_item(request, app_name, d_name, d_form, d_plural)
def improvement_edit(request, pk): return edit_item(
    request, app_name, pk, d_obj, d_name, d_form, d_plural)
def improvement_delete(request, pk): return delete_item(request, app_name, pk, d_obj, d_plural)


# MAPS
e_name = 'map'
e_plural = 'maps'
e_obj = Map
e_form = MapForm

def maps(request): return show_all_items(request, app_name, e_obj, e_plural)
def map(request, pk):
    map = get_object_or_404(e_obj, pk=pk)
    hexes = map.territory.all().order_by('hex')
    for hex in hexes:
        get_hex_details(hex)
    return render(
        request, '%s/%s.html' % (app_name, e_name),
        {'title': map.name.title(), map: map, 'hexes': hexes}
    )
def map_new(request): return create_item(request, app_name, e_name, e_form, e_plural)
def map_edit(request, pk): return edit_item(
    request, app_name, pk, e_obj, e_name, e_form, e_plural)
def hex_edit(request, pk, map_id):
    tgt = '%s:map' % app_name
    hex = get_object_or_404(Territory, pk=pk)
    if request.method == "POST":
        form = TerritoryForm(request.POST, instance=hex)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            return redirect('%s:map' % app_name, pk=map_id)
    else:
        form = TerritoryForm(instance=hex)
    return render(
        request, '%s/edit.html' % app_name, {'title': 'Hex %s' % hex.hex, 'form': form}
    )
