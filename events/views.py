from common import *
from .models import Event
from .forms import EventForm
from .vars import app_name
from polity.models import Polity

# Event
a_name = 'event'
a_plural = 'events'
a_obj = Event
a_form = EventForm

def events(request):
    return show_all_items(
        request, app_name, a_obj, a_plural, sort='polity__name', sort_2='name',
        get_details=get_event_details,
    )
def event_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def event_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def event_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)


def event_resolve(request, pk):
    obj_plural = a_plural.replace(' ', '_')
    tgt = '%s:%s' % (app_name, obj_plural)
    event = get_object_or_404(a_obj, pk=pk)
    polity = get_object_or_404(Polity, pk=event.polity.id)

    if event.fame_increment != 0:
        polity.fame += event.fame_increment
    if event.infamy_increment != 0:
        polity.infamy += event.infamy_increment
    if event.unrest_increment != 0:
        polity.unrest += event.unrest_increment
    if event.treasury_increment != 0:
        polity.treasury += event.treasury_increment
    polity.save()

    event.delete()
    return redirect(tgt)
