from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def show_all_items(
        request, app_name, obj, obj_plural,
        sort=None, sort_2=None, sort_3=None, sort_4=None, sort_5=None
):
    obj_plural_s = obj_plural
    obj_plural = obj_plural.replace(' ', '_')
    if sort is None:
        items = obj.objects.all()
    elif sort_2 is None:
        items = obj.objects.order_by(sort)
    elif sort_3 is None:
        items = obj.objects.order_by(sort, sort_2)
    elif sort_4 is None:
        items = obj.objects.order_by(sort, sort_2, sort_3)
    elif sort_5 is None:
        items = obj.objects.order_by(sort, sort_2, sort_3, sort_4)
    else:
        items = obj.objects.order_by(sort, sort_2, sort_3, sort_4, sort_5)
    return render(
        request, '%s/%s.html' % (app_name, obj_plural),
        {'title': obj_plural_s.title(), obj_plural: items}
    )


def create_item(
        request, app_name, obj_name, obj_form, obj_plural,
        tgt=None, fast_commit=False
):
    obj_name_s = obj_name
    obj_name = obj_name.replace(' ', '_')
    obj_plural = obj_plural.replace(' ', '_')
    if tgt is None:
        tgt = '%s:%s' % (app_name, obj_plural)
    if request.method == "POST":
        form = obj_form(request.POST)
        if form.is_valid():
            if not fast_commit:
                instance = form.save(commit=False)
                instance.save()
            else:
                form.save(commit=True)
            return redirect(tgt)
    else:
        form = obj_form()
    return render(
        request, '%s/edit.html' % app_name, {'title': obj_name_s.title(), 'form': form}
    )


def edit_item(
        request, app_name, pk, obj, obj_name, obj_form, obj_plural,
        tgt=None, fast_commit=False
):
    obj_name_s = obj_name
    obj_name = obj_name.replace(' ', '_')
    obj_plural = obj_plural.replace(' ', '_')
    if tgt is None:
        tgt = '%s:%s' % (app_name, obj_plural)
    item = get_object_or_404(obj, pk=pk)
    if request.method == "POST":
        form = obj_form(request.POST, instance=item)
        if form.is_valid():
            if not fast_commit:
                instance = form.save(commit=False)
                instance.save()
            else:
                form.save(commit=True)
            return redirect(tgt)
    else:
        form = obj_form(instance=item)
    return render(
        request, '%s/edit.html' % app_name, {'title': obj_name_s.title(), 'form': form}
    )


def delete_item(request, app_name, pk, obj, obj_plural, tgt=None):
    obj_plural = obj_plural.replace(' ', '_')
    if tgt is None:
        tgt = '%s:%s' % (app_name, obj_plural)
    item = get_object_or_404(obj, pk=pk)
    item.delete()
    return redirect(tgt)