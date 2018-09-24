from django.shortcuts import render
from . models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required





class Blog(generic.ListView):
    model = Post
    template_name ='blog/blogIndex.html'
    paginate_by = 6
    


def blogdetail(request, id):
    blog_details = Post.objects.get(id = id)

    context = {
        'blog_details':blog_details
    }

    return render(request, 'blog/blog-details.html', context)