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

def me_and_the_web(request):
	return render_to_response('frontend/me-and-the-web.html', locals())

# Projects

def silence(request):
	return render_to_response('frontend/silence.html', locals())	

def brainfony(request):
	return render_to_response('frontend/brainfony.html', locals())	

def flatfolio(request):
	return render_to_response('frontend/flatfolio.html', locals())	

def denobo(request):
	return render_to_response('frontend/denobo.html', locals())	