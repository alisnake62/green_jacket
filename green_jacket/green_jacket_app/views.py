from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


from green_jacket_app.models import Brand, UserCustom, BrandModel, Favorite

def get_colors(is_dark_mode):

    colors = [
        [
            {"1": "#001011", "2":"#042629"},
            {"1": "#FFFFFF", "2":"#FFFFFF"}
        ],
        [
            {"1": "#0F4637", "2":"#266856"},
            {"1": "#A2E1C4", "2":"#93d5b7"}
        ],
        [
            {"1": "#EBD82D", "2":"#f8e74f"},
            {"1": "#001011", "2":"#042629"}
        ]
    ]
    text = ["#FFFFFF", "#001011"]

    index = 0 if is_dark_mode else 1

    return {
        "color1" : colors[0][index],
        "color2" : colors[1][index],
        "color3" : colors[2][index],
        "text": text[index]
    }

def get_context(request):
    context = {}
    try:
        user_name = request.user
        user_custom = UserCustom.objects.get(name=user_name)
        context["dark_mode"] = user_custom.dark_mode
        context["user"] = user_name
        context["connected"] = True
    except:
        context["dark_mode"] = False
        context["connected"] = False

    context["current_path"] = request.path
    context["colors"] = get_colors(context["dark_mode"])
    return context

def signup(request):
    context = get_context(request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = user.username
            user_custom = UserCustom(name=user_name)
            user_custom.save()
            login(request, user)
            return redirect('/green_jacket/home')  # Rediriger vers la page d'accueil ou une autre page
    else:
        form = UserCreationForm()
    context['form'] = form
    return render(request, 'registration/signup.html', context)

@login_required
def home(request):
    # La vue pour la page d'accueil, vous pouvez personnaliser cela

    context = get_context(request)
    return render(request, 'green_jacket/home.html', context)

@login_required
def green_score(request):

    context = get_context(request)
    return render(request, 'green_jacket/green_score.html', context)

def login_view(request):
    context = get_context(request)
    next_params = get_params(request, "next")
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if next_params not in ["None", None, ""]:
                return redirect(next_params)
            else:
                return redirect('/green_jacket/home')
    else:
        form = AuthenticationForm()
    context['form'] = form
    return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/green_jacket/login')

@login_required
def toogle_dark_mode(request):

    context = get_context(request)
    get_params = request.GET
    next_params = get_params.get("next")

    user_custom = UserCustom.objects.get(name=context["user"])
    user_custom.dark_mode = not user_custom.dark_mode
    user_custom.save()

    return redirect(next_params)

@login_required
def toogle_favorite(request):

    context = get_context(request)
    brand_model_id = get_params(request, "brand_model_id")
    type_selected = get_params(request, "type")
    brand_selected = get_params(request, "brand")
    favorite_selected = get_params(request, "favorite")

    user_custom = UserCustom.objects.get(name=context["user"])
    brand_model = BrandModel.objects.get(id=brand_model_id)

    favorite = Favorite.objects.filter(user=user_custom).filter(brand_model=brand_model)
    if len(favorite) == 0:
        favorite = Favorite(
            user=user_custom,
            brand_model=brand_model
        )
        favorite.save()
    else:
        favorite.delete()

    return redirect(f"/green_jacket/brand_models?brand={brand_selected}&type={type_selected}&favorite={favorite_selected}")

def get_params(request, param):
    get_params = request.GET
    return get_params[param] if param in get_params else None

@login_required
def brands(request):

    context = get_context(request)

    brands = Brand.objects.all()

    brands = [brand for brand in brands]
    brands.sort(key=lambda brand:-brand.get_score())

    context["brands"] = brands

    return HttpResponse(render(request, "green_jacket/brands.html", context))

@login_required
def brand_models(request):

    context = get_context(request)

    user_custom = UserCustom.objects.get(name=context["user"])

    brand_selected = get_params(request, "brand")
    favorite_selected = get_params(request, "favorite")
    brand_model_type_selected = get_params(request, "brand_model_type")
    context["brand_selected"] = brand_selected
    context["brand_model_type_selected"] = brand_model_type_selected

    brands_to_filter = Brand.objects.all()
    brands_to_filter = [brand for brand in brands_to_filter]

    brand_model_types_to_filter = [brand_model["type"] for brand_model in BrandModel.objects.all().values("type").distinct()]

    brand_models = BrandModel.objects.all()
    if brand_selected not in ("", None, "None"):
        brand_models = brand_models.filter(brand__name=brand_selected)
    if brand_model_type_selected not in ("", None, "None"):
        brand_models = brand_models.filter(type=brand_model_type_selected)

    brand_models = [model for model in brand_models]

    if favorite_selected == 'on':
        new_brand_models=[]
        for brand_model in brand_models:
            favorite = Favorite.objects.filter(user=user_custom).filter(brand_model=brand_model)
            if len(favorite) == 0:
                pass
            else:
                new_brand_models.append(brand_model)
        brand_models = new_brand_models

    brand_models.sort(key=lambda model:-model.get_score())

    for brand_model in brand_models:
        favorite = Favorite.objects.filter(user=user_custom).filter(brand_model=brand_model)
        if len(favorite) == 0:
            brand_model.favorite = False
        else:
            brand_model.favorite = True

    context["brand_models"] = brand_models
    context["brands_to_filter"] = brands_to_filter
    context["brand_model_types_to_filter"] = brand_model_types_to_filter
    context["favorite_selected"] = favorite_selected

    return HttpResponse(render(request, "green_jacket/brand_models.html", context))