"""evcharging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('news',views.news,name='news'),
    path('contact',views.contact,name='contact'),
    path('loginsignup',views.loginsignup,name='loginsignup'),
    path('login',views.login,name='login'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('stationlogin',views.stationlogin,name='stationlogin'),
     path('navigator',views.navigator,name='navigator'),
      path('station',views.station,name='station'),
       path('navhome',views.navhome,name='navhome'),
       path('signup',views.signup,name="signup"),
       path('usersignup',views.usersignup,name="usersignup"),
       path('booking',views.booking,name="booking"),
       path('profile',views.profile,name="profile"),
       path('manageuser',views.manageuser,name="manageuser"),
       path('manageusers',views.manageusers,name="manageusers"),
         path('stationedit/<int:value>/',views.stationedit,name="stationedit"),
path('addstation',views.addstation,name="addstation"),
path('addstationdetails',views.addstationdetails,name="addstationdetails"),
path('addstationdetailsupdate',views.addstationdetailsupdate,name="addstationdetailsupdate"),
path('deletestations/<int:value>/',views.deletestations,name="deletestations"),
path('stationview',views.stationview,name="stationview"),
path('viewbooking',views.viewbooking,name="viewbooking"),
path('viewbookingstation',views.viewbookingstation,name="viewbookingstation"),
path('userpayment',views.userpayment,name="userpayment"),
path('checkstation',views.checkstation,name="checkstation"),

path('bill/<int:value>/',views.bill,name="bill"),
path('completecharging',views.completecharging,name="completecharging"),
path('earning',views.earning,name="earning"),
path('earningstation',views.earningstation,name="earningstation"),
path('totalearning',views.totalearning,name="totalearning"),
path('bookingev',views.bookingev,name="bookingev"),
path('adminbookingev',views.adminbookingev,name="adminbookingev"),
path('bookingevadmin',views.bookingevadmin,name="bookingevadmin"),
path('passwordchangestation',views.passwordchangestation,name="passwordchangestation"),

path('updatepasswordstation',views.updatepasswordstation,name="updatepasswordstation"),

path('ristrict/<int:value>/',views.ristrict,name="ristrict"),
path('unristrict/<int:value>/',views.unristrict,name="unristrict"),
path('deleteuserstation/<int:value>/',views.deleteuserstation,name="deleteuserstation"),
path('deleteuser/<int:value>/',views.deleteuser,name="deleteuser"),

path('bookingevdone/<int:value>/',views.bookingevdone,name="bookingevdone"),
path('cancelbookingev/<int:value>/',views.cancelbookingev,name="cancelbookingev"),
path('filter',views.filter,name="filter"),
path('filterstation',views.filterstation,name="filterstation"),
path('filterdistance',views.filterdistance,name="filterdistance"),
path('filterdistancestation',views.filterdistancestation,name="filterdistancestation"),

path('getstation',views.getstation,name="getstation"),
path('logout',views.logout,name="logout"),
path('stationloginuser',views.stationloginuser,name="stationloginuser"),

path('loginstationuser',views.loginstationuser,name='loginstationuser'),

path('navhomeadmin',views.navhomeadmin,name='navhomeadmin'),
path('navigatoradmin',views.navigatoradmin,name='navigatoradmin'),
path('stationadmin',views.stationadmin,name='stationadmin'),
path('bookingadmin',views.bookingadmin,name='bookingadmin'),
path('profileadmin',views.profileadmin,name='profileadmin'),


#station
path('navhomestation',views.navhomestation,name='navhomestation'),
path('navigatorstation',views.navigatorstation,name='navigatorstation'),
path('stationstation',views.stationstation,name='stationstation'),
path('bookingstation',views.bookingstation,name='bookingstation'),
path('profilestation',views.profilestation,name='profilestation'),


]
