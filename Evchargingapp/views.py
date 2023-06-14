from datetime import date, timezone
import datetime
import json
import math
import time
from django.shortcuts import render,HttpResponse
from flask import redirect
from .models import AddStation, Booking, EVUser, User,UserBill,Rating
from django.contrib.auth import authenticate
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

def session_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if 'id' not in request.session:
            # Redirect to a login page or any other appropriate action
              
            messages.error(request, 'Please Login First')
            return redirect('loginsignup')  # Replace 'login' with your login URL name

        # Session exists, continue to the original view function
        return view_func(request, *args, **kwargs)

    return wrapped_view
# Create your views here.f
def index(request):
    return render(request,'Ev-Charging/index.html')
    # return HttpResponse("helooooo")

def home(request):
    return render(request,'Ev-Charging/index.html')
def about(request):
    return render(request,'Ev-Charging/about.html')
def services(request):
    return render(request,'Ev-Charging/service.html')
def news(request):
    return render(request,'Ev-Charging/news.html')
def contact(request):
    return render(request,'Ev-Charging/contact.html')
def userlogin(request):
    return render(request,'Ev-Charging/login-signup copy.html')

def stationlogin(request):
    return render(request,'Ev-Charging/login-signup.html')
def stationloginuser(request):
    return render(request,'Ev-Charging/login-signup copy 2.html')

def loginsignup(request):
    return render(request,'Ev-Charging/login.html')
def login(request):
    your_name = request.GET.get('email')
    your_pass = request.GET.get('your_pass')
    
    id = request.session.get('id')
    if id:
        return render(request,'NavUserAdmin/index.html')
    
    else:
     try:
       user=User.objects.get(email=your_name,password=your_pass)
    #    users = authenticate(request, username=user.username, password=user.password)
    #    login(request, users)
       request.session['email'] = your_name
       request.session['id'] = user.id
       messages.success(request, 'Your Login success')
       return render(request,'NavUserAdmin/index.html')
    
     except:
          
        messages.error(request, 'User Not Exist Please Check Email and Password')
        return render(request,'Ev-Charging/login-signup.html')
        return render(request,'Ev-Charging/login-signup.html')
def loginstationuser(request):
    your_name = request.GET.get('email')
    your_pass = request.GET.get('your_pass')
    
    id = request.session.get('id')
    if id:
        return render(request,'NavUserStation/index.html')
    
    else:
     try:
       user=AddStation.objects.get(user_email=your_name,password=your_pass)
       request.session['email'] = your_name
       request.session['id'] = user.id
    #    users = authenticate(request, username=user.username, password=user.password)
    #    login(request, users)
         
       messages.success(request, 'Your Login success')
       return render(request,'NavUserStation/index.html')
    
     except:
          
        messages.error(request, 'User Not Exist Please Check Email and Password')
        return render(request,'Ev-Charging/login-signup copy 2.html')
        return render(request,'Ev-Charging/login-signup.html')

def loginuser(request):
    your_name = request.GET.get('email')
    your_pass = request.GET.get('your_pass')
    # id = request.session.get('id')
    # request.session.clear()
    id = request.session.get('id')
    if id:
        return render(request,'NavUser/indexuser.html')
    
    else:
     try:
       user=EVUser.objects.get(email=your_name,password=your_pass)
       request.session['email'] = your_name
       request.session['id'] = user.id
         
       messages.success(request, 'Your Login success')
    #    users = authenticate(request, username=user.username, password=user.password)
    #    login(request, users)
       return render(request,'NavUser/indexuser.html')
    
     except:
          
        messages.error(request, 'User Not Exist Please Check Email and Password')
        return render(request,'Ev-Charging/login-signup copy.html')
        return render(request,'Ev-Charging/login-signup.html')
    

def signup(request):
    user_name = request.POST.get('name')
    user_email = request.POST.get('email')
    user_passward = request.POST.get('pass')
    user = User(username=user_name, email=user_email, password=user_passward)
    user.save()
      
    messages.success(request, 'Your SignUp success')
    return render(request,'Ev-Charging/login-signup.html')
