from django.shortcuts import render
from .models import house,hospital,doctor,issue
import gpxpy.geo

def search_view(request):
	if request.method =="GET":
		return render(request,'search.html',{})
	else:
		issues_list = issue.objects.filter(house_id=request.POST['h_id']).order_by('-timestamp','status')
		return render(request,'search.html',{'issue':issues_list})

def issues_view(request):
	if request.method =="GET":
		issues_list = issue.objects.all().order_by('-timestamp','status')
		x=issue.objects.all().count
		y=issue.objects.filter(status=3).count
		z=issue.objects.filter(status=2).count
		q=issue.objects.filter(status=1).count
		return render(request,'issue.html',{'issue':issues_list[:10],'X':x,'Y':y,'Z':z,'Q':q})
	else:
		obj = issue.objects.get(id=request.POST['issue_id'])
		obj.statusupdate()
		obj.save()
		issues_list = issue.objects.all().order_by('-timestamp','status')
		x=issue.objects.all().count
		y=issue.objects.filter(status=3).count
		z=issue.objects.filter(status=2).count
		q=issue.objects.filter(status=1).count
		return render(request,'issue.html',{'issue':issues_list[:10],'X':x,'Y':y,'Z':z,'Q':q})

def issuelist_view(request):
	if request.method =="GET":
		issues_list = issue.objects.all().order_by('-timestamp','status')
		return render(request,'issue_list.html',{'issue':issues_list})
	else:
		obj = issue.objects.get(id=request.POST['issue_id'])
		obj.statusupdate()
		obj.save()
		issues_list = issue.objects.all().order_by('-timestamp','status')
		return render(request,'issue_list.html',{'issue':issues_list})

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
			hos.append((x.H_id,x.H_name,float("%0.2f" %(dist/1000.0)),x.mobile,x.H_address,y.D_name,y.time_start,y.time_end,y.mobile,request.POST['spec']))	
		hos = sorted(hos,key=lambda x: x[2])
		return render(request,'hospital.html',{'hospitals':hos})
	else :
		return render(request,'hospital.html',{})				





