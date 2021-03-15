from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contact


def home (request):
    
    return render(request,'home.html', {'home': 'active'})
def skills(request):
     context = {'skills':'active'}
     return render(request,'skills.html',context)
def contac(request):
    context = {'contact':'active',}
    if request.method =='POST':
        name = request.POST['fname']
        emial = request.POST['fmail']
        subject = request.POST['fsubject']
        textarea = request.POST['mess']
        obj = contact(name=name,emial=emial,subject=subject,textarea=textarea)
        obj.save();
        return redirect('/contact')
    else:
        return render(request, 'contact.html',context)
def service(request):
     context = {'service':'active'}
     return render(request, 'service.html',context)