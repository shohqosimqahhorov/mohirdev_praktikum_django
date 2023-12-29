from django.urls import path
from .views import (
    news_list,
    news_detail,
    homePageView,
    ContactPageView,
    HomePageView,
    LocalNewsView,
    PoliticNewsView,
    TechNewsView,
    SportNewsView,
    SocietyNewsView
)
urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('local/', LocalNewsView.as_view(), name='local_news'),
    path('politic/', PoliticNewsView.as_view(), name='politic_news'),
    path('tech/', TechNewsView.as_view(), name='tech_news'),
    path('sport/', SportNewsView.as_view(), name='sport_news'),
    path('society/', SocietyNewsView.as_view(), name='society_news')
]
