from django.shortcuts import render_to_response, render

def index(request):
  return render_to_response('blog/index.html', locals())
