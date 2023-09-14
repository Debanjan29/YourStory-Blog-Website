from django.urls import path
from blog import views

urlpatterns = [
    path("", views.blogHome,name="Home"),    
    path("about/", views.about),
    path("contact/", views.contact,name="contact"),
    path("blog/",views.blog),
    path('blog/<str:slug_incoming>',views.blogPost,name='blogPost'),
    path('search/',views.search),
    path('register/',views.register),
    path('login/',views.loginn,name="login"),
    path('logout/',views.logoutt,name="logout"),
    path('postBlog/',views.post,name="postBlog")
    #path('blog/<str:slug_incoming>/comment',views.blogPost,name='blogPost'),
]