def usersignup(request):
    user_name = request.POST.get('name')
    user_email = request.POST.get('email')
    user_passward = request.POST.get('pass')
    user = EVUser(username=user_name, email=user_email, password=user_passward)
    user.save()
      
    messages.success(request, 'Your SignUp success')
    return render(request,'Ev-Charging/login-signup copy.html')

@session_required 
def navigator(request):
    val=AddStation.objects.all()
    # my_list = json.loads(serialize('json', val))
    # request.session['my_array'] = val
    # my_list_json = json.dumps(val)
    return render(request,'NavUser/navigator.html', {'locate':val})
@session_required 
def station(request):
    return render(request,'NavUser/stations.html')
@session_required 
def navhome(request):
    return render(request,'NavUser/index.html')
@session_required  
def rating(request):
    if request.method == 'POST':
        user_id = request.POST.get('userid')
        station_id = request.POST.get('stationid')
        bill_id = request.POST.get('billid')
        rating_number = request.POST.get('rating')
        bill=UserBill.objects.get(id=bill_id)
        bill.rating=rating_number
        bill.save()
        # Create a new rating instance
        rating = Rating(user_id=user_id, station_id=station_id, bill_id=bill_id, rating_number=rating_number)
        
        # Save the rating instance to the database
        rating.save()
        id = request.session.get('id')
        user=UserBill.objects.filter(userid=id)
    # book=Booking.objects.filter(ev_user=user)
        return render(request,'NavUser/bookingratings.html',{'books':user})

# Save the rating instance to the database
    # rating.save()
    # return render(request,'NavUser/index.html')
@session_required 
def booking(request):
    id = request.session.get('id')
    user=EVUser.objects.get(id=id)
    book=Booking.objects.filter(ev_user=user)
    return render(request,'NavUser/booking.html',{'books':book})
@session_required  
def bookingrating(request):
    id = request.session.get('id')
    user=UserBill.objects.filter(userid=id)
    # book=Booking.objects.filter(ev_user=user)
    return render(request,'NavUser/bookingratings.html',{'books':user})
@session_required  
def profile(request):
    return render(request,'Admin/profile.html')

@session_required  
def manageuser(request):
    user=AddStation.objects.all()
    return render(request,'Admin/manageuserstation.html',{'users':user})
@session_required  
def manageusers(request):
    user=EVUser.objects.all()
    return render(request,'Admin/manageuser.html',{'users':user})
@session_required  
def addstation(request):
    return render(request,'Admin/addchargingstation.html')
@session_required  
def stationview(request):
    # id = request.session.get('id')
    # user=AddStation.objects.all()
    try:
       add_station = AddStation.objects.all()
       Rate=[]
       count=0
       rating=0
       print("1")
       for i  in add_station:
           print("1")
           ratee=Rating.objects.filter(station_id=i.id)
           count1 = ratee.count()
           print(count1)
           if(count1==0):
                Rate.append(0)
           
           else:  
            count=0
            rating=0
            print("1")
            print(ratee)
            for j in ratee:
              print("2")
              print(j.rating_number,"Check")
              rating=rating+j.rating_number
              count=count+1
            rating=rating/count
            print("3")
            rounded_rating = round(rating, 1)
            Rate.append(rounded_rating)
            
       print("5")
       data = zip(add_station, Rate)
       print("6")
       return render(request,'Admin/chargingstatiiion.html',{'station':data})
    except:
      
       return render(request,'Admin/addchargingstation.html')
   
# def stationview(request):
#     # id = request.session.get('id')
#     # user=AddStation.objects.all()
#     try:
#        add_station = AddStation.objects.all()
#        return render(request,'Admin/chargingstatiiion.html',{'station':add_station})
#     except:
#        return render(request,'Admin/addchargingstation.html')
   
@session_required  
def deletestations(request,value):
    id = request.session.get('id')
    user=User.objects.get(id=id)
    add_station = AddStation.objects.get(id=value)
    add_station.delete()
      
    messages.success(request, 'Deleted Success')
    return redirect('stationview')
    # return render(request,'Admin/addchargingstation.html')
