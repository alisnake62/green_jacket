from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


from green_jacket_app.models import Brand

# from bfmAdmin.models import Export

# from bfmAdmin.utils.exportUtils import ExportUtils
# from bfmAdmin.utils.viewsUtils import ViewsUtils

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/green_jacket/home')  # Rediriger vers la page d'accueil ou une autre page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
    # La vue pour la page d'accueil, vous pouvez personnaliser cela

    context = {}
    context["user"] = request.user
    return render(request, 'green_jacket/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/green_jacket/home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/green_jacket/login')

def toto(request):

    # # Check Authenticate
    # nextLogin = "green_jacket/toto/"
    # if not request.user.is_authenticated: return redirect(f"/green_jacket/login/?next=/{nextLogin}")

    context = {}
    context["message"] = "titiTATA"

    brands = [brand for brand in Brand.objects.all()]

    context["brands"] = brands
    return HttpResponse(render(request, "green_jacket/toto.html", context))