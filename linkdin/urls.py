from django.conf.urls import include, url
from django.contrib import admin
from .views import home, repository, next_page

urlpatterns = [
    # Examples:
    # url(r'^$', 'jitfintask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^data/', home),
    url(r'^get_repo', repository),
    url(r'^get_next_page', next_page)
]