@session_required  
def stationedit(request,value):
    # id = request.session.get('id')
    # user=User.objects.get(id=id)
    add_station = AddStation.objects.get(id=value)
      
    messages.success(request, 'Edited Success')
    return render(request,'Admin/stationedit.html',{'station':add_station})

@session_required  
def viewbooking(request):
    countbooking=[]
    count=0
    station=AddStation.objects.all()
    for i in station:
        book=Booking.objects.filter(add_station=i)
        for j in book:
            count=count+1
        countbooking.append(count)
        count=0
    data = zip(station, countbooking)
    return render(request,'Admin/bookingslot.html',{'booking':data})
@session_required  
def bill(request,value):
    book=Booking.objects.get(id=value)
    return render(request,'AdminStation/bill.html',{'booking':book})
@session_required  
def completecharging(request):
    
    billamount = request.GET.get('totalbill')
    value = request.GET.get('id')
    book=Booking.objects.get(id=value)
    bill = UserBill()
    bill.amount = billamount
    bill.username = book.ev_user.username
    bill.userid = book.ev_user.id
    bill.stationid = book.add_station.id
    bill.date = date.today()
    current_time = time.localtime()
    bill.time = current_time  # Assuming the time is 12:30:00

# Save the instance to the database
    bill.save()
    book.delete()
      
    messages.success(request, 'Charging Complete')
    return redirect('viewbookingstation')
    # return render(request,'AdminStation/bill.html',{'booking':book})
@session_required  
def checkstation(request):
    id = request.session.get('id')
    station=AddStation.objects.get(id=id)
    return render(request,'AdminStation/bookingslot.html',{'check':station})
@session_required  
def viewbookingstation(request):
    id = request.session.get('id')
    print(id)
    
    station=AddStation.objects.get(id=id)
    print(station)
    book=Booking.objects.filter(add_station=station)
    print(book)
    return render(request,'AdminStation/bookingslot.html',{'bookev':book})
@session_required  
def userpayment(request):
    return render(request,'Admin/userpayment.html')
@session_required  
def earning(request):
    amount=[]
    totalbooking=[]
    billamount=0
    count=0
    station=AddStation.objects.all()
    for i in station:
        bill=UserBill.objects.filter(stationid=i.id)
        for j in bill:
            billamount=billamount+j.amount
            count=count+1
        amount.append(billamount)
        totalbooking.append(count)
        billamount=0
        count=0
    data = zip(station, amount,totalbooking)
    return render(request, 'Admin/earning.html', {'data': data})
    # return render(request,'Admin/earning.html',{'stations':station,'earn':amount})
@session_required  
def earningstation(request):
    id = request.session.get('id')
    # print(id)
    station = UserBill.objects.filter(stationid=id).order_by('-id')
    print(station)
    return render(request,'AdminStation/earning.html',{'earnings':station})
@session_required  
def ratingstation(request):
    id = request.session.get('id')
    # print(id)
    station = UserBill.objects.filter(stationid=id).order_by('-id')
    print(station)
    return render(request,'AdminStation/rating.html',{'earnings':station})
@session_required  
def totalearning(request):
    id = request.session.get('id')
    # print(id)
    station=UserBill.objects.filter(stationid=id)
    sumt=0
    for i in station:
        sumt=sumt+i.amount
    # print(station)
    return render(request,'AdminStation/totalearning.html',{'sum':sumt})
