from django import forms


class CourseEntryForm(forms.Form):
    name=forms.CharField(max_length=30)
    description=forms.CharField(max_length=50)
    fees=forms.IntegerField()
    duration=forms.IntegerField()

