
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, AnonymousUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import JsonResponse
import json
# Create your views here.



def index(request):


    try:
        customer = request.user.customer
    except:
        device = str(AnonymousUser)
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cartItems = order.get_cart_items
    products = Product.objects.filter(is_featured=True).order_by('-id')
    newproducts = Product.objects.filter(is_new=True).order_by('-id')
    data = Brand.objects.all().order_by('-id')[:4]

    
    context = {  'cartItems':cartItems, 'products':products, 'newproducts':newproducts, 'data':data }

    return render(request, 'index.html', context)


def men(request):

    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    products = Product.objects.filter(is_man=True).order_by('-id')
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    brands = Brand.objects.all().order_by('-id')
    accessoriess = Accessories.objects.all().order_by('-id')

    sizes = Size.objects.all().order_by('-id')

    accessoriesId = request.GET.get("accessories")
    brandId = request.GET.get("brand")
    if accessoriesId:
        products = Product.objects.filter(accessories=accessoriesId , is_man=True).order_by('-id')
  
    elif brandId:
        products = Product.objects.filter(brand=brandId , is_man=True).order_by('-id')


    else:
        products = Product.objects.filter(is_man=True).order_by('-id')



    context = {'products':products, 'cartItems':cartItems, 'brands':brands, 'accessoriess':accessoriess, 'sizes':sizes}

    return render(request, 'men.html', context)


def women(request):

    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    products = Product.objects.filter(is_women=True).order_by('-id')
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    brands = Brand.objects.all().order_by('-id')
    accessoriess = Accessories.objects.all().order_by('-id')

    sizes = Size.objects.all().order_by('-id')

    accessoriesId = request.GET.get("accessories")
    brandId = request.GET.get("brand")

    if accessoriesId:
        products = Product.objects.filter(accessories=accessoriesId , is_women=True).order_by('-id')
  
    elif brandId:
        products = Product.objects.filter(brand=brandId , is_women=True).order_by('-id')


    else:
        products = Product.objects.filter(is_women=True).order_by('-id')



    context = {'products':products, 'cartItems':cartItems, 'brands':brands, 'accessoriess':accessoriess, 'sizes':sizes}

    return render(request, 'women.html', context)

def kids(request):
    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    products = Product.objects.filter(is_kid=True).order_by('-id')
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    brands = Brand.objects.all().order_by('-id')
    accessoriess = Accessories.objects.all().order_by('-id')

    sizes = Size.objects.all().order_by('-id')

    accessoriesId = request.GET.get("accessories")
    brandId = request.GET.get("brand")

    if accessoriesId:
        products = Product.objects.filter(accessories=accessoriesId , is_kid=True).order_by('-id')
  
    elif brandId:
        products = Product.objects.filter(brand=brandId , is_kid=True).order_by('-id')


    else:
        products = Product.objects.filter(is_kid=True).order_by('-id')



    context = {'products':products, 'cartItems':cartItems, 'brands':brands, 'accessoriess':accessoriess, 'sizes':sizes}

    return render(request, 'kids.html', context)


def brand(request):


    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    data = Brand.objects.all().order_by('-id')


    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems, 'data':data}

    return render(request, 'brand.html', context)


def brandList(request, brand_id):


    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    accessoriess = Accessories.objects.all().order_by('-id')

    sizes = Size.objects.all().order_by('-id')
    category = Category.objects.filter(status=0)


    
    # filter product by brand
    brand = Brand.objects.get(id=brand_id)
    data = Product.objects.filter(brand=brand).order_by('-id')

    accessoriesId = request.GET.get("accessories")
    catId = request.GET.get("category")

    
    if accessoriesId:
        data = Product.objects.filter(accessories=accessoriesId, brand=brand ).order_by('-id')
  
    if catId:
        data = Product.objects.filter(category= catId ).order_by('-id')
  
    else:
        pass

    context = {'data':data, 'cartItems':cartItems, 'accessoriess':accessoriess, 'sizes':sizes, 'brand':brand, 'category':category}

    return render(request, 'product_list.html', context)


def accessories(request):

    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    data = Accessories.objects.all()

    context = {'data':data, 'cartItems':cartItems,}


    return render(request, 'accessories.html', context)


def accessoriesList(request, accessories_id):


    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    accessoriess = Accessories.objects.all().order_by('-id')

    category = Category.objects.filter(status=0)

    brands = Brand.objects.all().order_by('-id')

    # filter product by accessories
    brand = Accessories.objects.get(id=accessories_id)
    data = Product.objects.filter(accessories=brand).order_by('-id')

    catId = request.GET.get("category")
    brandId = request.GET.get("brand")

    if catId:
        data = Product.objects.filter(category= catId, accessories=brand ).order_by('-id')

    if brandId:
        data = Product.objects.filter(brand= brandId, accessories=brand)
    


    context = {'data':data, 'cartItems':cartItems, 'category':category, 'accessories':accessoriess, 'brand':brand, 'brands':brands}

    return render(request, 'accessories_list.html', context)


