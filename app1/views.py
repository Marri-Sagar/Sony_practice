from django.shortcuts import render



def hello(request):
    return render(request,'hello.html',{"hai":"hai sagar-Sonyproject"})


