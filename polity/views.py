from common import *
from .models import Polity, LogEntry
from .forms import PolityForm, LogEntryForm
from .vars import app_name


# POLITIES
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


def polity_modify_treasury(request, pk, dir, step):
    polity = get_object_or_404(Polity, pk=pk)
    if dir == '+':
        polity.treasury += step
    else:
        polity.treasury -= step
    polity.save()
    return redirect('polity:polity_details', pk=pk)


def polity_modify_unrest(request, pk, dir, step):
    polity = get_object_or_404(Polity, pk=pk)
    if dir == '+':
        polity.unrest += step
    else:
        polity.unrest -= step
    polity.save()
    return redirect('polity:polity_details', pk=pk)


# LOG ENTRIES
b_name = 'log entry'
b_plural = 'log entries'
b_obj = LogEntry
b_form = LogEntryForm

def log_entries(request):
    return show_all_items(
        request, app_name, b_obj, b_plural, sort='polity__name', sort_2='year', sort_3='month__pk'
    )
def log_entry_new(request):
    return create_item(request, app_name, b_name, b_form, b_plural, fast_commit=True)
def log_entry_edit(request, pk):
    return edit_item(request, app_name, pk, b_obj, b_name, b_form, b_plural, fast_commit=True)
