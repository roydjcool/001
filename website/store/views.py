from django.shortcuts import *
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "store/index.html")


def collections(request):
    category = Category.objects.filter(status=0)
    context =  {'category':category}
    return render(request, "store/collections.html", context)

def collectionsview(request, slug):
    if Category.objects.filter(slug=slug, status=0):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category':category}
        return render(request, "store/products/index.html", context)
    else:
        messages.warning(request, "No Category Found")
        return redirect('collections')
    
# def subcateview(request):
#     categories = Category.objects.all()
#     selected_category_id = request.GET.get('category')
#     if selected_category_id:
#         items = Category.objects.filter(category=selected_category_id)
#     else:
#         items = Category.objects.all()
#     context = {
#         'categories': categories,
#         'selected_category_id': selected_category_id,
#         'items': items,
#     }
#     return render(request, 'men.html', context)

def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}            
        else:
            messages.error(request, "No product Found")
            return redirect('collections')
    else:
        messages.error(request, "No Category Found")
        return redirect('collections')
    return render(request, "store/products/view.html", context)