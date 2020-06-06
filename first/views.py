from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from .forms import PostForm
from django.utils import timezone
import json
from django.http import HttpResponseBadRequest,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post,EmailPush,LinePush


# Create your views here.
class Post_list(ListView):
    model = Post
    template_name = 'first/list.html'
    context_object_name = 'posts'
    ordering = ['-created']

class Post_detail(DetailView):
    model = Post
    template_name = 'first/post_detail.html'

class Post_new(LoginRequiredMixin,CreateView):
    
    model = Post
    template_name = 'first/post_forms.html'
    fields = ['title','tokuten','content','name','img','tell','email','url']
    
    def form_valid(self,form):
        form.instance.author == self.request.user
        return super().form.valid(form)

class Post_update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','tokuten','content','name','img','tell','email','url']
    
    def form_valid(self,form):
        form.instance.author == self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.name:
            return True
        return False

class Post_delete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.name:
            return True
        return False
   

def callback(request):
    if request.method == 'POST':
        request_json = json.loads(request.body.decode('utf-8'))
        events = request_json['events']
        line_user_id == events[0]['source']['userid']
        
        if line_user_id =='Udeadbeefdeadbeefdeadbeefdeadbeef':
            pass

        elif events[0]['type'] =='follow':
            LinePush.objects.create(user_id = line_user_id)
        
        elif events[0]['type'] == 'unfollow'
            LinePush.objects.filter(user_id=line_user_id).delete()

    return HttpResponse()        