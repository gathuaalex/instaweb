from django.urls import path
from  .import views
 
urlpatterns=[
    #routing our view from where a hello function is.
    path("alex/",views.hello,name="index"),
    path("",views.register,name="register"),
    path("log/",views.user_login,name="log_in"),
    path("logout/",views.user_logout,name="logout1")
    ]