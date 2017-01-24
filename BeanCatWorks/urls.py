from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^about/', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^team/', TemplateView.as_view(template_name="team.html"), name='team'),
    url(r'^product/', TemplateView.as_view(template_name="product.html"), name='product'),
 #   url(r'^accounts/profile/$', TemplateView.as_view(template_name='profile.html'), name='account_profile'),
    url(r'^menu/', TemplateView.as_view(template_name="app_menu.html"), name='menu'),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += staticfiles_urlpatterns()
