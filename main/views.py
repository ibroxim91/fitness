from typing import Any
from django.shortcuts import redirect, render ,get_object_or_404
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView
from locals import lang_packages
import datetime
from datetime import timedelta
from .models import Admin, Resident,Tariff
# Create your views here.
today = datetime.datetime.now()
end = today + timedelta(seconds=15)
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .my_permissions import MyPermissionControl
from django.contrib.auth import authenticate, login, logout

# @user_passes_test(lambda user: user.is_superuser)
# @permission_required("main.add_resident")
@login_required
def delete_client(request,pk):
    try:
        resident = get_object_or_404(Resident,pk=pk ) 
    except:
        return JsonResponse({"status":"error"})
    else:
        resident.delete()   
        return JsonResponse({"status":"success"})




class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Resident.objects.all()[:5]

    def item_title(self, item):
        return item.first_name

    def item_description(self, item):
        return item.full_name

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return "/client/1"

class HomeView(MyPermissionControl, View):

    permission_required = "main.add_resident" 
    permission_denied_message = "You do not have permission to"   

    def get(self, request):

        views = request.session.get("views")
        if views is  None:
            views = 1
            request.session["views"] = views
        else:
            views = views + 1
            request.session["views"] = views
            request.session.save()
        response = render(request, "index.html",{"views":views,"page_":"home"} )
     
        # response.set_cookie("views",views , max_age=15)
        return response

class ClientView(MyPermissionControl,View):

    def get(self, request):
        residents = Resident.objects.all()
        return render(request, "clients.html" ,{"residents":residents,"page_":"clients_"})
  

class TarifsView(MyPermissionControl,View):
    def get(self, request):
        tarifs = Tariff.objects.all()
        return render(request, "tarifs.html" ,{"tarifs_":tarifs,"page_":"tarifs"})
    

class AddClientView(MyPermissionControl, CreateView):
    template_name = "add_client.html"
    model = Resident
    fields = "__all__"
    success_url = "/clients"

    def form_valid(self, form):
        resident = form.save()
        if resident.status == "active":
            resident.balans -= resident.tarif.price
            resident.save()
        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["form_title"] = "Mijoz qo'shish"
        context["button_title"] = "Qo'shish"
        return context

class AddTarifView(MyPermissionControl,CreateView):
    template_name = "add_client.html"
    model = Tariff
    fields = "__all__"
    success_url = "/tarifs"


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["form_title"] = "Tarif qo'shish"
        context["button_title"] = "Qo'shish"
        return context

class UpdateClientView(MyPermissionControl,UpdateView):
    template_name = "add_client.html"
    model = Resident
    fields = "__all__"
    success_url = "/clients"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["form_title"] = "Mijoz ma'lumotlarini tahrirlash"
        context["button_title"] = "Saqlash"
        return context

    # resident = Resident.objects.get(id=1)
    # form = UpdateClientViewForm(isinstance=resident)


class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not Admin.objects.filter(username=username).exists():
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        return redirect('/login')


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/login")        
