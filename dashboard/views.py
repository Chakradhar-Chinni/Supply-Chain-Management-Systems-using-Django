from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import SupplierRegistrationForm,AdminRegistrationForm,UserRegistrationForm,OrderForm,tudForm,tmdForm
from .models import UserOrder,SupplierRegistration,AdminRegistration,UserRegistration,tud,tmd

##from .models import SupplierRegistration,AdminRegistration,UserRegistration,UserOrder

from django.db.models import Q
# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def adminlogin(request):
    return render(request,'adminlogin.html')
#def adminregistration(request):
 #   return render(request,'adminregistration.html')
    
def supplierlogin(request):
    return render(request,'supplierlogin.html')
#def supplierregistration(request):
 #   return render(request,'supplierregistration.html')

def userlogin(request):
    return render(request,'userlogin.html')

def userregistration(request):
     if request.method=='POST':
        form = UserRegistrationForm(request.POST) 
        if form.is_valid(): 
            form.save()
            return render(request,'userregisucc.html')
     else:
        form = UserRegistrationForm()
        return render(request,'userregistration.html',{'form':form})

def supplierregistration(request):
     if request.method=='POST':
        form = SupplierRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("Data is added")
            return render(request,'suppregsucc.html')

     else:
        form = SupplierRegistrationForm()
        return render(request,'supplierregistration.html',{'form':form})

def adminregistration(request):
     if request.method=='POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data is added")
     else:
        form = AdminRegistrationForm()
        return render(request,'adminregistration.html',{'form':form})


def checkuser(request):
    if request.method=="POST":
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        #id = request.POST['uid']
        flag = UserRegistration.objects.filter(Q(UserName__exact=uname) & Q(Password__exact=upwd))
        if flag:
            #p.filter(children__status='whatever').values('children__name')
            ##id = UserRegistration.objects.filter(UserName__exact=uname).values_list('id',flat=True).first()
            #id = num
            uid = UserRegistration.objects.filter(UserName=uname).values_list('id', flat=True)[0]
            print(id)
            request.session['uname'] = uname
            request.session['uid'] = uid
            return render(request,'userhome.html',{'uname':uname,'uid':uid})
        else:
            return HttpResponse("Login Invalid")
    else:       
        return render(request,'userlogin.html')
    return render(request,'userlogin.html')

def checksupplier(request):
    if request.method=="POST":
        sname = request.POST['sname']
        spwd = request.POST['spwd']
        flag = SupplierRegistration.objects.filter(Q(UserName__exact=sname) & Q(Password__exact=spwd))
        if flag:
            request.session['sname'] = sname
            sid = SupplierRegistration.objects.filter(UserName=sname).values_list('id', flat=True)[0]
            request.session['sid'] = sid
            return render(request,'supplierhome.html',{'uname':sname,'sid':sid})
        else:
            return HttpResponse("Login Invalid")
    else:       
        return render(request,'supplierlogin.html')
    return render(request,'supplierlogin.html')    

def checkadmin(request):
    if request.method=="POST":
        aname = request.POST['aname']
        apwd = request.POST['apwd']
        flag = AdminRegistration.objects.filter(Q(UserName__exact=aname) & Q(Password__exact=apwd))
        if flag:
            request.session['aname'] = aname
            return render(request,'adminhome.html',{'aname':aname})
        else:
            return HttpResponse("Login Invalid")
    else:       
        return render(request,'adminlogin.html')
    return render(request,'adminlogin.html')   

def viewusers(request):
    users = UserRegistration.objects.all()
    count = UserRegistration.objects.all().count()
    return render(request,'viewusers.html',{'users':users,'count':count})

def viewsuppliers(request):
    users = SupplierRegistration.objects.all()
    count = SupplierRegistration.objects.all().count()
    return render(request,'viewsuppliers.html',{'users':users,'count':count})

def adminhome(request):
    aname = request.session['aname']
    return render(request,'adminhome.html',{'aname':aname})

def order(request):
    uid = request.session['uid']
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            UserOrder.objects.filter(UserId=-1).update(UserId=uid)  #only last order will be -1, so updates to Userid
            return render(request,'ordersuccess.html')
    else:
        form = OrderForm()
        uname = request.session['uname']
        return render(request,'order.html',{'form':form,'uname':uname})
    return render(request,'order.html')
def vieworders(request):
    orders = UserOrder.objects.all()     
    count = UserOrder.objects.all().count()
    suppliers = SupplierRegistration.objects.all()
    return render(request,'vieworders.html',{'orders':orders,'count':count,'suppliers':suppliers})

def deleteuser(request,id):
    UserRegistration.objects.filter(id=id).delete() #SELECT * FROM TABLE WHERE id=id
    users = UserRegistration.objects.all()
    return render(request,'viewusers.html',{'users':users})

def deletesupplier(request,id):
    #return HttpResponse("Delete Supplier button")
    SupplierRegistration.objects.filter(id=id).delete() #SELECT * FROM TABLE WHERE id=id
    users = SupplierRegistration.objects.all()
    return render(request,'viewsuppliers.html',{'users':users})

def deliver(request,id):
    UserOrder.objects.filter(id=id).update(OrderStatus = 'Delivered')
    #return HttpResponse("Delivered & Database is updated")
    return render(request,'delisucc.html')

def viewsupplierorders(request):
    id = request.session['sid']
    sorders = UserOrder.objects.filter(SupplierId=id)
    return render(request,'viewsupplierorders.html',{'sorders':sorders})
    #return HttpResponse("Supplier Orders Page")

def userorders(request,id):
    orders = UserOrder.objects.filter(UserId=id)
    return render(request,'userorders.html',{'orders':orders})
    #return HttpResponse("From User Orders")

def issuesupplier(request,id): 
    if request.method=='POST':
        sid = request.POST['sid']
        orderid = id
        UserOrder.objects.filter(id=orderid).update(SupplierId=sid,SupplierStatus='Assigned')
        orders = UserOrder.objects.all()
        return render(request,'vieworders.html',{'orders':orders})
    else:
        return HttpResponse("Cnfiguration is Required")
    return HttpResponse(id)


def userregisucc(request):
    return render(request,'userregisucc.html')

def ud(request):
    if request.method=='POST': 
        form = tudForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data is added")
    else:
        form = tudForm()
        return render(request,'usertemp.html',{'form':form})
    return render(request,'usertemp.html')

def md(request):
    if request.method=='POST':
        form = tmdForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data is added")
    else:                 
        form = tmdForm()
        return render(request,'mgrtemp.html',{'form':form})
    return render(request,'mgrtemp.html')

def au(request):   #approved users(au)
    users = tud.objects.all()
    return render(request,'approveusers.html',{'users':users})

def useranalysis1(request,id):   #approved users(au)
    if request.method =='POST':
        name = request.POST['one']
        tud.objects.filter(id=id).update(Status=name)
        users = tud.objects.all()
        return render(request,'useranalysis.html',{'users':users,'name':name})
    else:
        users = tud.objects.all()
        return render(request,'useranalysis.html',{'users':users})            
    return render(request,'useranalysis.html')

def useranalysis(request):
    users = tud.objects.all()
    return render(request,'useranalysis.html',{'users':users,'id':id})         

def checkadmin1(request):
    if request.method=='POST':
        aname = request.POST['aname']
        apwd =  request.POST['apwd']  
        if (aname=='admin' and apwd =='admin'):
            return render(request,'admin1home.html')

def admin1(request):
    return render(request,'admin1.html')

def logintype(request):
    return render(request,'login_type.html')