
from django.shortcuts import render
from .forms import ProductForm,RawProductForm
from .models import products
#def products_create_view(request):
#	my_form=RawProductForm()
#	if request.method=="POST":
#		my_form=RawProductForm(request.POST)
#		if my_form.is_valid():
#			print(my_form.cleaned_data)
#			products.objects.create(title=my_new_title)
#		else:
#			print(my_form.errors)
#	context={		'form': my_form
#	}
#	return render(request,"create.html",context)		






#def products_create_view(request):
#    if request.method=="POST":
#    	my_new_title=request.POST.get('title')
#    	print(my_new_title)
#    context={}
#    return render(request,"create.html",context)
def render_initial_data(request):
	initial_data={
	    'title': "this is my new title"
	}
	obj=products.objects.get(id=1)
	form=ProductForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
	context={
	'form': form
	}
	return render(request,"create.html",context)


def products_create_view(request):
	form=ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=ProductForm()

	context={
	'form': form
	}
	return render(request,"create.html",context)
def products_detail_view(request):
   obj=products.objects.get(id=1)
   context={
   'objects':obj
   }			
   return render(request,"detail.html",context)


  







