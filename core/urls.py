from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('user/<str:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/<str:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('user/<str:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    
    path('thing_list/', views.ThingListView.as_view(), name='thing_list'),
    path('thing/<str:pk>/', views.ThingDetailView.as_view(), name='thing_detail'),
    path('thing/<str:pk>/delete/', views.ThingDeleteView.as_view(), name='thing_delete'),
    path('thing/<str:pk>/update/', views.ThingUpdateView.as_view(), name='thing_update'),

    path('create/attraction/', views.AttractionCreateView.as_view(), name='attraction_create'),
    path('create/tour/', views.TourCreateView.as_view(), name='tour_create'),
    path('create/food/', views.FoodCreateView.as_view(), name='food_create'),
    path('create/outdoor/', views.OutdoorCreateView.as_view(), name='outdoor_create'),
    path('create/shopping/', views.ShoppingCreateView.as_view(), name='shopping_create'),

    path('thing/<str:thing_pk>/create/comment/', views.CommentCreateView.as_view(), name='comment_create'),
    path('thing/<str:thing_pk>/update/comment/<str:pk>/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<str:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    path('user/<str:owner_pk>/create/plan/', views.PlanCreateView.as_view(), name='plan_create'),
    path('plan/<str:plan_pk>/add/thing/<str:thing_pk>/', views.plan_add, name="plan_add"),
    path('plan/<str:plan_pk>/remove/thing/<str:thing_pk>/', views.plan_remove, name="plan_remove"),
    path('plan/<str:pk>/delete/', views.PlanDeleteView.as_view(), name='plan_delete'),
    path('user/<str:owner_pk>/update/plan/<str:pk>/', views.PlanUpdateView.as_view(), name='plan_update'),
    path('user/<str:user_pk>/like/<str:liking>/plan/<str:plan_pk>/', views.plan_like, name="plan_like"),

    path('thing/<str:thing_pk>/create/picture/', views.PictureCreateView.as_view(), name='picture_create'),

]