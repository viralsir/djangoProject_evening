from django.shortcuts import render,redirect
from .models import course_master
from .form import CourseEntryForm

# Create your views here.
def course_entry(request):
    cform=CourseEntryForm()
    if request.method == 'POST':
        cform=CourseEntryForm(request.POST)
        if cform.is_valid():
            newcourse=course_master()
            newcourse.name=cform.cleaned_data["name"]
            newcourse.fees=cform.cleaned_data["fees"]
            newcourse.duration=cform.cleaned_data['duration']
            newcourse.description=cform.cleaned_data['description']
            newcourse.save()
            return redirect('course-view')

        else:
            return render(request, "course/course_register.html", {
                "form": cform
            })

    return render(request,"course/course_register.html",{
        "form":cform
    })

def course_view(request):
    return render(request,"course/course_view.html",{
        "courses":course_master.objects.all()
    })