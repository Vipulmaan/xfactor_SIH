from django.shortcuts import render
from .models import house,hospital,doctor,issue
import gpxpy.geo

def issues_view(request):
	if request.method =="GET":
		issues_list = issue.objects.all().order_by('timestamp')
		return render(request,'issue.html',{'issue':issues_list})
	else:
		obj = issue.objects.get(house_id=request.POST['house_id'])
		obj.statusupdate()
		obj.save()
		issues_list = issue.objects.all().order_by('timestamp')
		return render(request,'issue.html',{'issue':issues_list})




def home1(request):
	if request.method == "POST":
		obj1 = house.objects.get(house_id=request.POST['h_id'])
		all_objs = hospital.objects.all()
		hos =[]
		for x in all_objs:
			dist = gpxpy.geo.haversine_distance(obj1.latitude,obj1.longitude,x.latitude,x.longitude)
			hos.append((x.H_id,x.H_name,dist/1000.0,x.mobile,x.H_address))	
		hos = sorted(hos,key=lambda x: x[2])
		return render(request,'hospital.html',{'hospitals':hos})
	else :
		return render(request,'hospital.html',{})

def home(request):
	if request.method == "POST":
		obj1 = house.objects.get(house_id=request.POST['h_id'])
		all_objs = doctor.objects.filter(specialist=request.POST['spec'])
		hos =[]
		for y in all_objs:
			x = hospital.objects.get(H_id = y.H_id)
			dist = gpxpy.geo.haversine_distance(obj1.latitude,obj1.longitude,x.latitude,x.longitude)
			hos.append((x.H_id,x.H_name,dist/1000.0,x.mobile,x.H_address,y.D_name,y.time_start,y.time_end,y.mobile))	
		hos = sorted(hos,key=lambda x: x[2])
		return render(request,'hospital.html',{'hospitals':hos})
	else :
		return render(request,'hospital.html',{})				





