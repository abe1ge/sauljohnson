from django.shortcuts import render_to_response, redirect, render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def index(request):
	return render_to_response('frontend/index.html', locals())

def blog(request):
	return render_to_response('frontend/blog.html', locals())

def contact(request):
	errors = []
	if request.POST:
		try:
			if len(request.POST['name']) < 2:
				errors.append('The name you provide needs to 2 or more characters in length.')
			if len(request.POST['message']) < 30:
				errors.append('The message you submit needs to be 30 or more characters in length.')
			validate_email(request.POST['email'])
		except ValidationError:
			errors.append('The email address you provided is invalid.')
	return render(request, 'frontend/contact.html', {'success': len(errors) == 0, 'errors': errors, 'post': request.POST})

def terms(request):
	return render_to_response('frontend/terms.html', locals())

def privacy(request):
	return render_to_response('frontend/privacy.html', locals())

def login(request):
	return render_to_response('frontend/login.html', locals())

def me_and_the_web(request):
	return render_to_response('frontend/me-and-the-web.html', locals())

def me_and_the_desktop(request):
	return render_to_response('frontend/me-and-the-desktop.html', locals())

# Social

def linkedin(request):
	return redirect('https://www.linkedin.com/profile/view?id=323695094')

# Projects

def silence(request):
	return render_to_response('frontend/silence.html', locals())

def brainfony(request):
	return render_to_response('frontend/brainfony.html', locals())

def flatfolio(request):
	return render_to_response('frontend/flatfolio.html', locals())

def denobo(request):
	return render_to_response('frontend/denobo.html', locals())

def veryrss(request):
	return render_to_response('frontend/veryrss.html', locals())
