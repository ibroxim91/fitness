from .views import *
from django.urls import path



urlpatterns = [
     path("latest/", LatestEntriesFeed()),
    path('', HomeView.as_view(), name="home"  ),
    path('clients', ClientView.as_view(), name="clients"  ),
    path('tarifs',TarifsView.as_view(), name="tarifs"  ),
    path('add_client', AddClientView.as_view(), name="add_client"  ),
    path('add_tarif', AddTarifView.as_view(), name="add_tarif"  ),
    path('update_client/<int:pk>', UpdateClientView.as_view(), name="update_client"  ),

    path('delete_client/<int:pk>', delete_client, name="delete_client"  ),
]