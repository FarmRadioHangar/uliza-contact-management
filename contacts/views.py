from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
	#query_list = ..............
	template = loader.get_template('contacts/home.html')
	#context = {'m_query_list': query_list,}
	#return HttpResponse(template.render(template.render(context, request))
	return HttpResponse(template.render(None, request)) #render(request, 'contacts/home.html', context)

def role(request):
	template = loader.get_template('contacts/role.html')
	return HttpResponse(template.render(None, request))

def detail(request):
	template = loader.get_template('contacts/detail.html')
	return HttpResponse(template.render(None, request))

def contact(request):
	template = loader.get_template('contacts/contact.html')
	return HttpResponse(template.render(None, request))
#def detail(request, contact_id):
	#try:
		#contact = getcontact
	#except Contact.DoesNotExist:
		#raise Http404('Contact does not exist')
	#return render(request, 'contacts/detail.html', {'contact':contact})
#	pass
		
