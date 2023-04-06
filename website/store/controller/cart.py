from django.shortcuts import *
from django.contrib import messages
from django.http import JsonResponse

from store.models import Product, Cart

def addtocart(request):
    if request.method == 'POST':        
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':"Product Already in Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty :
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status':"Product added Successfully"})
                    else:
                        return JsonResponse({'status':"Only" + str(product_check) +" quantity available"})
            else:
                return JsonResponse({'status':"No Such Product Found"})
        else:
            return JsonResponse({'status':"Login to Continue"})    
    return redirect('/')


# cart section started.....................


def viewcart(request):
    cart = Cart.objects.filter(user = request.user)
    # qty = Cart.objects.filter('product_qty')
    print(cart)
    context = {'cart': cart}
    return render(request,"store/products/cart.html",context)
