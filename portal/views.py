from django.shortcuts import render, redirect
from .models import *
from .filters import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string



def parcels(request):
    parcels = Parcel.objects.all()
    myFilter = ParcelFilter(request.GET, queryset=parcels)
    parcels = myFilter.qs

    drivers = Partner.objects.all()
  
    context = {'parcels': parcels, 'myFilter': myFilter, 'drivers':drivers}

    return render(request,'parcels.html',context)
    

def routes(request):

    routes = DriverRoute.objects.all()
    myFilter = RouterFilter(request.GET, queryset=routes)
    routes = myFilter.qs

    drivers = Partner.objects.all()

    context = {'routes': routes, 'myFilter':myFilter, 'drivers':drivers }

    return render(request, 'routes.html', context)


def register(request):
    customers = Customer.objects.all()
    form = CustomerForm(request.POST)

    if request.method == 'POST':

        if form.is_valid() :
            check_existing = customers.filter(sender_phone=request.POST['sender_phone']).exists() 
            if check_existing:
                messages.success(request, 'User with the same cellphone number already exists')
            else:
                form.save()
                return redirect('customers')

    context = {'form':form, 'customer':customers}

    return render(request, 'register.html', context)


def customer(request):
    customers = Customer.objects.all()
    myFilter = CustomerFilter(request.GET,queryset=customers)
    customers = myFilter.qs

    context = {'customers':customers, 'myFilter':myFilter}

    return render(request,'customers.html', context)



def updateCustomer(request,pk):
    customer = Customer.objects.get(id=pk)

    form = CustomerForm(instance=customer)
        
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('send_parcel')

    context = {'form':form}

    return render(request,'updateCustomer.html', context)


def send_parcel(request):
    form = ParcelForm()

    if request.method == 'POST':
        parcel = Parcel.objects.all()
        form = ParcelForm(request.POST)
        if form.is_valid():
            check_existing = parcel.filter(refNumber=request.POST['refNumber']).exists()
            if check_existing:
                messages.success(request, 'Parcel with the same reference number already exists')
            else:
                form.save()
            return redirect('dispatch')
    
    context = {'form':form,}
    return render(request,'sendParcel.html', context)


def parcelSearch(request, pk):
    customer = Customer.objects.get(id=pk)
    parcels = customer.parcel_set.all()
    myFilter = ParcelFilter(request.GET, queryset=parcels)
    parcels = myFilter.qs
  
    context = {'parcels': parcels, 'myFilter': myFilter}

    return render(request, 'searchParcel.html', context)


def tracker(request):
    parcels = Parcel.objects.all()
    drivers = Partner.objects.all()
    myFilter = ParcelFilter(request.GET, queryset=parcels)
    parcels = myFilter.qs
    context = {'parcels': parcels, 'myFilter': myFilter, 'drivers':drivers}

    return render(request,'tracker.html', context)


def trackerSearch(request, pk):
    customer = Customer.objects.get(id=pk)
    parcels = customer.parcel_set.all()
    myFilter = ParcelFilter(request.GET, queryset=parcels)
    parcels = myFilter.qs
  
    context = {'parcels': parcels, 'myFilter': myFilter}

    return render(request, 'trackerSearch.html', context)


def readyDispatch(request):
    parcels = Parcel.objects.all()
    myFilter = ParcelFilter(request.GET, queryset=parcels)
    parcels = myFilter.qs
  
    context = {'parcels': parcels, 'myFilter': myFilter}

    return render(request,'dispatchParcel.html',context)


def dispatch(request, pk):
    parcels = Parcel.objects.get(id=pk)

    form = ParcelForm(instance=parcels)
        
    if request.method == 'POST':
        form = CustomerForm(request.POST,instance=parcels)
        if form.is_valid():
            form.save()
            return redirect('submitDispatch')

    context = {'form':form}

    return render(request,'dispatchParcel.html', context)



def updateParcel(request, pk):
    parcel = Parcel.objects.get(id=pk)

    form = ParcelForm(instance=parcel)

    context = {'form':form}

    if request.method == 'POST':
        form = ParcelForm(request.POST,instance=parcel)

        if form.is_valid(): 
            form.save()

            return redirect('updatePartner',pk)

    return render(request, 'updateParcel.html',context)


def send_dispatch(request, pk):
    parcel = Parcel.objects.get(id=pk)

    form = ParcelForm(instance=parcel)

    context = {'form':form}

    if request.method == 'POST':
        form = ParcelForm(request.POST,instance=parcel)

        if form.is_valid(): 
            form.save()

            return redirect('addPartner')

    return render(request, 'updateParcel.html',context)


def deleteParcel(request, pk):
    parcel = Parcel.objects.get(id=pk)
   
    if request.method == 'POST':
        parcel.delete()
        return redirect('tracker')

    context = {'item':parcel}

    return render(request, 'deleteParcel.html',context)


def updatePartner(request, pk):
    
    driver = Partner.objects.get(parcel=pk)
       
    driver_form = PartnerForm(instance=driver)
    
    context = {'driver_form':driver_form}
        
    if request.method == 'POST':
        driver_form = PartnerForm(request.POST,instance=driver)

        if driver_form.is_valid(): 
            driver_form.save()

            return redirect('tracker')
    
    return render(request, 'updatePartner.html', context)


def addPartner(request):
    form = PartnerForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('tracker')
    
    context = {'form':form}

    return render(request,'addPartner.html', context)


def addTaxiRank(request):
    form = RouterForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('routes')
    
    context = {'form':form}

    return render(request,'addTaxiRank.html',context)


def signupPage(request):
    form = SignupUserForm(request.POST)
    users = User.objects.all()

    if form.is_valid():
        check_existing = users.filter(email=request.POST['email']).exists()
        if check_existing:
            messages.success(request, 'User with the same Email Address already exists')
        else:
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user )
            return redirect('login')
    
    context = {'form':form}
    return render (request, 'signup.html', context)


def signinPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')



        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('tracker')
        else:
            messages.info(request, 'Incorrect Username/Password')
            
    context = {}
    return render (request, 'signin.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


def users(request):
    form = ApplicationForm(request.POST)
    
    if form.is_valid():               
        name = form.cleaned_data['fname']
        surname = form.cleaned_data['lname']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        address = form.cleaned_data['raddress']
        job = form.cleaned_data['job']
        province = form.cleaned_data['province']
        city = form.cleaned_data['city']
        motivation = form.cleaned_data['motivation']

        context_email = {'name':name, 'surname':surname, 'phone':phone, 'email':email, 'address':address, 'job':job, 'province':province, 'city':city, 'motivation':motivation}

        html = render_to_string('applicationEmail.html', context_email)  

        send_mail('Job Aplication', 'Job Application Details', 'mrgig.taxicourier@gmail.com',['taxicourier@mrgig.co.za'], fail_silently=False, html_message=html)
        
        return redirect('/')
    context = {'form':form}
    return render(request, 'userProfile.html', context)
