
from django.urls import path 
from api.v1.tasks import views



urlpatterns = [
    path('login/', views.login_api )

   

]
  