from django.urls import  path
from . import  views
urlpatterns=[
    path("view/",views.home,name="task-home"),
    path("new/",views.add_task,name="add-task")
]