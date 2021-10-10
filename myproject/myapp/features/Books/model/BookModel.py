"""
@Docs
"""

import abc

from django.db import models

from myproject.myapp.base.BaseModel import BaseModelProtocol
from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import (
    AnalyticProtocol,
)


class BookModel(models.Model, AnalyticProtocol, BaseModelProtocol):
    book_id = models.BigAutoField(primary_key=True)
    book_title = models.CharField(max_length=6000)
    book_start_date = models.DateTimeField("book start reading Date", auto_now_add=True)
    book_end_date = models.DateTimeField("book end reading Date", auto_now_add=True)
    current_page = models.IntegerField("current page")
    page_count = models.IntegerField("current page")

    # MARK:- implement Base Analytic
    def calculate_analytic_value(self):
        pass

    # MARK:- generate object Hashmap
    def get_hashmap(self):
        result = {
            "id": self.book_id,
            "title": self.book_title,
            "add_date": self.book_start_date,
            "current_page": self.current_page,
            "page_count": self.page_count
        }
        return result

    # MARK: insert item
    @staticmethod
    def build_item(dic: dict):
        result = BookModel(book_title=dic["title"], current_page=dic["current_page"], page_count=dic["page_count"])
        return result

    @staticmethod
    def insert_item(item):
        item: BookModel
        item.save()
