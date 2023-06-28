from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from home.models import userInfo
from django.db.models import Sum
# Create your views here.

def home(request):
    global loginuser
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        loginuser=user
        if user is not None:
            if user.is_staff:
                auth_login(request, user)
                messages.success(request,"admin login successfully")
                print("superuser login successfully")
                return redirect('/adminpage')
            else:
                print("login successfully")
                messages.success(request,"login successfully")
                return redirect('/userinfo') 
        elif user is None:
            print("user is not login")
            messages.error(request,'Please check password or username')
            return redirect('/')
    return render(request, 'home.html')

def singup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.warning(request,"username is already taken")
            return redirect('/singup')
         
        user=User.objects.create(username=username,password=make_password(password))
        print(username)
        print(password)
        user.save()
        print("user register succesfully")
        messages.success(request,"user register successfully")
        return redirect('/')
    return render(request,'singup.html')

def adminpage(request):
    user1=User.objects.filter(username="coustomer1")
    user2=User.objects.filter(username="coustomer2")
    user1datas=userInfo.objects.filter(user=user1[0].id)
    user2datas=userInfo.objects.filter(user=user2[0].id)
    print(user1datas)
    print(user2datas)
    user1Q=0
    user1W=0
    user1B=0
    for user1data in user1datas:
        user1Q+=user1data.quantity
        user1W+=user1data.weight
        user1B+=user1data.box_count
    print(user1Q,user1B,user1W)
    user2Q=0
    user2W=0
    user2B=0
    for user2data in user2datas:
        user2Q+=user2data.quantity
        user2W+=user2data.weight
        user2B+=user2data.box_count
    print(user2Q,user2B,user2W)
    userTQ=user1Q+user2Q
    userTW=user1W+user2W
    userTB=user1B+user2B
    return render (request,'adminpage.html',{'user1Qs':user1Q,'user1Ws':user1W,'user1Bs':user1B,'user2Qs':user2Q,'user2Ws':user2W,'user2Bs':user2B,'userTQ':userTQ,'userTW':userTW,'userTB':userTB})

def userinfo(request):
    global loginuser
    if request.method=="POST":
        date=request.POST['date']
        company_name=request.POST['company-name']
        owner=request.POST['owner']
        item=request.POST['Item']
        quantity=request.POST['quantity']
        weight=request.POST['weight']
        req_of_shipment=request.POST['req-of-shipment']
        tracking_id=request.POST['tracking-id']
        shipment_size=request.POST['shipment-size']
        box_count=request.POST['box-count']
        specifiaction=request.POST['specifiaction']
        checklist_quantity=request.POST['checklist-quantity']
        user=loginuser
        print(user)
        saverecord=userInfo(user=user,order_date=date,company_name=company_name,owner=owner,
                          item=item,quantity=quantity,weight=weight,req_of_shpment=req_of_shipment,
                           tracking_id=tracking_id ,shipment_size=shipment_size,box_count=box_count
                             ,specification=specifiaction,checklist_quantity=checklist_quantity )
        saverecord.save()
        messages.success(request,"data saved successfully")
    return render (request,'userInfo.html')

def handlelogout(request):
    logout(request) 
    messages.success(request,"logout successfully")
    return redirect('/')   