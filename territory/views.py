from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Territory, Type, Feature, Improvement
from .forms import TerritoryForm, TypeForm, FeatureForm, ImprovementForm


def territories(request):
    territories = Territory.objects.all()
    return render(
        request, 'territory/territories.html',
        {'title': 'Territories', 'territories': territories}
    )


def types(request):
    type = Type.objects.all()
    return render(
        request, 'territory/types.html',
        {'title': 'Terrain Types', 'types': types}
    )


def features(request):
    features = Feature.objects.all()
    return render(
        request, 'territory/features.html',
        {'title': 'Terrain Features', 'features': features}
    )


def improvements(request):
    improvements = Improvement.objects.all()
    return render(
        request, 'territory/improvements.html',
        {'title': 'Terrain Improvements', 'improvements': improvements}
    )
