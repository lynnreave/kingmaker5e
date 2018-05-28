from common import *
from .models import Event
from .forms import EventForm
from .vars import app_name

# Event
a_name = 'event'
a_plural = 'events'
a_obj = Event
a_form = EventForm

def events(request):
    return show_all_items(request, app_name, a_obj, a_plural, sort='polity__name', sort_2='name')
def event_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def event_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def event_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)
