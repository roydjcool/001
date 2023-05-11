from django.shortcuts import *
from django.contrib import messages
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from store.models import *

@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'store/wishlist.html', context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check =Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':"Product Already Added"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':"Product Added"})
            else:
                return JsonResponse({'status':"No Such product Found"})
        else:
            return JsonResponse({'status': "Login To Continue"}) 
    return redirect('/')

