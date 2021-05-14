from django.urls import  path
from . import views
urlpatterns=[
  path("new/",views.course_entry,name="course-new"),
  path("view/",views.course_view,name="course-view")
]