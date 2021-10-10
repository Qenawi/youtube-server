#   Qenawi created AnalyticUrls.py at 4/29/21, 10:14 PM
#   AnalyticUrls.py @Docs
#
from django.urls import path
from myproject.myapp.features.Books.view import BookView
from myproject.myapp.features.Todo.view.TodoView import list_all,insert
from myproject.myproject.settings.base import MEDIA_URL, MEDIA_ROOT, STATIC_URL, DEBUG
from django.conf.urls.static import static

# view variables
_pathBase = "crud"
_ListAll = "todo"
_AddItem = "add_todo"
_DeleteItem = "delete_todo"

# Feature Urls
urlpatterns = [
    path(_pathBase+'/'+_ListAll, list_all, name='index'),
    path(_pathBase + '/' + _AddItem, insert, name='add_book')

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
