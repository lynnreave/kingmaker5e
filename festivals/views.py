from common import *
from .models import Festival
from .forms import FestivalForm
from .vars import app_name
from settlements.models import Settlement


# PEOPLE
a_name = 'festival'
a_plural = 'festivals'
a_obj = Festival
a_form = FestivalForm

def festivals(request):
    return show_all_items(
        request, app_name, a_obj, a_plural, sort='polity__name', sort_2='name'
    )
def festival_new(request):
    obj_name_s = a_name
    obj_name = a_name.replace(' ', '_')
    obj_plural = a_plural.replace(' ', '_')
    tgt = '%s:%s' % (app_name, obj_plural)
    if request.method == "POST":
        form = a_form(request.POST)
        #form.target_settlement.queryset = Settlement.objects.filter(territory=the_company.id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            return redirect(tgt)
    else:
        form = a_form()
    return render(
        request, '%s/edit.html' % app_name, {'title': obj_name_s.title(), 'form': form}
    )
def festival_edit(request, pk):
    obj_name_s = a_name
    obj_name = a_name.replace(' ', '_')
    obj_plural = a_plural.replace(' ', '_')
    tgt = '%s:%s' % (app_name, obj_plural)
    item = get_object_or_404(a_obj, pk=pk)
    if request.method == "POST":
        form = a_form(request.POST, instance=item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            return redirect(tgt)
    else:
        form = a_form(instance=item)
    return render(
        request, '%s/edit.html' % app_name, {'title': obj_name_s.title(), 'form': form}
    )
def festival_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)
