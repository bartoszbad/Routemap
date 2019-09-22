from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from routemap.forms import AddUserForm, LoginForm, AddRouteForm, AddSpotForm, AddListForm
from routemap.models import Route, PhotoSpots, RouteList


class MainView(View):
    def get(self, request):
        order_by = "-"
        order_by += request.GET.get('order_by', 'id')
        routes = Route.objects.all().order_by(order_by)

        if request.user.is_authenticated:
            lists = RouteList.objects.filter(user=request.user).order_by("pk")
            return render(request, 'main_page.html', context={"routes": routes,
                                                              "lists": lists,
                                                              })

        return render(request, 'main_page.html', context={"routes": routes,
                                                          })

    def post(self, request):
        route_list_name = request.POST["list_name"]
        route_pk = request.POST["route_pk"]
        expand_list = RouteList.objects.get(user=request.user, name=route_list_name)
        #print(expand_list)
        adding_route = Route.objects.get(pk=route_pk)
        #print(adding_route)
        if adding_route in expand_list.routes.all():
            #print("Juz jest")
            message = "Dodałeś już tą trasę do listy wcześniej!"
        else:
            expand_list.routes.add(adding_route)
            message = "Dodano trasę"
        messages.add_message(request, messages.INFO, message)

        return redirect(reverse("routes"))


class SpotsView(View):
    def get(self, request):
        spots_list = PhotoSpots.objects.all()
        paginator = Paginator(spots_list, 3)
        page = request.GET.get('page')
        spots = paginator.get_page(page)
        return render(request, "photo_spots.html", context={"spots": spots})


class AboutPageView(View):
    def get(self, request):
        return render(request, "about_page.html")


class AboutMeView(View):
    def get(self, request):
        return render(request, "about_me.html")


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        btn = "Zarejestruj"
        return render(request, "form.html", context={"form": form,
                                                     "submit_btn": btn,
                                                     })
    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            user = User.objects.create_user(username=username, email=email, password=password)

            RouteList.objects.create(name="Przejechane", user=user)
            RouteList.objects.create(name="Chce przejechać", user=user)

            return redirect(reverse('login_view'))

        btn = "Zarejestruj"

        return render(request, "form.html", context={"form": form,
                                                     "submit_btn": btn,
                                                     "message": "Podano niepoprawe dane!"
                                                     })


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        btn = "Zaloguj"
        return render(request, "form.html", context={"form": form,
                                                     "submit_btn": btn,
                                                     })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["login"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                url = request.GET.get('next', '/')
                return redirect(url)
            else:
                return render(request, "login_view.html", context={"message": "Podałeś błędą nazwę użytkownika lub hasło"})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('routes'))


class AddRouteView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddRouteForm()
        btn = "Dodaj"
        return render(request, "form.html", context={"form": form,
                                                         "submit_btn": btn,
                                                         })

    def post(self, request):
        form = AddRouteForm(request.POST)
        if form.is_valid():
            starts = form.cleaned_data["starts"]
            ends = form.cleaned_data["ends"]
            country = form.cleaned_data["country"]
            region = form.cleaned_data["region"]
            description = form.cleaned_data["description"]
            surface_condition = form.cleaned_data["surface_condition"]
            scenic_rating = form.cleaned_data["scenic_rating"]
            funny_to_drive = form.cleaned_data["funny_to_drive"]
            overal_rating = form.cleaned_data["overal_rating"]
            embed_view = form.cleaned_data["embed_view"]
            Route.objects.create(starts=starts, ends=ends, country=country, region=region,
                                 description=description, surface_condition=surface_condition,
                                 scenic_rating=scenic_rating, funny_to_drive=funny_to_drive,
                                 overal_rating=overal_rating, embed_view=embed_view)

            return redirect(reverse('routes'))

        btn = "Dodaj"

        return render(request, "form.html", context={"form": form,
                                                         "submit_btn": btn,
                                                         "message": "Podano niepoprawe dane!"
                                                         })


class AddSpotView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddSpotForm()
        btn = "Dodaj"
        return render(request, "form.html", context={"form": form,
                                                     "submit_btn": btn,
                                                     })

    def post(self, request):
        form = AddSpotForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            # photo_path = form.cleaned_data["photo_path"]
            # cordinates = form.cleaned_data["cordinates"]
            # iframe = form.cleaned_data["iframe"]
            # PhotoSpots.objects.create(photo_path=photo_path, cordinates=cordinates, iframe=iframe)
            return redirect(reverse('spots'))

        btn = "Dodaj"

        return render(request, "form.html", context={"form": form,
                                                     "submit_btn": btn,
                                                     "message": "Podano niepoprawe dane!"
                                                     })


class UserListsView(LoginRequiredMixin, View):
    def get(self, request):
        lists = RouteList.objects.filter(user=request.user).order_by("pk")
        form = AddListForm()
        btn = "Dodaj"
        return render(request, "lists.html", context={"lists": lists,
                                                      "form": form,
                                                      "submit_btn": btn,
                                                      })

    def post(self, request):
        form = AddListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            RouteList.objects.create(name=name, user=request.user)
            return redirect(reverse("lists"))

        btn = "Dodaj"

        return render(request, "form.html", context={"form": form,
                                                     "submit_btn": btn,
                                                     "message": "Podano niepoprawe dane!"
                                                     })




