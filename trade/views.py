from common import *
from .models import TradeRoute
from .forms import TradeRouteForm
from .vars import app_name

# TRADE ROUTES
a_name = 'trade route'
a_plural = 'trade routes'
a_obj = TradeRoute
a_form = TradeRouteForm

def trade_routes(request):
    return show_all_items(
        request, app_name, a_obj, a_plural, sort='polity__name', sort_2='type',
        get_details=get_trade_route_details,
    )
def trade_route_new(request):
    return create_item(request, app_name, a_name, a_form, a_plural, fast_commit=True)
def trade_route_edit(request, pk):
    return edit_item(request, app_name, pk, a_obj, a_name, a_form, a_plural, fast_commit=True)
def trade_route_delete(request, pk): return delete_item(request, app_name, pk, a_obj, a_plural)


def trade_route_activate(request, pk):
    obj_plural = a_plural.replace(' ', '_')
    tgt = '%s:%s' % (app_name, obj_plural)
    trade_route = get_object_or_404(a_obj, pk=pk)
    trade_route.active = True
    trade_route.save()
    return redirect(tgt)


def trade_route_deactivate(request, pk):
    obj_plural = a_plural.replace(' ', '_')
    tgt = '%s:%s' % (app_name, obj_plural)
    trade_route = get_object_or_404(a_obj, pk=pk)
    trade_route.active = False
    trade_route.save()
    return redirect(tgt)
