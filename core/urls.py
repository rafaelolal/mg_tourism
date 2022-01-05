from django.urls import path, re_path
from core import views

app_name = 'core'

urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    
    path('thing/', views.ThingListView.as_view(), name='thing'),
    path('add_picture/', views.PictureCreateView.as_view(), name='add_picture'),

    path('create_attraction/', views.AttractionCreateView.as_view(), name='create_attraction'),
    path('thing/attraction/<str:pk>/', views.AttractionDetailView.as_view(), name='attraction_detail'),

    # path('create_attraction/', views.create_attraction, name='create_attraction'),
    path('create_tour/', views.create_tour, name='create_tour'),

]

# http://127.0.0.1:8000/core/things/?attractions=on