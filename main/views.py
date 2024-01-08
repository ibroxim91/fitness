from django.shortcuts import render
from django.views import View
from locals import lang_packages
import datetime
from datetime import timedelta
# Create your views here.

today = datetime.datetime.now()
end = today + timedelta(seconds=15)


class HomeView(View):

    def get(self, request):
        views = request.COOKIES.get("views",0 )
        print()
        print(request.COOKIES)
        print()
        views = int(views) + 1
        response = render(request, "index.html",{"views":views} )
     
        # response.set_cookie("views",views , max_age=15)
        return response

class ClientView(View):
    def get(self, request):
        return render(request, "clients.html" )