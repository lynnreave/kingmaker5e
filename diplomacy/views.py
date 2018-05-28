from common import *
from .models import DiplomaticRelation
from .forms import DiplomaticRelationForm
from .vars import app_name

# Event
a_name = 'diplomatic relation'
a_plural = 'diplomatic relations'
a_obj = DiplomaticRelation
a_form = DiplomaticRelationForm

def diplomatic_relations(request):
    obj_plural_s = a_plural
    obj_plural = a_plural.replace(' ', '_')
    items = a_obj.objects.order_by('holder__name', 'target')
    get_diplomacy_dcs(items)
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {'title': obj_plural_s.title(), obj_plural: items}
    )
def diplomatic_relation_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def diplomatic_relation_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def diplomatic_relation_delete(request, pk):
    return delete_item(request, app_name, pk, a_obj, a_plural)
