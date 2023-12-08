from django.shortcuts import render, get_object_or_404, redirect
from .models import Tasks,Tests, Answers, Result
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ResultForm
import datetime


def result(request, pk):

    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваши данные сохранены!')
            return redirect('home')
        else:
            messages.success(request, f'Ваши данные НЕсохранены!')
            context = {
                'tests': Tests.objects.all(),
                'pk': pk,
                'form': form
            }
    else:
        res = Result.objects.get(pk=pk)
        form = ResultForm(instance = res)
#        form.fields['test'].queryset = Tests.objects.filter(id=res.test_id)
#        form.instance = res

        context = {
            'tests': Tests.objects.all(),
            'pk' : pk,
            'form': form,

            'test': res.test
        }
    return render(request, 'blog/result.html', context)

@login_required
def tester(request, id = -1, id_task = -1, pk = -1):

    test = Tests.objects.get(id=id)
    id_tasks = []
    if id_task == -1 :
        id_task = test.get_tasks_order()[0]
        id_tasks = list(test.get_tasks_order())
        id_tasks.reverse()
        id_tasks = id_tasks[:-1]
        res = Result()
        res.user = request.user
        res.test = test
        res.date = datetime.datetime.now()
        res.tr = 0
        res.fs = 0
        res.id_tasks = ''.join(map(str,id_tasks))
        res.save()

    if request.method == 'POST':
        res = Result.objects.get(pk=pk)
        if 'choice_answer' in request.POST:
            pp = request.POST['choice_answer']
            a = get_object_or_404(Answers, pk=request.POST['choice_answer'])
            if a.true :
                res.tr +=1
            else:
                res.fs +=1
            res.save()
        else:
            res.fs +=1
            res.save()

    if id_task == 0 : return  redirect('/result/'+str(pk))
    tests = Tests.objects.all()
    task = Tasks.objects.get(id=id_task)

    try:
        id_tasks = list(map(int,list(res.id_tasks)))
        task_next = id_tasks.pop()
        res.id_tasks = ''.join(map(str,list(id_tasks)))
        res.save()
    except:
        task_next = 0
        redirect('/result/'+str(pk))

    answers = Answers.objects.filter(task=task.id)

    context = {
        'title': 'Тесты',
        'test': test,
        'tests': tests,
        'task': task,
        'task_next': task_next,
        'id_task': id_task,
        'answers': answers,
#        'tr' : tr,
#        'fs': fs,
        'res': res,
        'post': request.POST
    }

    return render(request, 'blog/tester.html', context)

@login_required
def home(request):


    if request.method == 'POST':
        tests = Tests.objects.all()
        context = {
            'title': 'Тесты',
            'tests': tests,
        }
    else:
        context = {
            'title': 'Тесты',
            'tests': Tests.objects.all(),
        }
    return render(request, 'blog/home.html', context)


def about(request):

    context = {
        'title': 'обо мне!'
    }
    return render(request, 'blog/about.html', context)