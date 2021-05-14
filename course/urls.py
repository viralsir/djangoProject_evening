from django.urls import  path
from . import views
urlpatterns=[
  path("new/",views.CourseEntryView.as_view(),name="course-new"),
  path("view/",views.CourseListView.as_view(),name="course-view")
]