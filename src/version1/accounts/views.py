from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from travello.models import Destination

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
         return render(request,'login.html')   

def register (request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created') 
                return redirect('login')
        else:
            messages.info(request,'password not matching .. ')
            return redirect('register')
        return redirect('/')
    else:
        return render (request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def createimg(request):
    print('crear imagen')
    if request.method=='POST':
        print('creado con post')
        Name=request.POST['Name']
        Direccion=request.FILES['Direccion']
        Descripcion=request.POST['Descripcion']
        Precio=request.POST['Precio']
        Oferta=request.POST.get('Oferta',False)
        print(Name)
        print(Direccion)
        print(Descripcion)
        print(Precio)
        if Oferta=='on':
            Oferta=True
        else :
            Oferta=False
        imgs=Destination.objects.create(name=Name,img=Direccion,desc=Descripcion,price=Precio,offer=Oferta)
        imgs.save()
        print('destino agregado')
        dests=Destination.objects.all()

        
    return render (request,'createimg.html')
def eliminar(request,id):
    data=Destination.objects.get(id=id)
    data.delete()
    return redirect(to='listar')
def modificar(request,id):
    data=Destination.objects.get(id=id)
    if request.method=='POST':
        data=Destination()
        data.id=request.POST['textid']
        data.name=request.POST['Name']
        data.img=request.FILES['Direccion']
        data.desc=request.POST['Descripcion']
        data.price=request.POST['Precio']
        data.offer=request.POST.get('Oferta',False)
        if data.offer=='on':
            data.offer=True
        else :
            data.offer=False
        data.save()
        return redirect('listar')
    return render(request,'modificar.html',{'data':data,})
def listar(request):
    data=Destination.objects.all()
    return render(request,'listar.html',{'data':data,})

