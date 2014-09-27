from django.shortcuts import render_to_response

def index(request):
	return render_to_response('frontend/index.html', locals())

def contact(request):
	return render_to_response('frontend/contact.html', locals())