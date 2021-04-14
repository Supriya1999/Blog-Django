from django.urls import path
from .import views

app_name='blog_app'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('home', views.IndexView.as_view(),name='home'),
    path('add_cat/',views.AddCategoryView.as_view(), name='add_cat'),
    path('add/',views.AddView.as_view(), name='add'),
    path('posts/',views.PostsView.as_view(),name='posts'),
    path('<slug:slug>/',views.SingleView.as_view(),name='single'),
    path('edit/<int:pk>/',views.EditView.as_view(),name='edit'),
    path('delete/<int:pk>/',views.Delete.as_view(),name='delete'), 
    path('category/<str:cats>/',views.CategoryView,name='cat_view'),

]