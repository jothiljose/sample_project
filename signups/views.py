from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core import serializers
from django.http import HttpResponse
from signups.models import SignUp
from django.shortcuts import get_object_or_404






# Create your views here.

# def signup(request):
# 	return TemplateResponse(request, "signup.html", 
# 								context_instance=RequestContext(request))
def signup(request,id):
	# data = SignUp.objects.all()
	# data = SignUp.objects.filter(first_name = 'manu')
	# data = SignUp.objects.get(id = id)
	data = get_object_or_404(SignUp,id = id)
	
	my_str = "This is my string"
	return TemplateResponse(request, "videos/signup.html", {"data":data})

def signup2(request):
	data = SignUp.objects.all()
	data = serializers.serialize('xml',data)

	return HttpResponse(data,content_type="application/xml")
 