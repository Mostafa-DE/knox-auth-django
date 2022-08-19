from django.urls import path
from knox import views as knox_views

from demo.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
]
