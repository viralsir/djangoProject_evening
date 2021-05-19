from django.urls import  path
from . import views
urlpatterns=[
  path("new/",views.CourseEntryView.as_view(),name="course-new"),
  path("view/",views.CourseListView.as_view(),name="course-view"),
  path("update/<int:pk>",views.CourseUpdateView.as_view(),name="course-update"),
  path("detail/<int:pk>",views.CourseDetailView.as_view(),name="course-detail"),
  path("delete/<int:pk>",views.CourseDeleteView.as_view(),name="course-delete")
]