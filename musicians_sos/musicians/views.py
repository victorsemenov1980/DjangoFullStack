from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Main, Service,Services,FAQ,Info
import random


# Create your views here.
def index(request):
    inform=Info.objects.all()
    starter=[]
    for k in inform:
        starter.append(k.Message)
    random.shuffle(starter)
    info=starter[0]
    all_musicians=Main.objects.all()
    data=[]
    for i in all_musicians:
        data.append((i))
    random.shuffle(data)
    out=data[:6]
        
    return render(request,'index.html',{'data':out,'info':info})

def success(request):
    username=request.user
    personal_page=Main.objects.get(user=username)
    personal_services=Service.objects.filter(user=username)
    content={
        'personal_page':personal_page,
        'services':personal_services
        
        }
    
    return render(request,'success.html',content)

def signup(request):
    if request.method=='POST': #user wants to register
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return render(request,'success.html')
        else:
            return render(request,'signup.html',{'error':'Passwords must match!'})
            
    else:#if get
        
        return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        user= auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            # return redirect ('success')
            return render(request,'success.html')
        else:
            return render(request,'login.html',{'error':'Username or password is not correct'})
            
    else:
        return render(request,'login.html')
    
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect ('index')


def nursing(request):
    obj=Services.objects.filter(Category='Home/Dog/Baby sitting')[0]
    all_=Service.objects.all().filter(Category=obj)
    all_musicians=Main.objects.all()
    data=[]
    for i in all_:
        user=i.user
        m=all_musicians.get(user=user)
        data.append((m,i))
        
    return render(request,'nursing.html',{'data':data})
    

def professional(request):
    obj=Services.objects.all().filter(Category='Professional service')
    all_musicians=Main.objects.all()
    data=[]
    for j in obj:
        all_=Service.objects.all().filter(Category=j)
    
        
        for i in all_:
            user=i.user
            m=all_musicians.get(user=user)
            data.append((m,i))
        
    return render(request,'professional.html',{'data':data})
   

def home(request):
    obj=Services.objects.filter(Category='Home remodelling')[0]
    all_=Service.objects.all().filter(Category=obj)
    all_musicians=Main.objects.all()
    data=[]
    for i in all_:
        user=i.user
        m=all_musicians.get(user=user)
        data.append((m,i))
        
    return render(request,'home.html',{'data':data})
    

def wedding(request):
    obj=Services.objects.filter(Category='Weddings and Live Gigs')[0]
    all_=Service.objects.all().filter(Category=obj)
    all_musicians=Main.objects.all()
    data=[]
    for i in all_:
        user=i.user
        m=all_musicians.get(user=user)
        data.append((m,i))
        
    return render(request,'wedding.html',{'data':data})
    


def recording(request):
    obj=Services.objects.filter(Category='Remote recording')[0]
    all_recordings=Service.objects.all().filter(Category=obj)
    all_musicians=Main.objects.all()
    data=[]
    for i in all_recordings:
        user=i.user
        m=all_musicians.get(user=user)
        data.append((m,i))
        
    return render(request,'recording.html',{'data':data})


def lessons(request):
    obj=Services.objects.filter(Category='Music Lessons')[0]
    all_=Service.objects.all().filter(Category=obj)
    all_musicians=Main.objects.all()
    data=[]
    for i in all_:
        user=i.user
        m=all_musicians.get(user=user)
        data.append((m,i))
        
    return render(request,'lessons.html',{'data':data})

def manage_account(request):
    username=request.user
    try:
        Main.objects.get(user=username)
        return render(request,'manage_account.html',{'error':'Your main info is already entered into database','already':True})
    except:   
        return render(request,'manage_account.html')
def faq(request):
    faqs=FAQ.objects.all()
    return render(request,'faq.html',{'faqs':faqs})


def account(request,account_id):
    account=get_object_or_404(Main,pk=account_id)
    username=account.user
    personal_services=Service.objects.filter(user=username)
    return render(request,'account.html',{'account':account,'services':personal_services})

@login_required(login_url='login')
def manage(request):
    if request.method=='POST':
        if request.POST['name'] and request.POST['email'] and request.POST['phone'] and request.POST['cover'] and request.POST['bio'] and request.POST['instrument'] and request.POST['organization'] and request.FILES['photo']:
            basic=Main()
            basic.Name=request.POST['name']
            basic.Email=request.POST['email']
            basic.Phone=request.POST['phone']
            basic.CoverLetter=request.POST['cover']
            basic.Bio=request.POST['bio']
            basic.Instrument=request.POST['instrument']
            basic.Organization=request.POST['organization']
            basic.Photo=request.FILES['photo']
            basic.user=request.user
            basic.save()
            return redirect ('success')
        else: 
            return render(request,'main_info.html',{'error':'All fields are required'})
    else:
         return render(request,'main_info.html')

@login_required(login_url='login')
def add_service(request):
    username=request.user
    cats=Services.objects.all()
    all_services=Service.objects.filter(user=username).count()
    if all_services<3:
        
        if request.method=='POST':
            if request.POST['sub_cat'] and request.POST['description']:
                service=Service()
                service.Sub_Category=request.POST['sub_cat']
                service.Description=request.POST['description']
                service.user=request.user
                service.Category=cats.filter(Sub_Category=request.POST['sub_cat'])[0]
                service.save()
                return redirect ('success')
            else: 
                return render(request,'add_service.html',{'error':'All fields are required'})
        
        else:
             return render(request,'add_service.html',{'categories':cats,'all_services':all_services})
    else:
             return render(request,'add_service.html',{'categories':cats,'all_services':all_services,'error':'You cannot enter more services'})









