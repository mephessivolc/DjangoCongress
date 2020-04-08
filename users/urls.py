from django.urls import path
from django.conf.urls import include

from . import views
from rest_framework import routers

from .api_rest.viewsets import UsersViewsets

router = routers.DefaultRouter()
router.register(r'contas', UsersViewsets)

app_name = 'users'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api_rest/', include(router.urls)),
    path('cadastrar/', views.CreateUsersView.as_view(), name='create'),
    path('entrar/', views.LoginUsersView.as_view(), name='login'),
    path('sair/', views.LogoutUsersView.as_view(), name='logout'),
    path('atualizar/cadastro/', views.UpdateUsersView.as_view(), name='update'),
    path('atualizar/senha/', views.UpdatePasswordView.as_view(), name='update_password'),

    # export csv
    # path('exportar/csv', views.UserCSVNameList.as_view(), name='csv_user_name_export'),
    # path('exportar/email/csv', views.UserCSVNameEmailList.as_view(), name='csv_user_name_email_export'),

    # export pdf
    # path('exportar/pdf', views.UserPDFNameList.as_view(), name='pdf_user_name_export'),
    # path('exportar/email/pdf', views.UserPDFNameEmailList.as_view(), name='pdf_user_email_export'),
    # path('exportar/inscritos_ja_pagos/pdf', views.UserPDFNameSubscribedList.as_view(), name='pdf_user_subscribed_export'),
    # path('exportar/inscritos_nao_pagos/pdf', views.UserPDFNameNoSubscribedList.as_view(), name='pdf_user_no_subscribed_export'),

    # password treatment
    path('esqueci_minha_senha/', views.PasswordResetView.as_view(), name='password_reset'),
    path('esqueci_minha_senha/enviado/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('esqueci_minha_senha/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('esqueci_minha_senha/completo/', views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
