from django.shortcuts import render, redirect
from .models import News, Autor
from django.views.generic import ListView, View
from .forms import NewsForm
from django.urls import reverse
# Create your views here.

class NewsListView(ListView):
    model = News
    template_name = 'blog/news-list.html'
    context_object_name = 'news'
    queryset = News.objects.filter(activity_flag='a')


class RegisterNews(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'blog/news_form.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            data = news_form.cleaned_data
            new_news = News.objects.create(title=data['title'], content=data['content'], activity_flag='i')
            new_news.save()
        return redirect('news-list')


