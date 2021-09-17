from django.urls import path  
from . import views  

app_name = "clean"

urlpatterns = [
    path("",views.index,name = "index"),
    path("login/", views.dev_login,name="login"),
    path("register/", views.dev_register, name = "register"),
    path("user/<int:pk>/",views.after_login, name="after_login"),
    path("logout/", views.dev_logout, name="logout"),
    path("user/<int:user_pk>/services/", views.dev_services, name="dev_services"),
    path("user/<int:user_pk>/add_services/", views.all_avail_services, name="all_avail_services"),
    path("user/<int:user_pk>/points/", views.dev_points, name="dev_points"),
    path("user/<int:user_pk>/add_service/<int:service_pk>/",views.dev_add_service,name="dev_add_service"),
    path("user/<int:user_pk>/done_service/<int:service_pk>/",views.dev_service_mark_as_done,name="dev_service_mark_as_done")
    
]