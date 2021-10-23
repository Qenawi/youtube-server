#   Qenawi created AnalyticUrls.py at 4/29/21, 10:14 PM
#   AnalyticUrls.py @Docs
#
from django.urls import path
from myproject.myapp.features.YouTube.view.YouTubeVideoView import list_all, insert , fetch_play_list
from myproject.myproject.settings.base import MEDIA_URL, MEDIA_ROOT, STATIC_URL, DEBUG
from django.conf.urls.static import static

# view variables
_pathBase = "crud"
_ListAll = "youtube_video"
_AddItem = "add_youtube_video"
_DeleteItem = "delete_youtube_video"
_fetch_play_list = "fetch_play_list"

# Feature Urls
urlpatterns = [
    path(_pathBase + '/' + _ListAll, list_all, name='index'),
    path(_pathBase + '/' + _AddItem, insert, name='add_youtube_video'),
    path(_pathBase + '/' + _fetch_play_list, fetch_play_list, name='add_youtube_video')

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
