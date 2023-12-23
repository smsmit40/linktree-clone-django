from django.contrib import admin
from django.urls import path
from .views import index, page, logout_user, add_link, linktree_page, link_increment, signup_user, delete_link

urlpatterns = [
    path('', index, name='index'),
    path('homepage/', page, name='profile_page'),
    path('register/', signup_user, name='register_user'),
    path('user/logout', logout_user, name='logout'),
    path('links/add', add_link, name='add_link'),
    path('links/delete/<int:id>/', delete_link, name='delete_link'),
    path('page/<int:id>/', linktree_page, name='linktree_page'),
    path('link/<int:pk>/increment/', link_increment, name="increment_link"),
]