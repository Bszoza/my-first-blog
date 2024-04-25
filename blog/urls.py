from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]

