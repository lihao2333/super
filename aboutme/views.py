from django.shortcuts import render

# Create your views here.
def skill(request):
    return render(request, 'skill.html',{} )
def resume(request):
    return render(request, 'resume.html',{} )
