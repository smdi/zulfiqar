"""Institute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from django.contrib import admin
from institutepro import views
from django.contrib.auth.decorators import login_required
from institutepro.apiviews import FeedbackList ,FeedbackDeatail , UserCreate

urlpatterns = [

    url(r'^$', views.loginview , name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^reg/', views.registrationview),
    url(r'^logout/', views.logout),
    url(r'^forgot/',views.forgotPassword),
    url(r'^home/',login_required( views.home)),
    url(r'^services/',login_required( views.services)),
    url(r'^contacts/', login_required(views.contacts)),
    url(r'^feedback/', login_required(views.feedbacks)),
    url(r'^gallery/',login_required(views.gallery)),
    url(r'^api/feedback/(?P<name>[A-Za-z]+)$',FeedbackDeatail.as_view()),
    url(r'^api/feedback/', FeedbackList.as_view()),
    url(r'^api/users/',UserCreate.as_view())

]














