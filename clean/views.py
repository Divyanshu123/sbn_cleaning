from django.shortcuts import render,redirect,get_object_or_404
from .forms import DevoteeRegForm1,DevoteeRegForm2, DevLoginForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Service,Devotee  

# Create your views here.

def index(request):
    return render(request, "clean/index.html")


def after_login(request,pk):
    user = get_object_or_404(User,pk=pk)
    return render(request, 'clean/after_login.html', {'user':user})


def dev_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('clean:after_login', pk = user.pk)

            else:
                return HttpResponse('user is not active!')

        else:
            return HttpResponse('invalid User Credentials!')

    form = DevLoginForm()
    return render(request,'clean/login_page.html',{'form':form})

def all_avail_services(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    services = Service.objects.filter(taken=False)
    return render(request,'clean/all_avail_services.html', {'user':user,'services':services})

def dev_add_service(request,user_pk, service_pk):
    user = get_object_or_404(User,pk=user_pk)
    service = get_object_or_404(Service,pk = service_pk)
    service.taken=True
    service.save() 
    user.devotee.services.add(service)
     
    return redirect('clean:all_avail_services',user_pk=user_pk)

def dev_services(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    services = user.devotee.services.all()
    return render(request,'clean/dev_services.html',{'user':user, 'services':services}) 

def dev_service_mark_as_done(request,user_pk,service_pk):
    user = get_object_or_404(User,pk=user_pk)
    dev = user.devotee  
    service = get_object_or_404(Service, pk = service_pk)
    service.done = True  
    dev.total_score += service.point  
    dev.score_of_week += service.point  
     
    dev.save()
    service.save()  
    return redirect('clean:dev_services', user_pk=user_pk)




def dev_points(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    return render(request,'clean/dev_points.html', {'dev':user.devotee})

def dev_register(request):
    if request.method == 'POST':
        form1 = DevoteeRegForm1(request.POST)
        form2 = DevoteeRegForm2(request.POST)

        if form1.is_valid() and form2.is_valid():
            f1 = form1.save(commit=False)
            f1.password = make_password(form1.cleaned_data['password'])
            f1.save()

            dev = Devotee.objects.create(info=f1,phone_number=form2.cleaned_data['phone_number'])
            return redirect('clean:index')

        else:
            return HttpResponse('Invalid Credentials!')

    
    form1 = DevoteeRegForm1()
    form2 = DevoteeRegForm2()
    return render(request,'clean/register_page.html',{'form1':form1,'form2':form2})


@login_required
def dev_logout(request):
    logout(request)
    return redirect('clean:index')