@session_required  
def bookingev(request):
    lat1 = request.POST.get('latitude')
    lon1 = request.POST.get('longitude')
    print(lat1,"chceking lat")
    destination = request.POST.get('destination')
    lat1=float(lat1)
    lon1=float(lon1)
    # latitude = request.POST.get('latitude')
    # val=AddStation.objects.all()
    station=AddStation.objects.all()
    val=station
    speed = 100
    for i in station:
        if i.station_name==destination:
            lat2=i.latitude
            lon2=i.longitude
            radius = 6371.0
            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad
            a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = radius * c
            time = distance / speed
            slots=i.slots_number
            stationid=i.id
            slotcout=Booking.objects.filter(add_station=i).count()
            slots=slots-slotcout
            hours = int(time)
            minutes = int((time - hours) * 60)
            seconds = int(((time - hours) * 60 - minutes) * 60)
            time="Hour:  "+str(hours)+" Minutes:  "+str(minutes)+" Seconds:  "+str(seconds)
            return render(request,'NavUser/bookingev.html',{'times':time , 'distances':distance ,'locate':val,'slot':slots,"id":stationid})

    
    # # lat1 = 31.3684
    # # lon1 = 74.2634
    # lat2 = 31.4100
    # lon2 = 74.2072
    
    
    # lat1_rad = math.radians(lat1)
    # lon1_rad = math.radians(lon1)
    # lat2_rad = math.radians(lat2)
    # lon2_rad = math.radians(lon2)
    # dlat = lat2_rad - lat1_rad
    # dlon = lon2_rad - lon1_rad
    # a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # distance = radius * c
    # time = distance / speed
    
    # return render(request,'NavUser/bookingev.html',{'times':time , 'distances':distance})
@session_required  
def adminbookingev(request):
    lat1 = request.POST.get('latitude')
    lon1 = request.POST.get('longitude')
    print(lat1,"chceking lat")
    destination = request.POST.get('destination')
    lat1=float(lat1)
    lon1=float(lon1)
    # latitude = request.POST.get('latitude')
    # val=AddStation.objects.all()
    station=AddStation.objects.all()
    val=station
    speed = 100
    for i in station:
        if i.station_name==destination:
            lat2=i.latitude
            lon2=i.longitude
            radius = 6371.0
            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad
            a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = radius * c
            time = distance / speed
            slots=i.slots_number
            stationid=i.id
            slotcout=Booking.objects.filter(add_station=i).count()
            slots=slots-slotcout
            hours = int(time)
            minutes = int((time - hours) * 60)
            seconds = int(((time - hours) * 60 - minutes) * 60)
            time="Hour:  "+str(hours)+" Minutes:  "+str(minutes)+" Seconds:  "+str(seconds)
            return render(request,'NavUserAdmin/bookingev.html',{'times':time , 'distances':distance ,'locate':val,'slot':slots,"id":stationid})
@session_required  
def addstationdetails(request):
    stationName = request.POST.get('stationName')
    location = request.POST.get('location')
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    ownerName = request.POST.get('ownerName')
    slotsNumber = request.POST.get('slotsNumber')
    timing = request.POST.get('timing')
    email = request.POST.get('email')
    password = request.POST.get('password')
    id = request.session.get('id')
    print(stationName)
    user=User.objects.get(id=id)
    add_station = AddStation.objects.create(
    station_name=stationName,
    location_city=location,
    longitude=longitude,
    latitude=latitude,
    owner_name=ownerName,
    slots_number=slotsNumber,
    timing=timing,
    user_email=email,
    password=password,
    user=user  # Assign the user object to the "user" field
   )
    add_station.save()
    return render(request,'Admin/addchargingstation.html')
@session_required  
def addstationdetailsupdate(request):
    stationid = request.POST.get('stationid')
    stationName = request.POST.get('stationName')
    location = request.POST.get('location')
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    ownerName = request.POST.get('ownerName')
    slotsNumber = request.POST.get('slotsNumber')
    timing = request.POST.get('timing')
    email = request.POST.get('email')
    password = request.POST.get('password')
    id = request.session.get('id')
    print(stationName)
    # user=User.objects.get(id=id)
    add_station = AddStation.objects.get(id=stationid)
    add_station.station_name = stationName
    add_station.location_city = location
    add_station.longitude =longitude
    add_station.latitude =latitude
    add_station.owner_name = ownerName
    add_station.slots_number = slotsNumber
    add_station.timing =timing
    add_station.user_email =email
    add_station.password =password
    
    add_station.save()
      
    messages.success(request, 'Updated Success')
    add_station = AddStation.objects.all()
    return render(request,'Admin/chargingstatiiion.html',{'station':add_station})
    # return render(request,'Admin/addchargingstation.html')

