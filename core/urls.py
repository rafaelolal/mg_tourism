from django.urls import path, re_path
from core import views
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('user/<str:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/update/<str:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    
    path('thing_list/', views.ThingListView.as_view(), name='thing_list'),
    path('thing/<str:pk>/', views.ThingDetailView.as_view(), name='thing_detail'),
    path('thing/<str:pk>/delete/', views.ThingDeleteView.as_view(), name='thing_delete'),
    path('thing/<str:pk>/update/', views.ThingUpdateView.as_view(), name='thing_update'),

    path('attraction/create/', login_required(views.AttractionCreateView.as_view()), name='attraction_create'),
    path('tour/create/', login_required(views.TourCreateView.as_view()), name='tour_create'),
    path('food/create/', login_required(views.FoodCreateView.as_view()), name='food_create'),
    path('outdoor/create/', login_required(views.OutdoorCreateView.as_view()), name='outdoor_create'),
    path('shopping/create/', login_required(views.ShoppingCreateView.as_view()), name='shopping_create'),

    path('comment/create/', login_required(views.CommentCreateView.as_view()), name='comment_create'),
    path('comment/<str:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<str:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),

    path('picture/create', login_required(views.PictureCreateView.as_view()), name='picture_create'),
]

# http://127.0.0.1:8000/core/things/?attractions=on