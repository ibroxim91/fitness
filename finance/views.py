from django.shortcuts import render
from django.views import View
# Create your views here.


class PaymentsView(View):
    def get(self, request, *args, **kwargs):
        context = {"page_":"payments"}
        return render(request, 'payments.html',context)
    

