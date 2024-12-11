from django.shortcuts import redirect, render
from tdapp.forms import TodoForm
from tdapp.models import Todo
# Create your views here.
def homepage(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("task added successfully!!")
    task_list=Todo.objects.all()
    form=TodoForm()
    return render(request,'home.html',{'form':form,'task_list':task_list})

#def todoview(request):
    #task_list=Todo.objects.all()
   # return render(request,'view.html',{'task_list':task_list})
   # return redirect('/')

def delete_view(request,id):
    task_list=Todo.objects.get(id=id)
    task_list.delete()
    return redirect('/')


def update_view(request,id):
    task_list=Todo.objects.get(id=id)
    form=TodoForm(instance=task_list)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=task_list)
        form.save()
        return redirect('/')
    return render(request,'home.html',{'form':form})
   

   