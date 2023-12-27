from django.shortcuts import redirect,render
from .forms import CreateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    return render(request,'index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    context = {'form':form}
    return render(request,'Register.html',context=context)

@login_required(login_url='two_factor:login')
def dashboard(request):
    return render(request,'Dashboard.html')

def user_logout(request):
    auth.logout(request)
    return redirect('')

def account_locked(request):
    return render(request,'account-locked.html')