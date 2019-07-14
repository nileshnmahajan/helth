from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect  
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from view.forms import ViewForm  
from view.models import Users
import os

import matplotlib.pyplot as plt

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files import File
from view.models import Hospital  
from view.models import Disease  
from view.models import Patient
import sqlite3
# Create your views here.

def main(request):
	return render(request,"admin_index.html",{})
#show all users	
def show(request):
		conn = sqlite3.connect('hos_data.db')
		#con.isolation_level = None
		c = conn.cursor()
		c2 = conn.cursor()
		User = []
		for row in c.execute('select * from users'):
			temp=[]
			for t in row:
				temp.append(t)
			if(str(temp[4])!='None'):
				q='select name from hospital where id='+str(temp[4])
				print (q)
				for row2 in c2.execute(q):
						for t2 in row2:
							temp[4]=t2
			else:
				temp[4]='not asign'
			#print (temp)
			User.append(temp)
		#print (User)	
		hos = Hospital.objects.all() 
		conn.close()
		#return HttpResponse('ok')
		return render(request,"show.html",{'User':User})  

#show all diseases		
def disease(request):
		conn = sqlite3.connect('hos_data.db')
		#con.isolation_level = None
		c = conn.cursor()
		c2 = conn.cursor()
		disease = []
		for row in c.execute('select * from disease'):
				temp=[row[0],row[1]];
				disease.append(temp)
		print (disease)		
		conn.close()		
		return render(request,"disease.html",{'disease':disease})  

		
def edit_disease(request, id):  
		conn = sqlite3.connect('hos_data.db')
		#con.isolation_level = None
		c = conn.cursor()
		n=request.POST.get('dname')
		q ="select * from disease where id = "+str(id)
		disease=[]
		for dsg in c.execute(q):
			disease=dsg
		conn.close()
		return render(request,"edit_disease.html",{'disease':disease})

		
def update_disease(request, id):  
		conn = sqlite3.connect('hos_data.db')
		#con.isolation_level = None
		c = conn.cursor()
		n=request.POST.get('dname')
		q="UPDATE disease set dname='"+n+"' where id = "+str(id)
		c.execute(q)
		conn.commit()
		conn.close()
		return redirect("/administrator/disease")  
def edit(request, id):  
        User = Users.objects.get(id=id)  
        return render(request,'edit.html', {'User':User})  
def update(request, id):  
		conn = sqlite3.connect('hos_data.db')
		#con.isolation_level = None
		c = conn.cursor()
		u=request.POST.get('username')
		q='select id from users where username="'+u+'"'
		count=0
		u2=''
		#check whether another user present with same username
		for row in c.execute(q):
			u2=row[0]
			print (row)
			count=count+1
			print(count)
		if(u2==id):
			#username not change by user
			count=0
		if count!=0:
			#another user same username found
			User = Users.objects.get(id=id)  
			return render(request,'edit.html', {'User':User,'user':1})
		#no any error it now get updated
		p=request.POST.get('password')	
		e=request.POST.get('email')	
		#!/usr/bin/python
		q="UPDATE users set username='"+u+"', password = '"+p+"', email ='"+e+"' where id = "+str(id)
		print (q)
		c.execute(q)
		conn.commit()
		conn.close()
		return redirect("/administrator/show")  

def destroy(request, id):  
        User = Users.objects.get(id=id)  
        User.delete()  
        return redirect("/administrator/show")
		
