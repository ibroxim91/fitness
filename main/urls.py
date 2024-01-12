from .views import HomeView,ClientView,AddClientView,UpdateClientView
from django.urls import path



urlpatterns = [

    path('', HomeView.as_view(), name="home"  ),
    path('clients', ClientView.as_view(), name="clients"  ),
    path('add_client', AddClientView.as_view(), name="add_client"  ),
    path('update_client/<int:pk>', UpdateClientView.as_view(), name="update_client"  ),
]