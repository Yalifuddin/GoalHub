import json
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests
from django.utils.html import strip_tags
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "my":
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()

    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'stok': product.stok,
            'description': product.description,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]

    last_login = request.user.last_login
    if last_login:
        last_login = last_login.strftime('%Y-%m-%d %H:%M:%S.%f')
    else:
        last_login = 'Never'

    context = {
        'nama_projek' : 'GoalHub',
        'npm' : '2406437155',
        'name': 'Yafi Alifuddin',
        'class': 'PBP F',
        'product_list': product_list,
        'product_json': json.dumps(data),
        'last_login': last_login,
        'username': request.user.username,
        'filter_type': filter_type
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    context = {
        'product': product
    }
    
    return render(request, "product_details.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize('xml', product_list)
    return HttpResponse(xml_data, content_type='application/xml')

def show_xml_by_id(request, product_id):
    try: 
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

@login_required(login_url='/login')
def show_json(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "my":
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'stok': product.stok,
            'description': product.description,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'stok': product.stok,
            'description': product.description,
            'is_featured': product.is_featured,
            'username': product.user.username if product.user else 'Anonymous',
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    if request.method == "POST":
        if request.content_type == 'application/json':
            import json
            data = json.loads(request.body)
            form = UserCreationForm(data)
        else:
            form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('ajax') or request.content_type == 'application/json':
                return JsonResponse({'success': True, 'message': 'Your account has been successfully created!', 'redirect': reverse('main:login')})
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            if request.POST.get('ajax') or request.content_type == 'application/json':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        # Support JSON (AJAX) and normal form submissions
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
            except Exception:
                return JsonResponse({'success': False, 'message': 'Invalid JSON'}, status=400)

            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'message': 'Login successful!', 'redirect': reverse('main:show_main')})
            else:
                return JsonResponse({'success': False, 'message': 'Username atau password salah.'}, status=200)
        else:
            # Use AuthenticationForm for normal POST
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return HttpResponseRedirect(reverse('main:show_main'))
            # form invalid -> re-render with errors
            context = {'form': form}
            return render(request, 'login.html', context)

    # GET request -> render login form
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.error(request, 'You have been logged out successfully.')
    response = HttpResponseRedirect(reverse('main:login'))
    return response

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user and product.user != request.user:
        return HttpResponseForbidden("You do not have permission to edit this product.")
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user and product.user != request.user:
        return HttpResponseForbidden("You do not have permission to delete this product.")
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
@require_POST
@csrf_exempt
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    stok = request.POST.get("stok")
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        is_featured=is_featured,
        stok=stok,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user and product.user != request.user:
        return HttpResponse(b"FORBIDDEN", status=403)
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    stok = request.POST.get("stok")

    product.name = name
    product.price = price
    product.description = description
    product.thumbnail = thumbnail
    product.category = category
    product.is_featured = is_featured
    product.stok = stok
    product.save()

    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
def delete_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user and product.user != request.user:
        return HttpResponse(b"FORBIDDEN", status=403)
    product.delete()
    return HttpResponse(b"DELETED", status=200)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        price = data.get("price")
        stok = data.get("stok", 0)
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Product(
            name=name, 
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            price=price,
            stok=stok,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    