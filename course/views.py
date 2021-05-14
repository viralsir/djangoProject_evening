from django.shortcuts import render,redirect
from .models import course_master

# Create your views here.
def course_entry(request):
    if request.method == 'POST':
        newcourse=course_master()
        newcourse.name=request.POST["cname"]
        newcourse.fees=request.POST["fees"]
        newcourse.duration=request.POST['durations']
        newcourse.description=request.POST['description']
        newcourse.save()
        return redirect('course-view')

    return render(request,"course/course_register.html")

def course_view(request):
    return render(request,"course/course_view.html",{
        "courses":course_master.objects.all()
    })