def cart(request):

    try:
        customer = request.user.customer
    except:
        device =str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items 
    
    context = {'items':items, 'order':order, 'cartItems':cartItems}

    return render(request, 'cart.html', context)


def signup(request):

    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        device =str(request.COOKIES['device'])

        if password1 == password2:

            myuser = User.objects.create_user(username, email, password1)

            myuser.save()
            messages.success(request, "Your Account has been successfully created.")
            return render(request, 'signin.html')
        
        else:
            pass

    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
            


    return render(request, 'signup.html', {'cartItems':cartItems})


def signin(request):


    
    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    context = {'cartItems':cartItems}


    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            try:
                customer = request.user.customer
            except:
                device = str(request.COOKIES['device'])
                customer, created = Customer.objects.get_or_create(device=device, user = user, name=user.get_username, email= user.get_email_field_name )

            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
            products = Product.objects.filter(is_featured=True).order_by('-id')
            newproducts = Product.objects.filter(is_new=True).order_by('-id')
            data = Brand.objects.all().order_by('-id')[:4]

    
            context = {'items':items, 'order':order, 'cartItems':cartItems, 'products':products, 'newproducts':newproducts, 'data':data }
            

            return render(request, 'index.html', context )

        else:
            messages.success(request, "Bad Credentials!")
            return render(request, 'signin.html')

    
    return render(request, 'signin.html', context)


def signout(request):
    logout(request)
    messages.success(request, 'Log out Successfully')

    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)


    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    products = Product.objects.filter(is_featured=True).order_by('-id')
    newproducts = Product.objects.filter(is_new=True).order_by('-id')
    data = Brand.objects.all().order_by('-id')[:4]

    
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'products':products, 'newproducts':newproducts, 'data':data }

    return render(request, 'index.html', context)


def product(request, id):

    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)


    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    
    prod = Product.objects.filter(id=id).first()
    context = {'prod':prod,'cartItems':cartItems}


    return render(request, 'product.html', context)


def checkout(request):

    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items 
    print(cartItems)

    if request.method == "POST":

        csrf = request.POST['csrfmiddlewaretoken']
        country = request.POST['country']
        city = request.POST['city']
        address = request.POST['address']
        state = request.POST['state']
        zip = request.POST['zip']
        cardname = request.POST['cardname']
        cardnumber = request.POST['cardnumber']
        expmonth = request.POST['expmonth']
        expyear = request.POST['expyear']
        ccv = request.POST['cvv']
        product = request.POST['product']

        shipAddress = ShippingAddress(customer=customer,order=order, address=address, city=city, state=state, zipcode=zip, )
        shipAddress.save()
        ordered = OrderItem.objects.all()
        for order in ordered:
            ordered = Ordered(product=order.product, order=order.order, quantity=order.quantity)
            ordered.save()


        popOrderItem = items
        popOrderItem.delete()



        products = Product.objects.filter(is_featured=True).order_by('-id')
        newproducts = Product.objects.filter(is_new=True).order_by('-id')
        data = Brand.objects.all().order_by('-id')[:4]

        cItems = cartItems

        context = {'items':items, 'order':order, 'cartItems':cItems, 'products':products, 'newproducts':newproducts, 'data':data }
        return render(request, 'index.html', context)
            

        print(product)

    





    context = {'items':items, 'order':order, 'cartItems':cartItems}



    return render(request, 'checkout.html', context)


def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']


    print('Action:', action)
    print('ProducdId:', productId)

    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        print(device)
        customer, created = Customer.objects.get_or_create(name=device)

         
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1

    elif action == 'remove':
        orderItem.quantity -= 1
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added', safe=False)


def viewAll(request):
    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    products = Product.objects.all()
    newproducts = Product.objects.filter(is_new=True).order_by('-id')
    data = Brand.objects.all().order_by('-id')[:4]

    
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'products':products, 'newproducts':newproducts, 'data':data }

    return render(request, 'all_product.html', context)



def search(request):

    q = request.GET['q']
    try:
        customer = request.user.customer
    except:
        device = str(request.COOKIES['device'])
        customer, created = Customer.objects.get_or_create(name=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    if q:
        products = Product.objects.filter(name__icontains=q).order_by('-id')
    else:
        products = None

    
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'products':products }

    return render(request, 'search.html', context)


