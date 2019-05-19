from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic



def index(request):
	return render(request, 'index.html',)

def blog(request):
	return render(request, 'blog.html')

def about(request):
	return render(request, 'about.html')

def post(request):
	#posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'post.html')
			
def contact(request):
	return render(request, 'contact.html')
