from django.urls import path
from accounts import views

# from cms import views

app_name = 'accounts'

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/', views.IndexView.as_view(), name="index"),
    path('create/', views.UserCreateView.as_view(), name="create"),  # 追記
]
