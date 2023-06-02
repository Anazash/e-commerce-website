from django.forms import ValidationError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Cart, Category
# from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
# from django.contrib.auth.decorators import login_required
from .models import Usermember

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_staff:
                return redirect('admin1')
            else:
                return render(request, 'home.html', {'username': username})
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

      

def signup(request):
    return render(request,'signup.html')

def admin1(request):
    return render(request,'adminshow.html')

# 
def logout(request):
    return redirect('home')

def add_category(request):
    if request.method == 'POST':
        categoryname = request.POST['cname']  # use categoryname instead of catname
        cat = Category(name=categoryname)  # use categoryname instead of catname
        cat.save()
        return redirect('admin1')

def add_product(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'addd_product.html', context)


def add_products(request):
        name=request.POST['name']
        description=request.POST['description']
        price=request.POST['price']
        sel=request.POST['sel']
        image=request.FILES.get('image')
        category1=Category.objects.get(id=sel)
        product=Product(name=name,description=description,price=price,category=category1,image=image)
        product.save()
        return redirect('adp')

def show_product(request):
    products=Product.objects.all()
    return render(request,'show_product.html',{'prdct':products})

def new_arrivals(request):
    products=Product.objects.all()
    return render(request,'newarrivals.html',{'prdct':products})

def show_user(request):
    members = Usermember.objects.all()
    return render(request, 'show_user.html', {'show': members})


def cart(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})

def add_to_cart(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.POST['image']

        # check if the item already exists in the cart
        cart_item = Cart.objects.filter(name=name).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item = Cart(name=name, price=price, description=description, image=image)
            cart_item.save()

        return redirect('cart')

from django.http import JsonResponse

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, pk=item_id)
    cart_item.delete()
    response = {
        'success': True,
        'message': 'Item successfully removed from cart.'
    }
    return JsonResponse(response)


def new(request):
    prd=Product.objects.all()
    return render(request,'newarrivals.html',{'products':prd})

def adp(request):
    cata=Category.objects.all()
    return render(request,'addd_product.html',{'catagory':cata})


def shpd(request):
    prd=Product.objects.all()
    return render(request,'show_product.html',{'products':prd})

def shus(request):
    us=Usermember.objects.all()
    return render(request,'show_user.html',{'show':us})

def adct(request):
    return render(request,'adminshow.html')


# def edit_student(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'POST':
#         student.name = request.POST.get('name')
#         student.address = request.POST.get('address')
#         student.age = request.POST.get('age')
#         student.date = request.POST.get('date')
#         course_id = request.POST.get('sel')
#         student.course = get_object_or_404(Course, pk=course_id)
#         student.save()
#         return redirect('show_student')
   
#     courses = Course.objects.all()
#     return render(request, 'edit_student.html', {'student': student, 'courses': courses})


def delete_product(request,id):
    prod=Product.objects.get(id=id)
    prod.delete()
    return redirect('shpd')

def user_signup(request):
    # courses=Course.objects.all()
    return render(request,'signup.html')

def add_user(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        address=request.POST.get('address')
        email=request.POST.get('email')
        age=request.POST.get('age')
        number=request.POST.get('number')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists')
                return redirect('user_signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
                u=User.objects.get(id=user.id)
                
                member=Usermember(address=address,age=age,number=number,user=u)
                member.save()
                return render(request,'login.html')
            
        else:
            messages.info(request,'Password doesnt match')
            return redirect('user_signup')
        
    else:
        return render(request,'login.html')
    
# def teach(request):
#     return render(request,'teacher_view.html')
    
# def see_pro(request):
#     return render(request,'teacher_card.html')

# @login_required(login_url='home')
# def see_pro(request):
#     user = request.user
#     member = Usermember.objects.get(user=user)
#     context = {'user': user, 'member': member}
#     return render(request, 'teacher_card.html', context)


# def edit_teach(request):
#     return render(request,'teacher_card.html')