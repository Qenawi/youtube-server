"""
@Docs
-todo add video tags analytics
"""

from django.db import models

# Description
from myproject.myapp.base.BaseModel import BaseModelProtocol


class YoutubeModel(models.Model, BaseModelProtocol):
    youtube_id = models.BigAutoField(primary_key=True)
    youtube_title = models.CharField(max_length=200)
    youtube_date = models.DateTimeField(auto_now=True, help_text="video request date")
    youtube_tags = models.CharField(max_length=200)

    def get_hashmap(self):
        result = {
            "id": self.youtube_id,
            "title": self.youtube_title,
            "request_date": self.youtube_date,
            "tags": self.youtube_tags
        }
        return result

        # MARK: insert item

    @staticmethod
    def build_item(dic: dict):
        result = YoutubeModel(youtube_title=dic["title"], youtube_tags=dic["tags"])
        return result

    @staticmethod
    def insert_item(item):
        item: YoutubeModel
        item.save()
