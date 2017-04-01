from django.db import models

class issue(models.Model):
	house_id = models.IntegerField()
	Detail = models.CharField(max_length=1000)
	status = models.IntegerField(default=1)
	timestamp = models.DateTimeField()

	def statusupdate(self):
		self.status+=1

	def __str__(self):
		return self.Detail

class house(models.Model):
	house_id = models.IntegerField()
	latitude = models.FloatField()
	longitude = models.FloatField()
	members = models.IntegerField(default=1)

	def __str__(self):
		return str(self.house_id) 

class hospital(models.Model):
	H_id = models.IntegerField()
	H_name = models.CharField(max_length=50)
	latitude = models.FloatField()
	longitude = models.FloatField()
	mobile = models.CharField(max_length=11)
	H_address = models.CharField(max_length=250)

	def __str__(self):
		return self.H_name +"   " + self.H_address
class doctor(models.Model):
	H_id = models.IntegerField()
	D_name = models.CharField(max_length=50)
	specialist = models.CharField(max_length=100)
	mobile = models.CharField(max_length=11)
	time_start = models.TimeField(auto_now=False)
	time_end = models.TimeField(auto_now=False)

	def __str__(self):
		return self.D_name +" - "+self.specialist
