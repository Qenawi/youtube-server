#   Qenawi created SongViewModel.py at 1/15/22, 5:09 PM
#   SongViewModel.py @Docs
#
import string

from pytube import YouTube


class SongViewViewModel:
    @staticmethod
    def download_video_as_mp3(song_path: string):
        yt = YouTube(song_path)
        t = yt.streams.filter(only_audio=True)
        streamUrl = t.first().url
        return streamUrl
