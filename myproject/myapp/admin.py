"""
@Docs
"""
from django.contrib import admin
from myproject.myapp.features.Todo.model.TodoModel import TodoTask
from myproject.myapp.features.Diary.model.DiaryModel import DiaryModel
from myproject.myapp.features.LifeEvents.model.LifeEventModel import LifeEvent
from myproject.myapp.features.Books.model.BookModel import BookModel
from myproject.myapp.features.Budget.model.BudgetModule import BudgetModel
from myproject.myapp.features.Analytics.model.AnalyticModule import AnalyticModule


# Register your models here.
# MARK:- Adding Todo Module To Admin
admin.site.register(TodoTask)
# MARK:- Adding Todo DiaryModel To Admin
admin.site.register(DiaryModel)
# MARK:- Adding Todo BookModel To Admin
admin.site.register(BookModel)
# MARK:- Adding Todo LifeEvent To Admin
admin.site.register(LifeEvent)
# MARK:- Adding Todo BudgetModel To Admin
admin.site.register(BudgetModel)
# MARK:- Adding Todo AnalyticModule To Admin
admin.site.register(AnalyticModule)
# MARK:- style admin
# MARK:- add DashBoard
