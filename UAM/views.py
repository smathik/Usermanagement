# Create your views here.
from django.shortcuts import render


def approverlogin(request):
	if request.method=='POST':
		print '>>>>>>'
		# username = 'admin'
		# password = 'Symc@123'
		username=request.POST['username']
		password=request.POST['password']
		print username,password
	return render(request,'login.html')
