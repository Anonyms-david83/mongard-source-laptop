from django.urls import path
from . import views

app_name = 'home' # to tell the app that now you have a name
urlpatterns = [
    path("" , views.HomeView.as_view() , name='home'),
    path("post/<post_id>/<slug:post_slug>" , views.PostDetailView.as_view() , name='post_detail'),
    path('post/delete/<int:post_id>/' , views.PostDeleteView.as_view() , name='post_delete'),
    path('post/update/<int:post_id>/' , views.PostUpdateView.as_view() , name='post_update'),
    path('post/create' , views.PostCreateView.as_view() , name='post_create')
]