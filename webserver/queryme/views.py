from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .query import qry
from .query import mlt
from .query import mfd
from .query import setTheme

# Create your views here.
def index(request):
	return search(request)
	#HttpResponse("Hello, world. Queryme speaking.")
	
#default search wills earch documents
def search(request):
	query = request.GET.get('query', '')
	start = request.GET.get('start', '')
#	if(not start):
#		start = 1
	return JsonResponse({'results': qry(query, 'doc', start)})
    
def search_exp(request):
	query = request.GET.get('query', '')
	start = request.GET.get('start', '')
	return JsonResponse({'results': qry(query, 'exp', start)})
    
def search_auth_docs(request):
	query = request.GET.get('query', '')
	author = request.GET.get('start', '')
	return JsonResponse({'results': qry(query, 'auth_docs', author)})

def recommend(request):
	query = request.GET.get('query', '')
	size = request.GET.get('size', '')
	return JsonResponse({'results': mlt(query, size)})
	
def domainsearch(request):
	query = request.GET.get('query', '')
	size = request.GET.get('size', '')
	domain = request.GET.get('domain', '')
	return JsonResponse({'results': mfd(query, domain, size)})
	
def theme(request):
	themeid = request.GET.get('theme', '')
	return JsonResponse({'results': setTheme(themeid)})