from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Person, NobleRank, Award
from .forms import PersonForm, NobleRankForm, AwardForm
from .vars import app_name


def people(request):
    people = Person.objects.all()
    return render(
        request, 'people/people.html',
        {'title': 'People', 'people': people}
    )


def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('people:people')
    else:
        form = PersonForm()
    return render(request, 'people/person_edit.html', {'title': 'People', 'form': form})


def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('people:people')
    else:
        form = PersonForm(instance=person)
    return render(request, 'people/person_edit.html', {'title': 'People', 'form': form})


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('people:people')


def noble_ranks(request):
    noble_ranks = NobleRank.objects.all()
    return render(
        request, 'people/noble_ranks.html',
        {'title': 'Noble Ranks', 'noble_ranks': noble_ranks}
    )


def noble_rank_new(request):
    if request.method == "POST":
        form = NobleRankForm(request.POST)
        if form.is_valid():
            noble_rank = form.save(commit=False)
            noble_rank.save()
            return redirect('people:noble_ranks')
    else:
        form = NobleRankForm()
    return render(request, 'people/noble_rank_edit.html', {'title': 'Noble Ranks', 'form': form})


def noble_rank_edit(request, pk):
    noble_rank = get_object_or_404(NobleRank, pk=pk)
    if request.method == "POST":
        form = NobleRankForm(request.POST, instance=noble_rank)
        if form.is_valid():
            noble_rank = form.save(commit=False)
            noble_rank.save()
            return redirect('people:noble_ranks')
    else:
        form = NobleRankForm(instance=noble_rank)
    return render(request, 'people/noble_rank_edit.html', {'title': 'Noble Ranks', 'form': form})


def noble_rank_delete(request, pk):
    noble_rank = get_object_or_404(NobleRank, pk=pk)
    noble_rank.delete()
    return redirect('people:noble_ranks')


def awards(request):
    awards = Award.objects.all()
    return render(
        request, 'people/awards.html',
        {'title': 'Awards', 'awards': awards}
    )


def award_new(request):
    if request.method == "POST":
        form = AwardForm(request.POST)
        if form.is_valid():
            award = form.save(commit=False)
            award.save()
            return redirect('people:awards')
    else:
        form = AwardForm()
    return render(request, 'people/award_edit.html', {'title': 'Awards', 'form': form})


def award_edit(request, pk):
    award = get_object_or_404(Award, pk=pk)
    if request.method == "POST":
        form = AwardForm(request.POST, instance=award)
        if form.is_valid():
            award = form.save(commit=False)
            award.save()
            return redirect('people:awards')
    else:
        form = AwardForm(instance=award)
    return render(request, 'people/award_edit.html', {'title': 'Awards', 'form': form})


def award_delete(request, pk):
    award = get_object_or_404(Award, pk=pk)
    award.delete()
    return redirect('people:awards')
