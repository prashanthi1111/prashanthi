from django import forms
from .models import products
class ProductForm(forms.ModelForm):
	class Meta:
	    model=products
	    fields = [
	       'title',
	       'description',
	       'price'
		]
class RawProductForm(forms.Form):
    title=forms.CharField(label=' ',widget=forms.TextInput(attrs={"placeholder":"your text"}))
    description=forms.CharField(
    	required=False,
    	widget=forms.Textarea(
    		attrs={
    		"placeholder":"your description",
    		"class":"new-class-name-two",
    		"id":"my-id-for-text-area",
    		"rows":20,
            "cols":120
            }
    	)
    	
    )
    		
    price=forms.DecimalField(initial=100.99)