from django.urls import path
from django.conf.urls import include

from . import views
from rest_framework import routers

from .api_rest.viewsets import UsersViewsets

router = routers.DefaultRouter()
router.register(r'contas', UsersViewsets)

app_name = 'users'
passwordpatterns = [
    path('atualizar/', views.UpdatePasswordView.as_view(), name='update_password'),
    path('esqueci/', views.PasswordResetView.as_view(), name='password_reset'),
    path('esqueci/enviado/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('esqueci/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('esqueci/completo/', views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api_rest/', include(router.urls)),
    path('cadastrar/', views.CreateUsersView.as_view(), name='create'),
    path('entrar/', views.LoginUsersView.as_view(), name='login'),
    path('sair/', views.LogoutUsersView.as_view(), name='logout'),
    path('atualizar/cadastro/', views.UpdateUsersView.as_view(), name='update'),

    # password treatment
    path('senha/', include(passwordpatterns)),
]
