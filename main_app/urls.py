from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('frogs/', views.frogs_index, name='index'),
    path('frogs/<int:frog_id>/', views.frogs_detail, name='detail'),
    path('frogs/create/', views.FrogCreate.as_view(), name='frogs_create'),
    path('frogs/<int:pk>/update/', views.FrogUpdate.as_view(), name='frogs_update'),
    path('frogs/<int:pk>/delete/', views.FrogDelete.as_view(), name='frogs_delete'),
    path('frogs/<int:frog_id>/add_feeding/',views.add_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
