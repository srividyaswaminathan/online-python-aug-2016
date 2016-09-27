from django.shortcuts import render, redirect
from .models import Product
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	#show all products select * from products
	if request.method== "GET":
		context = {
					'all_products': Product.objects.all()
		}
		for product in Product.objects.all():
			print product.product_name

		return render(request, 'semi_restful_app/product_index.html', context)
	if request.method == "POST":
		return create(request)	

def new(request):
	#display form to create a new products
	return render(request, 'semi_restful_app/product_new.html' )
	

def create(request):
	#create a new product
	if request.method == "POST":
		new_product = Product.objects.create(product_name=request.POST['name'], product_description=request.POST['description'], product_price=request.POST['price'])
		return redirect(reverse('index'))

def show(request, id):
	#display a specific product should be done w.r.t specific id
	product_in_db = Product.objects.get(id=id)
	context = { 
				'product_in_db': product_in_db,

	        }
	return render(request, 'semi_restful_app/product_show.html' , context)

def edit(request, id):
	edit_product = Product.objects.get(id=id)
	context = { 
				'edit_product': edit_product
	   }

	return render(request, 'semi_restful_app/product_edit.html', context)
	

def update(request, id):
	#update a specific product put
	if request.method =="POST":
		print request.POST
		Product.objects.filter(id=id).update(product_name=request.POST['product_name'], product_description=request.POST['product_description'], product_price=request.POST['product_price'])
		update_product = Product.objects.get(id=id)
		context = {  
	 				'product_in_db': update_product
		          }
		return render(request, 'semi_restful_app/product_show.html' , context)
	if request.method== "GET":
		return show(request)	

def destroy(request, id):
	#delete a specific product w.re.t id delete
	Product.objects.get(id=id).delete()
	return redirect('index')					


