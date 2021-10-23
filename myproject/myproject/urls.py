"""
@Docs
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path("", TemplateView.as_view(template_name="myapp/home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("", include('myproject.myapp.features.YouTube.urls.YouTubeUrls')),
    path('jet/', include('jet.urls', 'jet'))
]
