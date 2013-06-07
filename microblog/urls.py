from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.views.generic import TemplateView
from . import views

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^blog/', include("blog.urls", namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
)
