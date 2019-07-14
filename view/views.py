from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect  
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
import matplotlib.pyplot as plt
from django.conf import settings
import sqlite3 as db;global name_count
from django.template.defaultfilters import linebreaksbr
from graphs.graph import draw as d1
from hospital.views import get_year,get_month
import datetime

def main(request):
	global fig,plt
	year=18
	set=0
	urls=[]
	data=[]
	if(request.method=="GET"):
		temp=request.GET.get("year")
		if(temp!=None):
			temp=int(temp)
			year=temp-2000
			data=d1(year,int(get_month()))
			set=1				
	year=year+2000
	return render(request,'view_index.html',{'year':year,'set':set,'data':data})

def int_to_month(m):
	months=['jan','feb','mar','apr','may','jun','jul','aug','sup','oct','nov','dec']
	count=1
	for mm in months:
		if(count==m):
			return mm
		count=count+1