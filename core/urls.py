from django.urls import path, re_path
from core import views
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    
    path('thing_list/', views.ThingListView.as_view(), name='thing_list'),
    path('thing_list/<str:pk>/', views.ThingDetailView.as_view(), name='thing_detail'),
    path('thing_list/delete/<str:pk>/', views.ThingDeleteView.as_view(), name='thing_delete'),
    path('thing_list/update/<str:pk>/', views.ThingUpdateView.as_view(), name='thing_update'),

    path('create_attraction/', login_required(views.AttractionCreateView.as_view()), name='create_attraction'),
    path('create_tour/', login_required(views.TourCreateView.as_view()), name='create_tour'),
    path('create_food/', login_required(views.FoodCreateView.as_view()), name='create_food'),
    path('create_outdoor/', login_required(views.OutdoorCreateView.as_view()), name='create_outdoor'),
    path('create_shopping/', login_required(views.ShoppingCreateView.as_view()), name='create_shopping'),

    path('add_picture/', login_required(views.PictureCreateView.as_view()), name='add_picture'),
]

# http://127.0.0.1:8000/core/things/?attractions=on