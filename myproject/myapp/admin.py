"""
@Docs
"""
from django.contrib import admin
from myproject.myapp.features.YouTube.model.YouTubeModel import YoutubeModel

# Register your models here.
# MARK:- Adding YoutubeModel Module To Admin
admin.site.register(YoutubeModel)
# MARK:- style admin
# MARK:- add DashBoard
