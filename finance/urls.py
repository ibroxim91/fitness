from .views import *
from django.urls import path

app_name = "finance"

urlpatterns = [
     path("payments", PaymentsView.as_view() , name="payments"),

]