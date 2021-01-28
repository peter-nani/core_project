from django.shortcuts import render
from django.views import generic
from .models import Post, projects

# Create your views here.

def myprofile(request):
    return render(request,'Profile.html')
def know_more(request):
    return render(request,'know_more.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def proj(request):
    data = projects.objects.all()
    return render(request,'projects.html',{'data':data})

def contact(request):
    return render(request,'contact.html')