from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('author/<name>', views.getauthor, name="author"),
    path('article/<int:id>', views.getsingle, name="single_post"),
    path('topic/<name>', views.gettopic, name="topic"),
    path('login', views.getlogin, name="login"),
    path('logout', views.userlogout, name="logout"),
    path('create', views.getcreate, name="create"),
]