@session_required  
def ristrict(request,value):
    user=User.objects.get(id=value)
    user.status="No"
    user.save()
      
    messages.success(request, 'Ristricted Success')
    user=User.objects.all()
    return render(request,'Admin/manageuser.html',{'users':user})
@session_required  
def unristrict(request,value):
    user=User.objects.get(id=value)
    user.status="Yes"
    user.save()
      
    messages.success(request, 'UnRistricted Success')
    user=User.objects.all()
    return render(request,'Admin/manageuser.html',{'users':user})
@session_required  
def deleteuserstation(request,value):
    user=AddStation.objects.get(id=value)
    user.delete()
      
    messages.success(request, 'Deleted Success')
    user=AddStation.objects.all()
    return render(request,'Admin/manageuserstation.html',{'users':user})
@session_required 
def deleteuser(request,value):
    user=EVUser.objects.get(id=value)
    user.delete()
      
    messages.success(request, 'Deleted Success')
    user=EVUser.objects.all()
    return render(request,'Admin/manageuser.html',{'users':user})
@session_required     
def bookingevdone(request,value):
    id = request.session.get('id')
    try:
       user=EVUser.objects.get(id=id)
       station=AddStation.objects.get(id=value)
       count = Booking.objects.filter(add_station=station).count()
    
       if(count<station.slots_number):
            addbooking = Booking.objects.create(
     # Assign the user object to the "user" field
            ev_user=user,
            add_station=station
             )
            addbooking.save()
            id = request.session.get('id')
            user=EVUser.objects.get(id=id)
            book=Booking.objects.filter(ev_user=user)
              
            messages.success(request, 'Booking Success')
            return render(request,'NavUser/booking.html',{'books':book})
            # return redirect('booking')
            
       else:
            val=AddStation.objects.all()
              
            messages.error(request, 'No Slot Availiable Please Try Another Station')
            return render(request,'NavUser/navigator.html', {'locate':val})
    except:
        val=AddStation.objects.all()
          
        messages.error(request, 'No Slot Availiable Please Try Another Station')
        return render(request,'NavUser/navigator.html', {'locate':val}) 
   
@session_required      
def cancelbookingev(request,value):
    book=Booking.objects.get(id=value)
    book.delete()
    id = request.session.get('id')
    user=EVUser.objects.get(id=id)
    book=Booking.objects.filter(ev_user=user)
      
    messages.success(request, 'Booking Cancle Success')
    return render(request,'NavUser/booking.html',{'books':book})
    
    # redirect('booking')
    # return 0
    
    


@session_required  
def filter(request):
    
    lat1 = request.POST.get('latitude')
    lon1 = request.POST.get('longitude')
    minute = request.POST.get('minute')
    print(lat1,"checking")
    destination = request.POST.get('destination')
    lat1=float(lat1)
    lon1=float(lon1)
    # latitude = request.POST.get('latitude')
    # val=AddStation.objects.all()
    station=AddStation.objects.all()
    val=station
    speed = 100
    locations=[]
    for i in station:
        # if i.station_name==destination:
            lat2=i.latitude
            lon2=i.longitude
            radius = 6371.0
            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad
            a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = radius * c
            time = distance / speed
            slots=i.slots_number
            stationid=i.id
            slotcout=Booking.objects.filter(add_station=i).count()
            slots=slots-slotcout
            hours = int(time)
            minutes = int((time - hours) * 60)
            seconds = int(((time - hours) * 60 - minutes) * 60)
            if minutes <= int(minute):
                locations.append(i)
    return render(request,'NavUser/navigator.html', {'locate':locations})   
