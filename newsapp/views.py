from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm
# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        'news_list': news_list
    }

    return render(request, 'news/news_list.html', context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }

    return render(request, 'news/news_detail.html', context)

def homePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:5]
    local_one = News.published.filter(category__name="Ijtimoiy").order_by('-publish_time')[:1]
    local_news = News.published.all().filter(category__name="Ijtimoiy").order_by('-publish_time')[1:6]
    context = {
        'news_list': news_list,
        'categories': categories,
        'local_one': local_one,
        'local_news': local_news[:5]
    }

    return render(request, 'news/index.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        # context['local_one'] = News.published.filter(category__name="Ijtimoiy").order_by('-publish_time')[:1]
        context['local_news'] = News.published.all().filter(category__name="Ijtimoiy").order_by('-publish_time')[:5]
        context['politic_news'] = News.published.all().filter(category__name="Siyosat").order_by('-publish_time')[:5]
        context['sport_news'] = News.published.all().filter(category__name="Sport").order_by('-publish_time')[:5]
        context['tech_news'] = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[:5]

        return context


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request,'news/contact.html', context)

    def post(self,request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaningiz uchun rahmat</h2>")
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)


class LocalNewsView(ListView):
    model = News
    template_name = 'news/local_news.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Ijtimoiy')
        return news

class PoliticNewsView(ListView):
    model = News
    template_name = 'news/politic_news.html'
    context_object_name = 'politic_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Siyosat')
        return news


class TechNewsView(ListView):
    model = News
    template_name = 'news/tech_news.html'
    context_object_name = 'tech_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnologiya')
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport_news.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news


class SocietyNewsView(ListView):
    model = News
    template_name = 'news/society_news.html'
    context_object_name = 'society_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Jamiyat')
        return news