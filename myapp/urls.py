from django.urls import path
from .views import BlogViews,UserView

urlpatterns = [
    path('Blogs', BlogViews.as_view() , name="post-list"),
    path('Api/Register',UserView.as_view(),name = 'register')

]
