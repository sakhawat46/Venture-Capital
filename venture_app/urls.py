from django.urls import path
from venture_app import views

app_name = "venture_app"

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.customerlogin, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('profile/', views.profile, name='profile'),

]