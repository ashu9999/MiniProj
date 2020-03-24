from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'alumni'

urlpatterns = [

    path('signup/', views.signup, name='signup'),
]