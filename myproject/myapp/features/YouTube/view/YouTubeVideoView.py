#   Qenawi created AnalyticsView.py at 4/29/21, 10:11 PM
#   AnalyticsView.py @Docs
#
import string

from django.http import HttpRequest

from myproject.myapp.base.BaseView import view_list_all
from myproject.myapp.base.ResponseFormater import clean_response, sucess_response_from_string
from myproject.myapp.features.YouTube.model.YouTubeModel import YoutubeModel as mModel
from pytube import Playlist, YouTube

# add thread handiling
from myproject.myapp.features.YouTube.urls.UrlParams import UrlParams as serverParams
from myproject.myapp.features.YouTube.viewModel.SongViewModel import SongViewViewModel as songViewModel


# get direct mp3 steam link from video url
def _get_mp3_stream(video_url: string) -> string:
    return songViewModel.download_video_as_mp3(video_url)


# get playlist videos urls from playlist url
def _from_response(playlist: Playlist):
    return {"title": playlist.title,
            "description": playlist.description,
            "songs_list": [i.__str__() for i in playlist.video_urls]}


# URL
def fetch_video_steam_from_video_url(my_request: HttpRequest):
    url = my_request.GET[serverParams.playListKey]
    # type = my_request.GET[serverParams.videoStreamTypeKey]
    dic = {"streamUrl": _get_mp3_stream(url)}
    return clean_response(dic, "TBD")


# URL
def fetch_play_list(my_request: HttpRequest):
    url = my_request.GET[serverParams.playListKey]
    print("url -> ", url)
    m_url = url.__str__()
    playlist = Playlist(m_url)
    data = _from_response(playlist)
    return clean_response(data, playlist.description)


# URL
def list_all(my_request: HttpRequest):
    listed = view_list_all(mModel.objects.all())
    return clean_response(listed, "success")


# URL
def insert(my_request: HttpRequest):
    print(my_request)
    book = mModel.build_item(dic={"title": "@TestBook", "todo_success_rate": 800})
    mModel.insert_item(book)
    return sucess_response_from_string("inserted")
