from django.shortcuts import render_to_response, redirect

def index(request):
	return render_to_response('frontend/index.html', locals())

def contact(request):
	return render_to_response('frontend/contact.html', locals())

def terms(request):
	return render_to_response('frontend/terms.html', locals())

def privacy(request):
	return render_to_response('frontend/privacy.html', locals())

def login(request):
	return render_to_response('frontend/login.html', locals())	

def linkedin(request):
	return redirect('https://www.linkedin.com/profile/view?id=323695094')