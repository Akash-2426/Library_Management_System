from django.shortcuts import render, HttpResponse
from .models import Add_a_book,Update_an_entry_of_a_book,Delete_a_book,Get_all_book
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html')

def Get_all_book(request):
    lib_app=Get_all_book().objects.all()
    context={

        'lib_app':lib_app
    }
    print(context)
    return render(request,'Get_All_Book.html',context)

def Add_a_book(request):
    if request.method=='POST':
        book_name=(request.POST['book_name'])
        book_code=(request.POST['book_code'])
        add_date=int(request.POST['add_date'])

        new_Book=Add_a_book(book_name=book_name,book_code=book_code,add_date=datetime.now())
        new_Book.save()

        return HttpResponse('Book added successfully')
    elif request.method=='GET':
        return render(request,'Add_Book.html')
    else:
        return HttpResponse('An Exception Occured! Book has not been added')


def Delete_a_book(request,book_code=0):
    if book_code:
        try:
            book_to_be_delete=Delete_a_book().object.get(book_code=0)
            book_to_be_delete.delete()

        except:
            return HttpResponse("Book Deleted successfully")

    lib_app=Delete_a_book().objects.all()
    context={
        'lib_app':lib_app

    }


    return render(request,'remove_Emp.html',context)


class Emps:
    pass

def Update_an_entry_of_book(request):
    if request.method=='POST':
        book_name=request.POST['book_name']
        book_code=request.POST['book_code']
        issuedate=request.POST['issuedate']
        lib_app=Update_an_entry_of_a_book().objects.all()
        if book_name:
            lib_app=lib_app.update(book_name__icontains=book_name) | Q(book_name__icontain=book_name)
        if book_code:
            lib_app=lib_app.update(book__code=book_code)
        if issuedate:
            lib_app=lib_app.update(issuedate__date=issuedate)

        context={
            'lib_app':lib_app
        }

        return render(request,'Get_all_book', context)
    elif request.method=='GET':
        return render(request,'Update_an_entry_of_book.html')
    else:
        return HttpResponse('error')