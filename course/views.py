from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from .models import course_master
from .form import CourseEntryForm

class CourseEntryView(CreateView):
    model = course_master
    fields = '__all__'
    template_name = 'course/course_register.html'
#course_master_form.html

class CourseListView(LoginRequiredMixin,ListView):
    model = course_master
    template_name = 'course/course_view.html'
    context_object_name = 'courses'
    ordering = ['-name']

class CourseUpdateView(UpdateView):
    model = course_master
    fields = '__all__'
    template_name = 'course/course_register.html'

class CourseDetailView(DetailView):
    model = course_master
#course_master_detail.html

class CourseDeleteView(DeleteView):
    model = course_master
    success_url = '/course/view'

#course_master_confirm_delete.html



#course_master_list.html
# Create your views here.

# def course_entry(request):
#     cform=CourseEntryForm()
#     if request.method == 'POST':
#         cform=CourseEntryForm(request.POST)
#         if cform.is_valid():
#             newcourse=course_master()
#             newcourse.name=cform.cleaned_data["name"]
#             newcourse.fees=cform.cleaned_data["fees"]
#             newcourse.duration=cform.cleaned_data['duration']
#             newcourse.description=cform.cleaned_data['description']
#             newcourse.save()
#             return redirect('course-view')
#
#         else:
#             return render(request, "course/course_register.html", {
#                 "form": cform
#             })
#
#     return render(request,"course/course_register.html",{
#         "form":cform
#     })
#
# def course_view(request):
#     return render(request,"course/course_view.html",{
#         "courses":course_master.objects.all()
#     })