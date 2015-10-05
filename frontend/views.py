from django.shortcuts import render_to_response, redirect, render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from sauljohnson.sensitive import CONTACT_FORM_TARGET

def send_contact_mail(name, message, email):
	"""Sends an e-mail submitted through the contact form."""
	send_mail("Website Contact Form Submission",
		"From: " + name + "\n" + message, email, [CONTACT_FORM_TARGET])

def index(request):
	"""Home page"""
	return render_to_response('frontend/index.html', locals())

def blog(request):
	"""Blog page

	I couldn't be bothered with all the write-your-own-blog-engine stuff this
	time around because I'm not that good with Python. Instead there's a little
	CoffeeScript thingy that hooks into Google Blogger and just mirrors that
	stuff here.
	"""
	return render_to_response('frontend/blog.html', locals())

def crisp(request):
	"""Crisp page
	
	Page for my final year project blog. Once again, no blog engine involved.
	"""
	return render_to_response('frontend/crisp.html', locals())
	
def contact(request):
	"""Contact page

	The only real python code block on this entire website.
	"""

	errors = []
	if request.POST:
		try:
			name = request.POST['name']
			email = request.POST['email']
			message = request.POST['message']
			if len(name) < 2:
				errors.append('The name you provide needs to 2 or more characters in length.')
			if len(message) < 30:
				errors.append('The message you submit needs to be 30 or more characters in length.')
			validate_email(email)
			if len(errors) == 0:
				send_contact_mail(name, message, email)
		except ValidationError:
			errors.append('The email address you provided is invalid.')
	return render(request, 'frontend/contact.html', {'success': len(errors) == 0, 'errors': errors, 'post': request.POST})

def terms(request):
	"""Terms page"""
	return render_to_response('frontend/terms.html', locals())

def privacy(request):
	"""Privacy page"""
	return render_to_response('frontend/privacy.html', locals())

def me_and_the_web(request):
	"""Me and the Web page"""
	return render_to_response('frontend/me-and-the-web.html', locals())

def me_and_the_desktop(request):
	"""Me and the Desktop page"""
	return render_to_response('frontend/me-and-the-desktop.html', locals())

# Social

def linkedin(request):
	"""Just redirects to my LinkedIn profile."""
	return redirect('https://www.linkedin.com/profile/view?id=323695094')

# Projects

def silence(request):
	"""Silence project page"""
	return render_to_response('frontend/silence.html', locals())

def brainfony(request):
	"""Brainfony project page"""
	return render_to_response('frontend/brainfony.html', locals())

def flatfolio(request):
	"""Flatfolio project page"""
	return render_to_response('frontend/flatfolio.html', locals())

def denobo(request):
	"""Denobo project page"""
	return render_to_response('frontend/denobo.html', locals())

def veryrss(request):
	"""VeryRSS project page"""
	return render_to_response('frontend/veryrss.html', locals())
