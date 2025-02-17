from django.shortcuts import render,redirect
from .models import list
from .forms import TaskForm
def task_list(request):
    # task=''
    tasks=list.objects.all()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        # tasks={
        #     'title':title1,

        # }
        return redirect('task_list')
    # else:
        # form=TaskForm()
        

    return render(request,'task.html',{'tasks':tasks})

