from django.urls import path
from .views import CatCreateView, CatDeleteView, CatListView, CatDetailView, CatUpdateView, MissionsListView


urlpatterns = [
 
    #Cat endpoints
    path('cats/create/', CatCreateView.as_view(), name='cat-create'),
    path('cats/', CatListView.as_view(), name='cat-list'),
    path('cats/<int:id>/delete/', CatDeleteView.as_view(), name='cat-delete'),
    path('cats/<int:id>/', CatDetailView.as_view(), name='cat-detail'),
    path('cats/<int:id>/update-salary/', CatUpdateView.as_view(), name='cat-update'),


    #Missions endpoints
    path('missions/', MissionsListView.as_view(), name='mission-list-view'),
]