from common import *
from .models import Faction
from .forms import FactionForm
from .vars import app_name

# Event
a_name = 'faction'
a_plural = 'factions'
a_obj = Faction
a_form = FactionForm

def factions(request):
    return show_all_items(
        request, app_name, a_obj, a_plural, sort='polity__name', sort_2='name',
        #get_details=get_faction_details,
    )
def faction_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def faction_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def faction_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)