from common import *
from .models import Army
from .forms import ArmyForm
from .vars import app_name


# PEOPLE
a_name = 'army'
a_plural = 'armies'
a_obj = Army
a_form = ArmyForm

def armies(request):
    return show_all_items(
        request, app_name, a_obj, a_plural, sort='polity__name', sort_2='name'
    )
def army_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def army_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def army_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)
