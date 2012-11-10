from apps.news.models import News
from apps.core.helpers import render_to
from django.shortcuts import get_object_or_404
# Create your views here.


@render_to('news/article.html')
def article(request, pk):
    article = get_object_or_404(News, pk=pk)
    return {'article': article}


@render_to('news/news.html')
def news(request):
    news = News.objects.all()
    return {'news': news}
