# Create your views here.
from apps.core.helpers import render_to, get_object_or_None

from apps.banlist.models import ServerBanList
from apps.banlist.forms import AddServerBanForm

from django.contrib.auth.decorators import login_required

@login_required
@render_to('banlist/index.html')
def index(request):
    users = []
    servers = ServerBanList.objects.filter(owner=request.user)
    form = AddServerBanForm()
    return {'servers': servers, 'users': users, 'form': form}

@login_required
@render_to('banlist/add.html')
def add(request, pk=None):
    instance = get_object_or_None(ServerBanList, pk=pk)
    form = AddServerBanForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            ban = form.save(commit=False)
            ban.owner = request.user
            ban.save()
            return {'redirect': 'banlist:index'}
    return {
        'form': form
    }
