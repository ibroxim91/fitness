from django.shortcuts import render
from django.views import View
from locals import lang_packages
# Create your views here.

class HomeView(View):

    def get(self, request):
        return render(request, "index.html")
