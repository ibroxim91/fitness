from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView
from locals import lang_packages
import datetime
from datetime import timedelta
from .models import Resident
# Create your views here.
today = datetime.datetime.now()
end = today + timedelta(seconds=15)
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.http import JsonResponse
import json


def delete_client(request,pk):
    try:
        resident = Resident.objects.get(pk=pk)
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

class HomeView(View):

    def get(self, request):
        views = request.session.get("views")
        if views is  None:
            views = 1
            request.session["views"] = views
        else:
            views = views + 1
            request.session["views"] = views
            request.session.save()
        response = render(request, "index.html",{"views":views,} )
     
        # response.set_cookie("views",views , max_age=15)
        return response

class ClientView(View):
    def get(self, request):
        residents = Resident.objects.all()
        return render(request, "clients.html" ,{"residents":residents})

class AddClientView(CreateView):
    template_name = "add_client.html"
    model = Resident
    fields = "__all__"
    success_url = "/clients"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["form_title"] = "Mijoz qo'shish"
        context["button_title"] = "Qo'shish"
        return context

class UpdateClientView(UpdateView):
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