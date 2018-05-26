from common import *
from polity.models import Polity


def home(request):
    polities = Polity.objects.all()
    return render(request, 'core/home.html', {'title': 'Home', 'polities': polities})


def dashboard(request, pk):
    polity = get_polity_details(pk)['polity']
    return render(
        request, 'core/dashboard.html', {
            'title': polity.name.upper(),
            'polity': polity,
        }
    )
