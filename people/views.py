from common import *
from .models import Person, NobleRank, Award
from .forms import PersonForm, NobleRankForm, AwardForm
from .vars import app_name


# PEOPLE
a_name = 'person'
a_plural = 'people'
a_obj = Person
a_form = PersonForm

def people(request):
    return show_all_items(
        request, app_name, a_obj, a_plural, sort='last_name', sort_2='first_name'
    )
def person_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def person_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def person_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)

# NOBLE RANKS
b_name = 'noble rank'
b_plural = 'noble ranks'
b_obj = NobleRank
b_form = NobleRankForm

def noble_ranks(request):
    return show_all_items(request, app_name, b_obj, b_plural, sort='rank')
def noble_rank_new(request):
    return create_item(request, app_name, b_name, b_form, b_plural, fast_commit=True)
def noble_rank_edit(request, pk):
    return edit_item(request, app_name, pk, b_obj, b_name, b_form, b_plural, fast_commit=True)
def noble_rank_delete(request, pk): return delete_item(request, app_name, pk, b_obj, b_plural)


# AWARDS
c_name = 'award'
c_plural = 'awards'
c_obj = Award
c_form = AwardForm

def awards(request):
    return show_all_items(request, app_name, c_obj, c_plural, sort='name')
def award_new(request):
    return create_item(request, app_name, c_name, c_form, c_plural, fast_commit=True)
def award_edit(request, pk):
    return edit_item(request, app_name, pk, c_obj, c_name, c_form, c_plural, fast_commit=True)
def award_delete(request, pk): return delete_item(request, app_name, pk, c_obj, c_plural)
