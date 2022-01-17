from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('login/user/', views.user_login, name='user_login'),
    path('logout/user/', views.user_logout, name='user_logout'),
    path('user/<str:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('update/user/<str:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('delete/user/<str:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    
    path('thing_list/', views.ThingListView.as_view(), name='thing_list'),
    path('thing/<str:pk>/', views.ThingDetailView.as_view(), name='thing_detail'),
    path('delete/thing/<str:pk>/', views.ThingDeleteView.as_view(), name='thing_delete'),
    path('update/thing/<str:pk>/', views.ThingUpdateView.as_view(), name='thing_update'),

    path('create/attraction/', views.AttractionCreateView.as_view(), name='attraction_create'),
    path('create/tour/', views.TourCreateView.as_view(), name='tour_create'),
    path('create/food/', views.FoodCreateView.as_view(), name='food_create'),
    path('create/outdoor/', views.OutdoorCreateView.as_view(), name='outdoor_create'),
    path('create/shopping/', views.ShoppingCreateView.as_view(), name='shopping_create'),

    path('create/comment/thing/<str:thing_pk>/', views.CommentCreateView.as_view(), name='comment_create'),
    path('update/comment/<str:pk>/thing/<str:thing_pk>/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('delete/comment/<str:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),

    path('create/plan/', views.PlanCreateView.as_view(), name='plan_create'),
    path('plan/<str:plan_pk>/add/thing/<str:thing_pk>/', views.plan_add, name="plan_add"),
    path('plan/<str:plan_pk>/remove/thing/<str:thing_pk>/', views.plan_remove, name="plan_remove"),
    path('delete/plan/<str:pk>/', views.PlanDeleteView.as_view(), name='plan_delete'),
    path('update/plan/<str:pk>/', views.PlanUpdateView.as_view(), name='plan_update'),
    path('like/plan/<str:plan_pk>/', views.plan_like, name="plan_like"),

    path('create/picture/thing/<str:thing_pk>/', views.PictureCreateView.as_view(), name='picture_create'),
]