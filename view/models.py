from django.db import models
# Create your models here.

	
class Users(models.Model):  
	username=models.TextField()
	email=models.TextField()
	password=models.TextField()
	Hos_id=models.IntegerField()

	class Meta:  
		db_table = "Users"

class Hospital(models.Model):  
	NAME=models.TextField()
	location=models.TextField()
	class Meta:  
		db_table = "Hospital"
		
class Disease(models.Model):  
	dname=models.TextField()
	class Meta:  
		db_table = "Disease"
	

		 
class Patient(models.Model):  
	year=models.TextField()
	month=models.TextField()
	gender=models.TextField()
	hospital_id=models.TextField()
	disease_id=models.TextField()
	quntity=models.TextField()
	class Meta:  
		db_table = "Patient"
		
		
		