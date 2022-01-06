from django.urls import path, re_path
from core import views
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    
    path('thing/', views.ThingListView.as_view(), name='thing'),
    path('thing/<str:pk>/', views.ThingDetailView.as_view(), name='thing_detail'),

    path('create_attraction/', login_required(views.AttractionCreateView.as_view()), name='create_attraction'),
    path('create_tour/', login_required(views.TourCreateView.as_view()), name='create_tour'),

    path('add_picture/', login_required(views.PictureCreateView.as_view()), name='add_picture'),


]

# http://127.0.0.1:8000/core/things/?attractions=on