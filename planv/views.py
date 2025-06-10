from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model

from .forms import CustomUserForm
from .models import CustomUser



def index(request):
    return HttpResponse('Index de la pagina')

def create_user(request):
    class Meta:
        User = get_user_model()
    form = CustomUserForm(request.POST)
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
    return render(request, 'createUser.html', {'form': form})
