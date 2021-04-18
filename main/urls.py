from django.contrib import admin
from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('',views.HomepageView.as_view(),name="home"),
    path('theme/<slug:theme_slug>/',views.ThemeView,name="theme"),
    path('theme/<slug:theme_slug>/<slug:post_slug>/',views.PostView,name="post"),
    path('add_theme/',views.ThemeCreateView.as_view(),name='add_theme'),
    path('add_post/',views.PostCreateView.as_view(),name='add_post'),
    path('theme/<slug:theme_slug>/<slug:post_slug>/leave_comment',views.leave_comment,name="leave_comment"),
    path('<int:pk>/delete-comment/',views.CommentDeleteView.as_view(),name='delete_comment'),
    path('<int:pk>/delete-theme/',views.ThemeDeleteView.as_view(),name='delete_theme'),
    path('<int:pk>/delete-post/',views.PostDeleteView.as_view(),name='delete_post'),
    path('<int:pk>/update-theme/',views.ThemeUpdateView.as_view(),name='update_theme'),
    path('<int:pk>/update-post/',views.PostUpdateView.as_view(),name='update_post'),
    path('<slug:theme_slug>/add_post/',views.PostCreateView2.as_view(),name='add_post2')

]
#«Блять, забыл рансервер запустить, охуенно» ©️Хауди
