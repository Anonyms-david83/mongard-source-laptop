from django.shortcuts import render , redirect
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostUpdateForm

class HomeView(View):
    def get(self , request):
        posts = Post.objects.all()
        return render(request , 'home/index.html' , context={"posts" : posts})

class PostDetailView(View):
    def get(self , request , post_id , post_slug):
        post = Post.objects.get(id=post_id , slug=post_slug)
        return render(request , 'home/detail.html' , {'post' : post})

class PostDeleteView(LoginRequiredMixin , View):
    def get(self , request , post_id):
        post = Post.objects.get(pk = post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request , 'post delete d sucesffully' , 'success')
        else:
            messages.danger(request , 'post could not be deleted' , 'danger')
        return redirect("home:home")

class PostUpdateView(LoginRequiredMixin , View):
    form_class = PostUpdateForm

    def dispatch(self , request , *args , **kwargs):
        post = Post.objects.get(pk=kwargs['post_id']) #kwargs is a dictionary that contains args , post_id is located in there
        if not post.user.id == request.user.id:
            messages.error(request , 'you cant update this post' , 'dnager')
            return redirect('home:home')
        return super().dispatch(request , *args , **kwargs)

    def get(self , request , post_id):
        post = Post.objects.get(pk = post_id)
        # if not post.user.id == request.user.id:
        #     messages.error(request , 'you cant update this post' , 'danger')
        #     return redirect('home:home')

    def post(self , request , post_id):
        post = Post.objects.get(pk=post_id)
        # if not post.user.id == request.user.id:
        #     messages.error(request, 'you cant update this post', 'danger')
        #     return redirect('home:home')