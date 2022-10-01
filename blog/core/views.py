

from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin


from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.views.generic import( DetailView ,
                                 ListView,
                                 CreateView )
from django.views.generic.edit import CreateView ,DeleteView,UpdateView
from core.forms import *
from.models import *
from django.contrib.auth.models import User
# Create your views here.
def  hello(request):
    omar="omaruuu"
    context={"omar":omar}
    return render (request,"core/home.html",context)

class createpost(LoginRequiredMixin,CreateView):
    form_class=postform
    model=Post

    template_name= "core/createpost.html"


    def form_valid(self, form) :
       form.instance.author = self.request.user 
       
       return super().form_valid(form)
    success_url="/core/posts"  

class postDetailview(DetailView):
    model=Post
    template_name= "core/post_detail.html"  


# def  bookslistvieww(request): 

#   posts=Post.objects.all()
 
#   x=User.objects.all()
  
#   context={"postlist":posts,"x":x}
#   return render   (request,"core/posts.html",context) 

class Postlistview(LoginRequiredMixin , ListView):
    model=Post
    # ordering=('-date_posted') 
    context_object_name='postlist'
    template_name= "core/posts.html"    
    paginate_by=3


class User_Postlistview(LoginRequiredMixin , ListView):
    model=Post
    ordering=('-date_posted') 
    context_object_name='postlist'
    template_name= "core/userposts.html"    
    paginate_by=3
    def get_queryset(self) :
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class postdelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name="core/deletepost.html"
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False     
        
    success_url="/core/posts"     
 

class Updatpost(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Post
    form_class=postform
  
    template_name= "core/createpost.html"

    

    def form_valid(self, form) :
       form.instance.author = self.request.user 
       
       return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False     
        