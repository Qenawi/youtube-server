"""
@Docs
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path("", TemplateView.as_view(template_name="myapp/home.html"), name="home"),
    path("admin/", admin.site.urls),
    path("", include('myproject.myapp.features.Books.urls.BookUrls')),
    path("", include('myproject.myapp.features.Analytics.urls.AnalyticUrls')),
    path("", include('myproject.myapp.features.Budget.urls.BudgetUrls')),
    path("", include('myproject.myapp.features.Diary.urls.DiaryUrls')),
    path("", include('myproject.myapp.features.LifeEvents.urls.LifeEventUrls')),
    path("", include('myproject.myapp.features.Todo.urls.TodoUrls')),
    path('jet/', include('jet.urls', 'jet'))
]
