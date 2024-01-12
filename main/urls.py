from .views import HomeView,ClientView,AddClientView, LatestEntriesFeed,UpdateClientView,delete_client
from django.urls import path



urlpatterns = [
     path("latest/", LatestEntriesFeed()),
    path('', HomeView.as_view(), name="home"  ),
    path('clients', ClientView.as_view(), name="clients"  ),
    path('add_client', AddClientView.as_view(), name="add_client"  ),
    path('update_client/<int:pk>', UpdateClientView.as_view(), name="update_client"  ),

    path('delete_client/<int:pk>', delete_client, name="delete_client"  ),
]