"""
@Docs
"""
from django.db import models

from myproject.myapp.base.BaseModel import BaseModelProtocol


def view_list_all(model: list):
    result = []
    for item in model:
        item: BaseModelProtocol
        result.append(item.get_hashmap())
    return result
