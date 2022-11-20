from django.urls import path, include
from . import views

urlpatterns = [
    path("signup/", views.signup, name='signup'),
    path("signin/", views.signin, name='signin'),
    path("signout/", views.signout, name='signout'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("", views.dashboard, name='dashboard'),

    path("activate/<uidb64>/<token>/", views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]