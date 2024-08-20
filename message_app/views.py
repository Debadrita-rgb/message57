from django.shortcuts import render,HttpResponse,redirect
from message_app.models import Msg

# Create your views here.
def demo(request):
    return HttpResponse("Hello !! Working Properly")

def create(request):
    #print("Request is:",request.method)
    if request.method== 'POST':
        #fetch values from the form
        uname=request.POST['uname']
        umail=request.POST['uemail']
        mob=request.POST['umob']
        msg=request.POST['msg']
        
        """ print("Name",uname)
        print('Email',umail)
        print("Mobile",mob)
        print("Message",msg) """
        m=Msg.objects.create(name=uname,email=umail,mobile=mob,msg=msg)
        m.save()
        return redirect('/')
        #return HttpResponse("Data Fetched Successfully")
    else:
        return render(request,'create.html')

def dashboard(request):    
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
    #return HttpResponse("Data Fetched from database")

def delete(request,rid):
    #print("Id to be deleted"+rid)
    d=Msg.objects.filter(id=rid)
    d.delete()
    return redirect('/')
    #return HttpResponse("Id to be deleted"+rid)

def edit(request,rid):
    if request.method=='POST':
        #update data
        uname=request.POST['uname']
        umail=request.POST['uemail']
        mob=request.POST['umob']
        msg=request.POST['msg']
        
        u=Msg.objects.filter(id=rid)
        u.update(name=uname,email=umail,mobile=mob,msg=msg)
        return redirect('/')
        
    else:
        #display from with the previous fields
        #e=Msg.objects.filter(id=rid)
        e=Msg.objects.get(id=rid)
        print(e)
        context={}
        context['data']=e
        return render(request,'edit.html',context)

    
    #return HttpResponse("Id to be edited"+rid)