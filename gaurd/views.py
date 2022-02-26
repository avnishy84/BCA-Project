from django.shortcuts import render , redirect
from .models import gaurd_data
from entry.views import index
from entries.models import entry_data
from datetime import datetime
# Create your views here.

def gaurd(request):
    if request.session.get('guser'):
        return render(request,'slogin.html')
    else:
        return render(request,'gaurd.html')

def slogin(request):
    suser = request.POST['suser']
    spass = request.POST['spass']
    res = gaurd_data.objects.filter(username=suser,password=spass)
    if len(res)==1:
        data=entry_data.objects.all()
        request.session['guser']=res[0].username
        fname=res[0].firstname
        lname=res[0].lastname
        email=res[0].email
        doj=res[0].DOJ
        mobile=res[0].mobile
        return render(request,'slogin.html',{'res':data,'fname':fname,'lname':lname,'email':email,'doj':doj,'mobile':mobile})
    else:
        return render(request,'gaurd.html',{'error':'Incorrect username or password'})
   

def home (request):
    return redirect ('http://127.0.0.1:8000')


def logout(request):
    del request.session['guser']
    return redirect ('/gaurd/')
    
def gaurdent(request):
    
    if request.session.get('guser'):
        obj=entry_data.objects.all()
        return render(request,'gaurdent.html',{'res':obj})
    else:
        return redirect ('/gaurd/')

def newentry(request):
    if request.session.get('guser'):
        pur=request.POST['pur']
        NAME=request.POST['fullname']
        MOBILE=request.POST['mobile']
        ENTRY=datetime.now().strftime("%Y/%m/%d %H:%M")
        
        a=entry_data(date=pur ,name=NAME ,mobile=MOBILE ,entrytime=ENTRY )
        a.save()
        return redirect('/gaurd/gaurdent')
    else:
        return redirect ('/gaurd/')
        
def exit(request):
	if request.session.get('guser'):
		res = entry_data.objects.all()
		return render(request,'gaurdent.html',{'res':res})
	else:
		return redirect('/gaurd/')
		
def update_exit(request):
    extime = datetime.now().replace(microsecond=0)
    id = request.GET['id']
    k = entry_data.objects.get(id=id)
    k.exittime=extime.strftime("%Y/%m/%d %H:%M")
    k.save()
    return redirect('/gaurd/gaurdent')