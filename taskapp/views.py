from django.shortcuts import render,redirect
from django import forms
# Create your views here.
tasks=[
    "check balance",
    "do recharge",
    "book ticket",
    "register user",
    "do homework"
]
class NewTaskForm(forms.Form):
    task=forms.CharField(max_length=30,label="New Task :")
    priority=forms.IntegerField(max_value=10,min_value=1)


def home(request):
    return render(request,"taskapp/list_task.html",{
        "tasks":tasks
    })

def add_task(request):
    form=NewTaskForm()
    if request.method == 'POST':
        form=NewTaskForm(request.POST)
        if form.is_valid():
             tasks.append(form.cleaned_data["task"]);
             return redirect('task-home')
        else :
            return render(request, "taskapp/add_task.html", {
                "form": form
            })
    return render(request,"taskapp/add_task.html",{
        "form":form
    })