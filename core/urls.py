from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('user/<str:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/update/<str:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<str:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    
    path('thing_list/', views.ThingListView.as_view(), name='thing_list'),
    path('thing/<str:pk>/', views.ThingDetailView.as_view(), name='thing_detail'),
    path('thing/<str:pk>/delete/', views.ThingDeleteView.as_view(), name='thing_delete'),
    path('thing/<str:pk>/update/', views.ThingUpdateView.as_view(), name='thing_update'),

    path('attraction/create/', views.AttractionCreateView.as_view(), name='attraction_create'),
    path('tour/create/', views.TourCreateView.as_view(), name='tour_create'),
    path('food/create/', views.FoodCreateView.as_view(), name='food_create'),
    path('outdoor/create/', views.OutdoorCreateView.as_view(), name='outdoor_create'),
    path('shopping/create/', views.ShoppingCreateView.as_view(), name='shopping_create'),

    path('comment/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<str:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<str:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),

    path('picture/create', views.PictureCreateView.as_view(), name='picture_create'),
]