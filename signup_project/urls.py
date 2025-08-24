from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView
from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login-register/', views.login_register_view, name='login_register'),
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('book-now/', views.book_now_view, name='book_now'),
    path('accounts/', include('allauth.urls')),

    # Password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


