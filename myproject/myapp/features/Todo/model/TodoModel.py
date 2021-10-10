"""
@Docs
"""

from django.db import models


# Description
from myproject.myapp.base.BaseModel import BaseModelProtocol
from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import AnalyticProtocol


class TodoTask(models.Model , AnalyticProtocol , BaseModelProtocol ):
    todo_id = models.BigAutoField(primary_key=True)
    todo_title = models.CharField(max_length=200)
    todo_start_date = models.DateTimeField("Task Start Date")
    todo_end_date = models.DateTimeField("Task End Date")
    todo_status_is_finished = models.BooleanField("Is Finished")
    todo_status_is_archived = models.BooleanField("Is Archived")
    todo_status_success_rate = models.FloatField("Success Rate")

    def get_hashmap(self):
        result = {
            "id": self.todo_id,
            "title": self.todo_title,
            "add_date": self.todo_start_date,
            "todo_success_rate": self.todo_status_success_rate
        }
        return result

        # MARK: insert item

    @staticmethod
    def build_item(dic: dict):
        result = TodoTask(todo_title=dic["title"], todo_success_rate=dic["todo_success_rate"])
        return result

    @staticmethod
    def insert_item(item):
        item: TodoTask
        item.save()

