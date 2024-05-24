from django.urls import re_path, path
from . import views
from .views import *
from django.contrib.auth import views as auth_views    #




urlpatterns = [
    re_path('login/', views.login),
    re_path('signup/', views.signup),
    re_path('logout/', views.logout_user),
    re_path('test_token/', views.test_token),
    path('change_password/', change_password, name='change_password'),
    re_path('users/', UserListView.as_view(), name='user-list'),
    re_path('add_user/', views.addUser),                                    #to add users manually           
    re_path('suspend_users/',views.suspend_users, name='user-status'),      #to change user status
    # forget password :    
    path('external-link/', external_link_view, name='external-link-url'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('accounts/reset/done/', MyPasswordResetCompleteView.as_view(), name="password_reset_complete"),


]
