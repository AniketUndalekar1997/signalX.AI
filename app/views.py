from django.shortcuts import render
from .forms import UserForm
from django.contrib import messages
from .models import User

# Create your views here.

# Create your views here.
def userHome(request):
    if request.method == 'POST':
        p_form = UserForm(request.POST)
        if p_form.is_valid():
            name = p_form.cleaned_data['name']
            city = p_form.cleaned_data['city']
            user = User(name=name, city=city)
            user.save()
            messages.success(request, f'** User information is saved!')
    p_form = UserForm()
    return render(request, 'home.html', {'form':p_form, 'search':'active'})

def getUsers(request):
    template = 'showUser.html'
    result={}
    result = User.objects.all()
    context = {'users':result, 'search':'active'}
    return render(request, template, context)
