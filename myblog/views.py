from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

#def home(request):
#  return render(request, 'home.html', {})
# from django.http import HttpResponse
class HomeView(ListView):
  model = Post
  template_name = 'home.html'

class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_detail.html'

# def home(request):
#  return HttpResponse('Hello world')