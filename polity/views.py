from common import *
from .models import Polity
from .forms import PolityForm
from .vars import app_name


# TERRITORIES
a_name = 'polity'
a_plural = 'polities'
a_obj = Polity
a_form = PolityForm

def polities(request):
    return show_all_items(
        request, app_name, a_obj, a_plural, sort='name'
    )
def polity_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def polity_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def polity_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)
def polity_details(request, pk):
    polity = get_polity_details(pk)['polity']
    return render(
        request, 'polity/polity_details.html', {
            'title': polity.name.upper(),
            'polity': polity,
        }
    )