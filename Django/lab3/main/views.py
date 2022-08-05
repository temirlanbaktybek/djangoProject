from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import costomer
from .models import comentator
from .forms import costomerForm
from django.views.generic import DetailView, UpdateView, DeleteView
	

def course(request):
	return render(request, 'main/course.html')


def members(request):
	return render(request, 'main/members.html')
	

def developers(request):
	return render(request, 'main/dev.html')

def index(request):
	return render(request, 'main/index.html')

def phone(request):
	com = comentator.objects.all()
	return render(request, 'main/phone.html', context={'Commentator': com})

def laptop(request):
	com = comentator.objects.all()
	return render(request, 'main/laptop.html', context={'Commentator': com})

def second(request):
	cos = costomer.objects.all()
	return render(request, 'main/second.html', context = {'Costomers': cos})

def login(request):
	return render(request, 'main/login.html')


def create(request):
	eror = ''
	if request.method == "POST":
		form = costomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('second')
		else:
			eror = 'form have error'
	form = costomerForm()

	data = {
		'form': form
	}

	return render(request, 'main/create.html', data)

class DetailView(DetailView):
	model = costomer
	template_name = 'main/detail_view.html'
	context_object_name = 'costomer'

class UpdateView(UpdateView):
	model = costomer
	template_name = 'main/create.html'
	success_url = '/second'
	form_class = costomerForm
 	 	

class DeleteView(DeleteView):
	model = costomer
	success_url ="/second"
	template_name = 'main/delete.html'