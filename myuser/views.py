from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import MyUser
from .forms import PostForm

# Create your views here.
def index(request):
  posts = MyUser.objects.all()
  form = PostForm()
  context = {'posts': posts, 'form': form, }
  return render(request, 'myuser/index.html', context)

def create(request):
  form = PostForm(request.POST)
  form.save(commit=True)
  return HttpResponseRedirect(reverse('myuser:index'))

def delete(request, id=None):
  post = get_object_or_404(MyUser, pk=id)
  post.delete()
  return HttpResponseRedirect(reverse('myuser:index'))