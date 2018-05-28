from common import *
from .models import Settlement
from .forms import SettlementForm
from .vars import app_name


# PEOPLE
a_name = 'settlement'
a_plural = 'settlements'
a_obj = Settlement
a_form = SettlementForm

def settlements(request):
    return show_all_items(
        request, app_name, a_obj, a_plural, sort='territory__polity__name', sort_2='name'
    )
def settlement_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def settlement_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def settlement_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)
