from django.shortcuts import render
from random import randint
import random
import datetime
from django.http import HttpResponse , HttpResponseRedirect  
from django.shortcuts import render, redirect  
import os
import matplotlib.pyplot as plt
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files import File
import datetime  
from view.models import Users
import sqlite3 as db
from hospital.forms import formView as LoginForm
# from matplotlib import pylab
# from pylab import *
# import PIL, PIL.Image
import io
import numpy as np

def index(request):
    return HttpResponse('ok')
	

#hospital main page 	
def main(request):  
		username=0
		if(request.session.has_key('username')):
			if request.session['username']!=0:
				username=request.session['username']
		return render(request,'hospital_index.html',{'username':username})  

#global matplotlib instance		
fig = plt.figure()
			
#for specific login hospital show them their data on monthly basis			
def view_data(request):
		show=0
		min=0
		max=0
		selected=''
		dis=[]
		if (is_login(request)):#is user not login
			return render(request, 'loggedin.html', {"username" : 0})
		if request.method == "POST":  
			month=request.POST.get('month')
			year=request.POST.get('year')
			selected='showing data of year '+str(year)+' and month '+str(month)
			month=month_to_int(month)
			name='data/hos_patient_data_year_'+str(year)+'.db'
			conn = db.connect(name)
			conn2 = db.connect('hos_data.db')
			c = conn.cursor()
			c2 = conn2.cursor()
			u=request.session['id']#it has store user id while login
			q='select dis_id, male,female from patient where hos_id='+str(u)+' and month = '+str(month)
			for row in c.execute(q):
				temp=[row[0],row[1],row[2]]
				q2='select dname from disease where id='+str(row[0])
				for row2 in c2.execute(q2):
					temp[0]=row2[0]
				dis.append(temp)	
			conn.close()
			show=1	
		year=reversed(range(1,19))
		months=['jan','feb','mar','apr','may','jun','jul','aug','sup','oct','nov','dec']
		username=''
		if request.session.has_key('username'):
			if request.session['username']==0:
				username=0;
			else:
				username=request.session['username']
		return render(request,'view_data.html',{'years':year,'months':months,'data':dis,'show':show,'selected':selected,"username" : username})

#for int to string months name convertion
def month_to_int(m):
	months=['jan','feb','mar','apr','may','jun','jul','aug','sup','oct','nov','dec']
	count=1
	for mm in months:
		print(mm,' = ',m)
		if(mm==m):
			return count
			
		count=count+1
		

def get_month():
	now = datetime.datetime.now()
	return str(now.month)
	
def get_year():
	now = datetime.datetime.now()
	return str(now.year)[2:]
	
def get_hos_id(request):
	return str(request.session['hos_id'])
def get_id(request):
	return str(request.session['id'])	
	
def get_username(request):
	return str(request.session['username'])
#for adding monthly data of each hospital		
def add_data(request):
	global month,year,hosid	
	if (is_login(request)):#is user not login
			return render(request, 'loggedin.html', {"username" : 0})
	username=request.session['username']
	name='data/hos_patient_data_year_'+get_year()+'.db'
	conn=db.connect(name)
	c=conn.cursor()
	m=get_month()
	hos_id=get_hos_id(request)
	#user not submitted hospital
	if(hos_id=='None'):
		help='this hospital is geting link to your id'
		selected=' fill your hospital details below '
		error=''
		return render(request,'add_new_hospital.html',{"username" : username,'disease':0,'selected':selected,'help':help,'error':error})  
	q='select count(id) from patient where hos_id='+hos_id+' and month = '+m+''
	count=''
	for row in c.execute(q):
		count=row[0]
	if(count>0):
		help='data of this month is allready submitted'
		selected=' data of year '+str(2018)+' and month september of diseases '+str(count)+' allready submitted'
		return render(request,'add_new_data.html',{"username" : username,'disease':0,'selected':selected,'help':help})  
#form is submitting	
	
	if request.method == "POST": 
		conn=db.connect('data/hos_patient_data_year_18.db')
		c=conn.cursor()
		count=0

		hos_id=str(request.session['id'])
		for disease in range (1,99):
			month='9'
			mn='m'+str(disease)
			fn='f'+str(disease)
			male=str(request.POST.get(mn))
			female=str(request.POST.get(fn))
			if (male!='' and male.isdigit() and female !='' and female.isdigit()):
				count=count+1
				q="insert into patient(month,hos_id,dis_id,male,female) values (?,?,?,?,?)"
				q2=(month,hos_id,disease,male,female)
				c.execute(q,q2)
		conn.commit()
		conn.close()
		help='your records of this months are submitted recently by you \nthere is only once in month records can be submitted \nfor any query contack admin@kk.com'
		selected=' data of year '+str(2018)+' and month september of diseases '+str(count)+' submitted successfully'
		return render(request,'add_new_data.html',{"username" : username,'disease':0,'selected':selected,'help':help})  
