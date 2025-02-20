from django.shortcuts import render,HttpResponse,redirect
from .forms import std_form
from .models import student1

# Create your views here.
def std(request):
    post2=student1.objects.all()
    post = student1.objects.get(id=1)
    
    if request.method=="POST":
        form=std_form(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(request,'student2.html')
        else:
            form =std_form()
           
    return render(request,'student1.html',{'form':form,'post':post,'post2':post2})
            
    


