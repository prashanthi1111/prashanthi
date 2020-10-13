
from django.shortcuts import render
from .models import products
from .forms import ProductForm
def products_create_view(request):
	context={}
	return render(request,"create.html",context)

#def products_create_view(request):
	#form=ProductForm(request.POST or None)
	#if form.is_valid():
	    #form.save()
	    #form=ProductForm()
	#context={
	#'form': form
	#}
	#return render(request,"create.html",context)
def products_detail_view(request):
	obj=products.objects.get(id=1)
	context={
	#'objects': obj
	}
	return render(request,"detail.html",context)


  







