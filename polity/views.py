from common import *
from .models import Polity, LogEntry
from .forms import PolityForm, LogEntryForm
from .vars import app_name
from core.models import Month


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
b_plural = 'logs'
b_obj = LogEntry
b_form = LogEntryForm

def logs(request, polity_id, current_year):
    obj_plural_s = b_plural
    obj_plural = b_plural.replace(' ', '_')
    polity = Polity.objects.get(pk=polity_id)
    logs = b_obj.objects.filter(polity=polity).order_by('year', 'month__pk')
    years = []
    for log in logs:
        if log.year not in years:
            years.append(log.year)
    years.sort(reverse=True)
    if current_year is 0 and len(years) > 0:
        current_year = years[0]
    if current_year is not 0:
        logs = b_obj.objects.filter(polity=polity, year=current_year).order_by('month__pk')
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {
            'title': '%s Logs (%s)' % (polity.name.title(), current_year),
            obj_plural: logs, 'polity_id': polity_id, 'years': years, 'current_year': current_year,
        }
    )


def logs_add_year(request, polity_id):
    polity = Polity.objects.get(pk=polity_id)
    logs = b_obj.objects.filter(polity=polity).order_by('year', 'month__pk')
    years = []
    for log in logs:
        if log.year not in years:
            years.append(log.year)
    years.sort(reverse=True)
    current_year = years[0] + 1
    for month in Month.objects.all():
        LogEntry.objects.create(
            polity=polity,
            year=current_year,
            month=month)
    return redirect('%s:%s' % (app_name, b_plural), polity_id=polity_id, current_year=current_year)


def log_entry_edit(request, pk, polity_id, current_year):
    obj_name_s = b_name
    obj_name = b_name.replace(' ', '_')
    obj_plural = b_plural.replace(' ', '_')
    item = get_object_or_404(b_obj, pk=pk)
    if request.method == "POST":
        form = b_form(request.POST, instance=item)
        if form.is_valid():
            form.save(commit=True)
            return redirect(
                '%s:%s' % (app_name, b_plural), polity_id=polity_id, current_year=current_year
            )
    else:
        form = b_form(instance=item)
    return render(
        request, '%s/edit.html' % app_name, {'title': obj_name_s.title(), 'form': form}
    )
