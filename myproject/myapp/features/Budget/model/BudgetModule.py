"""
@Docs
"""

from django.db import models

from myproject.myapp.base.BaseModel import BaseModelProtocol
from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import (
    AnalyticProtocol,
)


# Description
class BudgetModel(models.Model, AnalyticProtocol,BaseModelProtocol):
    budget_id = models.BigAutoField(primary_key=True)
    budget_title = models.CharField("budget title", max_length=6000)
    budge_date = models.DateTimeField("budget Date", auto_now_add=True)
    budget_amount = models.FloatField("budget Amount")

    # MARK:- implement Base Analytic
    def calculate_analytic_value(self):
        pass

        # MARK:- generate object Hashmap

    def get_hashmap(self):
        result = {
            "id": self.budget_id,
            "title": self.budget_title,
            "add_date": self. budge_date ,
            "budget_amount": self.budget_amount
        }
        return result

        # MARK: insert item

    @staticmethod
    def build_item(dic: dict):
        result = BudgetModel(budget_title=dic["title"],  budget_amount=dic["budget_amount"])
        return result

    @staticmethod
    def insert_item(item):
        item: BudgetModel
        item.save()

