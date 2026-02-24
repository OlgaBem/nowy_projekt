from django.urls import path
from .views import lista_ogloszen
from .views import rezerwuj_ogloszenie
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', lista_ogloszen, name='lista_ogloszen'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('rezerwuj/<int:id>/', rezerwuj_ogloszenie, name='rezerwuj_ogloszenie'),
]


