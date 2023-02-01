from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
from .models import NewsTitle
from django.views.generic import TemplateView, ListView
from .crawlingrun import TestCrawling


# Create your views here.
class HomeView(TemplateView):
    template_name = 'crawlingapp/home.html'

class InfoView(TemplateView):
    template_name = 'crawlingapp/info.html'

class NewsListView(ListView):
    model = NewsTitle
    queryset = NewsTitle.objects.all()
    context_object_name = "news_title"

def crawling_run(request):
 
    if request.POST:
        test = TestCrawling()
        test.test_crawling()
        
        #models.NewsTitle.objects.create(test.title)
    
    return render(request,'crawlingapp/crawling.html')