@session_required  
def filterstation(request):
    
    lat1 = request.POST.get('latitude')
    lon1 = request.POST.get('longitude')
    minute = request.POST.get('minute')
    print(lat1,"checking")
    destination = request.POST.get('destination')
    lat1=float(lat1)
    lon1=float(lon1)
    # latitude = request.POST.get('latitude')
    # val=AddStation.objects.all()
    station=AddStation.objects.all()
    val=station
    speed = 100
    locations=[]
    for i in station:
        # if i.station_name==destination:
            lat2=i.latitude
            lon2=i.longitude
            radius = 6371.0
            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad
            a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = radius * c
            time = distance / speed
            slots=i.slots_number
            stationid=i.id
            slotcout=Booking.objects.filter(add_station=i).count()
            slots=slots-slotcout
            hours = int(time)
            minutes = int((time - hours) * 60)
            seconds = int(((time - hours) * 60 - minutes) * 60)
            if minutes <= int(minute):
                locations.append(i)
    return render(request,'NavUserStation/navigator.html', {'locate':locations})   
@session_required      
def filterdistance(request):
    
    lat1 = request.POST.get('latitude')
    lon1 = request.POST.get('longitude')
    minute = request.POST.get('minute')
    print(lat1,"checking")
    destination = request.POST.get('destination')
    lat1=float(lat1)
    lon1=float(lon1)
    # latitude = request.POST.get('latitude')
    # val=AddStation.objects.all()
    station=AddStation.objects.all()
    val=station
    speed = 100
    locations=[]
    for i in station:
        # if i.station_name==destination:
            lat2=i.latitude
            lon2=i.longitude
            radius = 6371.0
            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad
            a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = radius * c
            time = distance / speed
            slots=i.slots_number
            stationid=i.id
            slotcout=Booking.objects.filter(add_station=i).count()
            slots=slots-slotcout
            hours = int(time)
            minutes = int((time - hours) * 60)
            seconds = int(((time - hours) * 60 - minutes) * 60)
            if distance <= int(minute):
                locations.append(i)
    return render(request,'NavUser/navigator.html', {'locate':locations})   
@session_required  
def filterdistancestation(request):
    
    lat1 = request.POST.get('latitude')
    lon1 = request.POST.get('longitude')
    minute = request.POST.get('minute')
    print(lat1,"checking")
    destination = request.POST.get('destination')
    lat1=float(lat1)
    lon1=float(lon1)
    # latitude = request.POST.get('latitude')
    # val=AddStation.objects.all()
    station=AddStation.objects.all()
    val=station
    speed = 100
    locations=[]
    for i in station:
        # if i.station_name==destination:
            lat2=i.latitude
            lon2=i.longitude
            radius = 6371.0
            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad
            a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = radius * c
            time = distance / speed
            slots=i.slots_number
            stationid=i.id
            slotcout=Booking.objects.filter(add_station=i).count()
            slots=slots-slotcout
            hours = int(time)
            minutes = int((time - hours) * 60)
            seconds = int(((time - hours) * 60 - minutes) * 60)
            if distance <= int(minute):
                locations.append(i)
    return render(request,'NavUserStation/navigator.html', {'locate':locations})   
@session_required  
def getstation(request):
    print("hello")
    val=AddStation.objects.all()
    # my_list = json.loads(serialize('json', val))
    # request.session['my_array'] = val
    # my_list_json = json.dumps(val)
    return val

@session_required  
def logout(request):
    request.session.clear()
    # logout(request)
    # my_list = json.loads(serialize('json', val))
    # request.session['my_array'] = val
    # my_list_json = json.dumps(val)
      
    messages.success(request, 'Logout Success')
    return render(request,'Ev-Charging/index.html')

#admin
@session_required  
def navhomeadmin(request):
    return render(request,'NavUserAdmin/index.html')
@session_required  
def navigatoradmin(request):
    val=AddStation.objects.all()
    # my_list = json.loads(serialize('json', val))
    # request.session['my_array'] = val
    # my_list_json = json.dumps(val)
    return render(request,'NavUserAdmin/navigator.html', {'locate':val})
@session_required  
def stationadmin(request):
    return render(request,'NavUserAdmin/stations.html')
