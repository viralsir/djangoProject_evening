from django.shortcuts import render,redirect
from django import forms
# Create your views here.

class NewTaskForm(forms.Form):
    task=forms.CharField(max_length=30,label="New Task :")
    priority=forms.IntegerField(max_value=10,min_value=1)
    status=forms.ChoiceField(choices=[('active','active'),('deactive','deactive')])


def home(request):
    if "task" not in request.session:
        request.session["task"]=[]

    return render(request,"taskapp/list_task.html",{
        "tasks":request.session["task"]
    })

def add_task(request):
    form=NewTaskForm()
    if request.method == 'POST':
        form=NewTaskForm(request.POST)
        if form.is_valid():
             #tasks.append(request.POST["task"]);
             request.session["task"]+=[form.cleaned_data["task"]];
             return redirect('task-home')
        else :
            return render(request, "taskapp/add_task.html", {
                "form": form
            })
    else :
        return render(request,"taskapp/add_task.html",{
            "form":form
        })