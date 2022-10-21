from django.urls import path
from django.contrib.auth import views as auth_views

from user import views

app_name = "user"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
]
