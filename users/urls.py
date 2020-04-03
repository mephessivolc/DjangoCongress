from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('cadastrar/', views.CreateUsers.as_view(), name='create_user'),
    path('entrar/', views.LoginUsers.as_view(), name='login'),
    path('sair/', views.LogoutUsers.as_view(), name='logout'),
    path('atualizar/senha/', views.UpdatePasswordUserView.as_view(), name='update_password'),
    path('atualizar/cadastro/', views.UpdateUserView.as_view(), name='update_user'),

    # export csv
    path('exportar/csv', views.UserCSVNameList.as_view(), name='csv_user_name_export'),
    path('exportar/email/csv', views.UserCSVNameEmailList.as_view(), name='csv_user_name_email_export'),

    # export pdf
    path('exportar/pdf', views.UserPDFNameList.as_view(), name='pdf_user_name_export'),
    path('exportar/email/pdf', views.UserPDFNameEmailList.as_view(), name='pdf_user_email_export'),
    path('exportar/inscritos_ja_pagos/pdf', views.UserPDFNameSubscribedList.as_view(), name='pdf_user_subscribed_export'),
    path('exportar/inscritos_nao_pagos/pdf', views.UserPDFNameNoSubscribedList.as_view(), name='pdf_user_no_subscribed_export'),

    # password treatment
    path('esqueci_minha_senha/', views.PasswordUserResetView.as_view(), name='password_reset'),
    path('esqueci_minha_senha/enviado/', views.PasswordUserResetDoneView.as_view(), name='password_reset_done'),
    path('esqueci_minha_senha/<uidb64>/<token>/', views.PasswordUserResetConfirmView.as_view(), name='password_reset_confirm'),
    path('esqueci_minha_senha/completo/', views.PasswordUserResetCompleteView.as_view(), name="password_reset_complete"),
]
