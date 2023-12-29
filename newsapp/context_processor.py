from .models import News, Category


def latest_news(request):
    latest_news = News.published.all().order_by('-publish_time')[:8]
    categories = Category.objects.all()
    context = {
        'latest_news': latest_news,
        'categories': categories
    }

    return context