"""
@Docs
"""

from django.db import models

from myproject.myapp.base.BaseModel import BaseModelProtocol
from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import (
    AnalyticProtocol,
)


# Description
class DiaryModel(models.Model, AnalyticProtocol , BaseModelProtocol ):
    diary_id = models.BigAutoField(primary_key=True)
    diary_description = models.CharField(max_length=6000)
    diary_date = models.DateTimeField("event Date", auto_now_add=True)
    diary_success_rate = models.FloatField("Success Rate")

    # MARK:- implement Base Analytic
    def calculate_analytic_value(self):
        pass

    def get_hashmap(self):
        result = {
            "id": self.diary_id,
            "description": self.diary_description,
            "add_date": self.diary_date,
            "diary_success_rate": self.diary_success_rate
        }
        return result

        # MARK: insert item

    @staticmethod
    def build_item(dic: dict):
        result = DiaryModel(diary_description=dic["description"], diary_success_rate=dic["diary_success_rate"])
        return result

    @staticmethod
    def insert_item(item):
        item: DiaryModel
        item.save()

