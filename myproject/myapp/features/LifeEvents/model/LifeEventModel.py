"""
@Docs
"""

from django.db import models

from myproject.myapp.base.BaseModel import BaseModelProtocol
from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import (
    AnalyticProtocol,
)


# Description
class LifeEvent(models.Model, AnalyticProtocol , BaseModelProtocol ):
    life_event_id = models.BigAutoField(primary_key=True)
    life_event_title = models.CharField(max_length=600)
    life_event_date = models.DateTimeField("event Date")
    life_event_success_rate = models.FloatField("Success Rate")

    # MARK:- implement Base Analytic
    def calculate_analytic_value(self):
        pass

    def get_hashmap(self):
        result = {
            "id": self.life_event_id,
            "title": self.life_event_title,
            "event_date": self.life_event_date,
            "event_success_rate": self.life_event_success_rate
        }
        return result

        # MARK: insert item

    @staticmethod
    def build_item(dic: dict):
        result = LifeEvent(diary_description=dic["title"], diary_success_rate=dic["event_success_rate"])
        return result

    @staticmethod
    def insert_item(item):
        item: LifeEvent
        item.save()


