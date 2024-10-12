
from django.shortcuts import render, HttpResponse
from cv.models import Contact

def home(request):
    context = {'name': 'Arunkumar', 'course': 'django'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse("This is my about page (/)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("This is my project page (/)")
    return render(request, 'project.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data has been print to the db")
        # return HttpResponse("This is my contact page (/contact)")
    return render(request, 'contact.html')


    # return HttpResponse("This is my contact page (/)")

