from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.core.urlresolvers import reverse
from .forms import RoleForm, DetailForm
from .models import Role as RoleModel
from collections import namedtuple
import logging
import requests
import json

url = 'http://0.0.0.0:3000/api/v1/content/' #Test url

def home(request):
	#query_list = ..............
	template = loader.get_template('contacts/home.html')
	#context = {'m_query_list': query_list,}
	#return HttpResponse(template.render(template.render(context, request))
	return HttpResponse(template.render(None, request)) #render(request, 'contacts/home.html', context)

def role(request):
	template = loader.get_template('contacts/role.html')
	role_url = url + 'roles/'
	try:
		response = requests.get(role_url)
		#role_list = json.loads(response.content, object_hook=lambda d:namedtuple('R', d.keys())(*d.values()))
       		#m_list = {'listener', 'broadcastor', 'others'}
		role_list = json.loads(response.content)
		context = Context({'m_role_list': role_list})
		return HttpResponse(template.render(context, request))
	except requests.ConnectionError:
		logging.exception('Server connection failed')
		return HttpResponse(template.render(None, request))

def add_role(request):
	role_url = url + 'roles/'
	if request.method == 'POST':
		form = RoleForm(request.POST)
		if form.is_valid():# Validate form data
			#name = form.cleaned_data['name']
			#desc = form.cleaned_data['description']
			try:
				requests.post(role_url, form.cleaned_data)
			except requests.ConnectionError as ex:
				logging.exception('Server connection failed')
	else:
		form = RoleForm()
	return render(request, 'contacts/add_role.html', {'form':form})

def detail(request):
	template = loader.get_template('contacts/detail.html')
	detail_url = url + 'details/'
	try:
		response = requests.get(detail_url)
		detail_list = json.loads(response.content)
		context = Context({'m_detail_list': detail_list})
		return HttpResponse(template.render(context, request))
	except requests.ConnectionError:
		logging.exception('Server connection failed')
		return HttpResponse(template.render(None, request))

def add_detail(request):
	detail_url = url + 'details/'
	if request.method == 'POST':
		form1 = DetailForm(request.POST)
		if form1.is_valid(): #Validate data
			#Post to coresponding api
			try:
				requests.post(detail_url, form1.cleaned_data)
			except requests.ConnectionError:
				logging.exception('Server connection failed')
	else:
		form1 = DetailForm
	return render(request, 'contacts/add_detail.html', {'form':form1})

def contact(request):
	template = loader.get_template('contacts/contact.html')
	contact_url = url + 'contact_details/'
	try:
		response = requests.get(contact_url)
		contact_list = json.loads(response.content)
		context = Context({'m_contact_list', request})
		return HttpResponse(template.render(context, request))
	except requests.ConnectionError:
		logging.exception('Server connection failed')
		return HttpResponse(template.render(None, request))

def add_contact(request):
	template = loader.get_template('contacts/add_contact.html')
	contact_url = url + 'contact_details/'
	#if request.method == 'POST':
	#	return HttpResponseRedirect(reverse('uliza-contact'))
	return HttpResponse(template.render(None, request))


#def detail(request, contact_id):
	#try:
		#contact = getcontact
	#except Contact.DoesNotExist:
		#raise Http404('Contact does not exist')
	#return render(request, 'contacts/detail.html', {'contact':contact})
#	pass
		
