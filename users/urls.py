from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('pending', views.approval_pending, name='approval_pending'),
    path('blocked', views.account_blocked, name='account_blocked'),
    path('fill_missing', views.fill_missing, name='fill_missing'),
    path('on_external_oauth', views.on_external_oauth, name='on_external_oauth'),
    path('logout', views.logout, name='logout'),
    path('send_email', views.send_email, name='send_email'),
    path('verify_email', views.verify_email, name="verify_email")
]
