from common import *


def home(request):
    return render(request, 'core/home.html', {'title': 'Home'})
