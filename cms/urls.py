from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # ユーザーの健康状態
    path('userhealth', views.userhealth_list, name='userhealth_list'),
    path('userhealth/add', views.userhealth_edit, name='userhealth_add'),
    path('userhealth/mod/<int:userhealth_id>', views.userhealth_edit, name='userhealth_mod'),
    path('userhealth/del/<int:userhealth_id>', views.userhealth_del, name='userhealth_del'),
]
