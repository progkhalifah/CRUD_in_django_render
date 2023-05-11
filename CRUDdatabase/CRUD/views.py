from django.shortcuts import redirect, render

from .models import Employees


def index(request):
    emp = Employees.objects.all()

    context = {
        'emp': emp,
    }

    return render(request, 'CRUD\post\index.html', context)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('home')
    return render(request, 'CRUD\post\index.html')


def edit(request):
    emp = Employees.objects.all()

    context = {
        'emp': emp,
    }
    return render(request, 'CRUD\post\index.html', context)


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('home')
    return render(request, 'CRUD\post\index.html')


def delete(request, id):
    emp = Employees.objects.filter(id=id)
    emp.delete()
    context ={
        'emp':emp
    }
    return redirect('home')