@session_required  
def bookingadmin(request):
    id = request.session.get('id')
    user=EVUser.objects.get(id=id)
    book=Booking.objects.filter(ev_user=user)
    return render(request,'NavUserAdmin/booking.html',{'books':book})
@session_required  
def profileadmin(request):
    return render(request,'Admin/profile.html')

#station
@session_required  
def navhomestation(request):
    return render(request,'NavUserStation/index.html')
@session_required  
def navigatorstation(request):
    val=AddStation.objects.all()
    # my_list = json.loads(serialize('json', val))
    # request.session['my_array'] = val
    # my_list_json = json.dumps(val)
    return render(request,'NavUserStation/navigator.html', {'locate':val})
@session_required  
def stationstation(request):
    return render(request,'NavUserStation/stations.html')
@session_required  
def bookingstation(request):
    id = request.session.get('id')
    user=EVUser.objects.get(id=id)
    book=Booking.objects.filter(ev_user=user)
    return render(request,'NavUserStation/booking.html',{'books':book})
@session_required  
def profilestation(request):
    return render(request,'AdminStation/profile.html')

@session_required  
def bookingevadmin(request):
    lat1 = request.POST.get('latitude')
    lon1 = request.POST.get('longitude')
    print(lat1,"chceking lat")
    destination = request.POST.get('destination')
    lat1=float(lat1)
    lon1=float(lon1)
    # latitude = request.POST.get('latitude')
    # val=AddStation.objects.all()
    station=AddStation.objects.all()
    val=station
    speed = 100
    for i in station:
        if i.station_name==destination:
            lat2=i.latitude
            lon2=i.longitude
            radius = 6371.0
            lat1_rad = math.radians(lat1)
            lon1_rad = math.radians(lon1)
            lat2_rad = math.radians(lat2)
            lon2_rad = math.radians(lon2)
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad
            a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = radius * c
            time = distance / speed
            slots=i.slots_number
            stationid=i.id
            slotcout=Booking.objects.filter(add_station=i).count()
            slots=slots-slotcout
            hours = int(time)
            minutes = int((time - hours) * 60)
            seconds = int(((time - hours) * 60 - minutes) * 60)
            time="Hour:  "+str(hours)+" Minutes:  "+str(minutes)+" Seconds:  "+str(seconds)
            return render(request,'NavUserStation/bookingev.html',{'times':time , 'distances':distance ,'locate':val,'slot':slots,"id":stationid})
        
@session_required         
def passwordchangestation(request):
    return render(request,'AdminStation/profile1.html')
@session_required  
def updatepasswordstation(request):
    if request.method == 'POST':
        id = request.session.get('id')
        submitted_password = request.POST['old_password']

        station = AddStation.objects.get(id=id)

        if station.password == submitted_password:
            # Password matches, update the password
            station.password = request.POST['new_password']
            station.save()
              
            messages.success(request, 'Updated Password Success')
            return render(request,'AdminStation/profile1.html')
        else:
            # Password doesn't match, return back or display an error message
              
            messages.error(request, 'Not Updated Success')
            return render(request,'AdminStation/profile1.html')  # You can replace 'password_mismatch' with the appropriate URL name or path

    # return redirect('success')
    # return render(request,'AdminStation/profile.html')
@session_required  
def changepassworduser(request):
    return render(request,'NavUser/changepassword.html')
@session_required  
def changepassworduserupdate(request):
    if request.method == 'POST':
        id = request.session.get('id')
        submitted_password = request.POST['oldPassword']

        station = EVUser.objects.get(id=id)

        if station.password == submitted_password:
            # Password matches, update the password
            station.password = request.POST['newPassword']
            station.save()
              
            messages.success(request, 'Updated Password Success')
            return render(request,'NavUser/index.html')
        else:
            # Password doesn't match, return back or display an error message
              
            messages.error(request, 'Not Updated Success')
            return render(request,'NavUser/changepassword.html')  
@session_required          
def homeadmin(request):
    return render(request,'NavUserAdmin/index.html')
@session_required  
def homestation(request):
    return render(request,'NavUserStation/index.html')