#show form for add data
	disease=[]
	selected='enter data of year '+str(2018)+' and month september'
	conn=db.connect('hos_data.db')
	c=conn.cursor()
	help='add record in integer format without space \n if not record of specific disease keep it blank dont asign any value to it and click submit button once'
	for row in 	c.execute('select id,dname from disease'):
		disease.append([row[0],row[1]])
	
	return render(request,'add_new_data.html',{"username" : username,'disease':disease,'selected':selected,'help':help})  	
def add_hospital(request):

	
	conn=db.connect('hos_data.db')
	c=conn.cursor()
	name=request.POST.get('h_name')
	location=request.POST.get('h_location')
	q='select count(*) from hospital where NAME="'+name+'" and location ="'+location+'"'
	count=0
	for row in c.execute(q):
		count=row[0]
		#if same hospital is exist
		
	if(count>0):
		print("same hospital found")
		help='data of this month is allready submitted'
		error='same hospital present in recors'
		selected=' data of year '+str(2018)+' and month september of diseases '+str(count)+' allready submitted'
		return render(request,'add_new_hospital.html',{'error':1})
	print("same hospital not found")
	q1='insert into hospital(NAME,location) values(?,?)'
	q2=(name,location);
	c.execute(q1,q2)
	conn.commit()
	print ("inserted new hospital in db as",name,location)
	q='select id from hospital where NAME="'+name+'" and location ="'+location+'"'
	hos_id=''
	for row in c.execute(q):
		hos_id=row[0]#geting hos id for save in user account
	user_id=request.session['signup_id']
	q='update users set hos_id = '+str(hos_id)+' where id = '+str(user_id)
	c.execute(q)
	conn.commit()
	conn.close()
	return render(request, 'loggedin.html', {"username" : 0})	
	
def profile(request):  
		if (is_login(request)):#is user not login
			return render(request, 'loggedin.html', {"username" : 0})
		User=get_username(request) 
		conn=db.connect('hos_data.db')
		id=get_id(request);
		c=conn.cursor()
		data=[]
		q='select * from users where id='+id
		for row in c.execute(q):
			data.append(row[1]);data.append(row[3]);data.append(row[2]);data.append(row[4])
		q='select * from hospital where id='+str(data[3])
		for row in c.execute(q):
			data[3]=row[1]
			data.append(row[2])
		conn.close()
		help='this is information about login creditional contact and address'
		return render(request,'profile.html',{'User':User,'data':data,'help':help})	
		
def signup(request):  
	if request.method == "POST":  
		u=request.POST.get('username')
		p=request.POST.get('password')	
		e=request.POST.get('email')	
		conn = db.connect('hos_data.db')
		#con.isolation_level = None
		c = conn.cursor()
		#create table for store hospitals data
		q='select * from users where username="'+u+'"'
		count=0
		for row in c.execute(q):
			count=count+1
		if count==0:
			#not same username user present
			q="insert into users(username,email,password) values(?,?,?)"
			q2=(u,e,p)
			c.execute(q,q2)
			print("signup success as username and email ",u,e)
			id=0
			for row in c.execute(q):
				id=row[0]
			request.session['signup_id']=id
			conn.commit()	
			conn.close()
			#success		
			return render(request,'add_new_hospital.html',{'error':0})
		else:
			return render(request,'signup.html',{'email':1})  

	return render(request,'signup.html',{})  


def login_check(request):
	if request.method == 'GET' and request.GET.get('x')=='1':
		request.session['username']=0
		return render(request, 'loggedin.html', {"username" : 0})
		#LOGOUT
	elif request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		#LOGIN
		if(validate_login(request,username,password)):
		#return if login success
			request.session['username'] = username
			return render(request, 'hospital_index.html', {"username" : username})
		else:
			request.session['username'] = 0
			return render(request, 'loggedin.html', {"username" : 0,"invalid":1})
	elif request.session.has_key('username'):
		if request.session['username']==0:
			return render(request, 'loggedin.html', {"username" : 0})
			#PRIVIUS LOGIN IS LOGED OUT
		else:
			#user still login
			username = request.session['username']
			return render(request, 'hospital_index.html', {"username" : username})
	else:
		return render(request, 'loggedin.html', {"username" : 0})

		
		
def validate_login(request,u,p):
		conn = db.connect('hos_data.db')
		#con.isolation_level = None
		c = conn.cursor()

		q ="select * from users where username = '"+str(u)+"' and password = '"+str(p)+"'";
		count=0
		id=0
		hos_id=0
		for row in c.execute(q):
			count=count+1
			hos_id=row[4]
			id=row[0]
		request.session['id'] = id		
		request.session['hos_id'] = hos_id
		print('login success as ',id,hos_id);
		conn.close()	
		if(count==0):
			return 0
		else:
			return 1
			
			
def is_login(request):
	if(request.session.has_key('username')):
		if request.session['username']==0:
			#recently logout
			return 1
		else:
			#still login
			return 0
	else:
		#not login
		return 1
def int_to_month(m):
	months=['jan','feb','mar','apr','may','jun','jul','aug','sup','oct','nov','dec']
	count=1
	for mm in months:
		if(count==m):
			return mm
		count=count+1