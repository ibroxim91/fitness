from django.shortcuts import render
from django.views import View
from main.my_permissions import MyPermissionControl
# Create your views here.


class PaymentsView(MyPermissionControl,View):
    def get(self, request, *args, **kwargs):
        context = {"page_":"payments"}
        return render(request, 'payments.html',context)
    

