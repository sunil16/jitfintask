from django.conf.urls import include, url
from django.contrib import admin
from .views import home,fun

urlpatterns = [
    # Examples:
    # url(r'^$', 'jitfintask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^data/', home),
    url(r'^hello/', fun),
]
