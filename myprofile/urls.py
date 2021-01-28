from django.urls import path
from . import views

urlpatterns = [
    path('', views.myprofile, name="myprofile"),
    path('know_more/' ,views.know_more, name="Know_more"),
    # path('blog/', views.blog, name="blog"),
    path('projects/', views.proj, name="projects"),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('contact/', views.contact, name='contact'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]