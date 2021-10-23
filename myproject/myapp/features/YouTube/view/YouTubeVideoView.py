#   Qenawi created AnalyticsView.py at 4/29/21, 10:11 PM
#   AnalyticsView.py @Docs
#
from django.http import HttpRequest

from myproject.myapp.base.BaseView import view_list_all
from myproject.myapp.base.ResponseFormater import clean_response, sucess_response_from_string
from myproject.myapp.features.YouTube.model.YouTubeModel import YoutubeModel as mModel
from pytube import Playlist, YouTube


def _from_response(playlist: Playlist):
    return {"title": playlist.title,
            "description": playlist.description,
            "songs_list": [i.__str__() for i in playlist.video_urls]}


def fetch_play_list(my_request: HttpRequest):
    mUrl = "https://www.youtube.com/watch?v=kTJczUoc26U&list=PLDIoUOhQQPlXr63I_vwF9GD8sAKh77dWU"
    playlist = Playlist(mUrl)
    data = _from_response(playlist)
    return clean_response(data, playlist.description)


def list_all(my_request: HttpRequest):
    print(my_request)
    listed = view_list_all(mModel.objects.all())
    return clean_response(listed, "success")


def insert(my_request: HttpRequest):
    print(my_request)
    book = mModel.build_item(dic={"title": "@TestBook", "todo_success_rate": 800})
    mModel.insert_item(book)
    return sucess_response_from_string("inserted")
