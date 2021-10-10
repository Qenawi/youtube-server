#   Qenawi created AnalyticsView.py at 4/29/21, 10:11 PM
#   AnalyticsView.py @Docs
#
from django.http import HttpRequest

from myproject.myapp.base.BaseView import view_list_all
from myproject.myapp.base.ResponseFormater import clean_response, sucess_response_from_string
from myproject.myapp.features.LifeEvents.model.LifeEventModel import LifeEvent as mModel


def list_all(my_request: HttpRequest):
    print(my_request)
    listed = view_list_all(mModel.objects.all())
    return clean_response(listed, "success")


def insert(my_request: HttpRequest):
    print(my_request)
    book = mModel.build_item(dic={"title": "@TestBook", "event_success_rate": 100})
    mModel.insert_item(book)
    return sucess_response_from_string("inserted")


