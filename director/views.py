from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import director_login
from gaurd.models import gaurd_data
from entries.models import entry_data

# Create your views here.
def director(request):
    if request.session.get('user'):
        return render(request,'dpage.html')
    else:
        return render(request,'director.html')
    

def dlogin(request):
    duser = request.POST['duser']
    dpass = request.POST['dpass']
    
    res = director_login.objects.filter(username=duser, password=dpass)
    
    if len(res)==1:
        request.session['user']=res[0].username
        return render(request,'dpage.html')
    else:
        return render(request,'director.html',{'error':'Incorrect username or password'})

def regisact(request):
    if request.session.get('user'):
        username=request.POST['username']
        password=request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        doj = request.POST['DOJ']
        email = request.POST['email']
        mobile = request.POST['mobile']
            
        res=gaurd_data.objects.filter(username=username)
        if len(res)==1:
           return render(request,'regis.html',{'error':'Account Already Existed with same username try Another One'})
        else:
            a=gaurd_data(username=username,password=password,firstname=firstname,lastname=lastname,DOJ=doj,email=email,mobile=mobile)
            a.save()
            return render(request,'regis.html',{'error':a.firstname,'msg':'New Account is Created Succesfully for'})
    else:
        return redirect ('/director/')
        
def regis(request):
    return render(request,'regis.html')
    
def logout(request):
    del request.session['user']
    return redirect ('/director/')
    
def home (request):
    if request.session.get('user'):
        return render (request,'dpage.html')
    else:
        return redirect ('/director/')
        
def entries(request):
    if request.session.get('user'):
        obj=entry_data.objects.all()
        return render(request,'entries.html',{'res':obj})
    else:
        return redirect ('/director/')    
        
def delete(request):
	if request.session.get('guser'):
		res = entry_data.objects.all()
		return render(request,'enteries.html',{'res':res})
	else:
		return redirect('/director/')
		
def update_delete(request):
    id = request.GET['id']
    entry_data.objects.filter(id=id).delete()
    return redirect('/director/entries')
    
def index (request):
    return redirect ('http://127.0.0.1:8000')