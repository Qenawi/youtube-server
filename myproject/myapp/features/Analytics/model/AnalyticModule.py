"""
@Docs
"""

from django.db import models


# Description
from myproject.myapp.base.BaseModel import BaseModelProtocol


class AnalyticModule(models.Model,BaseModelProtocol):
    analytic_id = models.BigAutoField(primary_key=True)
    analytic_title = models.CharField("analytic title", max_length=6000)
    analytic_date = models.DateTimeField("analytic Date", auto_now_add=True)
    analytic_amount = models.FloatField("analytic Amount")

    # MARK:- generate object Hashmap
    def get_hashmap(self):
        result = {
            "id": self.analytic_id,
            "title": self.analytic_title,
            "add_date": self.analytic_date,
            "analytic_amount": self.analytic_amount
        }
        return result

    # MARK: insert item
    @staticmethod
    def build_item(dic: dict):
        result = AnalyticModule(analytic_title=dic["title"], analytic_amount=dic["analytic_amount"])
        return result

    @staticmethod
    def insert_item(item):
        item: AnalyticModule
        item.save()
