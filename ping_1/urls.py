from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('User_Login',views.Login,name='Login'),
    path('',views.Log,name='Log'),
    path('desk',views.desk,name='desk'),
    path('desktop',views.desktop,name='desktop'),
    path('Admin_Registar',views.Reg,name='Reg'),
    path('User_Register',views.Regiss,name='Regiss'),
    path('',views.Logout,name='logout'),
    path('pie',views.pie,name='pie'),
    path('alert',views.alert,name='alert'),
    path('time',views.time,name='time'),
    path('pie2',views.pie,name='pie'),
    path('alert2',views.alert,name='alert'),
    path('ip_save',views.ip_save,name='ip_save'),
    path('chat/', views.chat, name='chat'),
    # Add more URLs as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

