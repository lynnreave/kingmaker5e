from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Person
from .forms import PersonForm


def people(request):
    people = Person.objects.all()
    return render(request, 'people/people.html', {'people': people})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'people/person_detail.html', {'person': person})


def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'people/person_edit.html', {'form': form})


def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm(instance=person)
    return render(request, 'people/person_edit.html', {'form': form})
