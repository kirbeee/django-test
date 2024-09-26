from django.urls import path
from user import views as user_views
urlpatterns = [
    path('', user_views.UsersView.as_view(), name='users_list_create'),  # 註冊 UsersView 的 GET 和 POST 請求
]