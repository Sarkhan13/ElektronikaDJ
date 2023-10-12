from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import Elan_form
from django.forms import modelform_factory,modelformset_factory
from django.contrib import messages
from django.http import Http404

# post create Telefon

def post_create_phone(request):
    form = Elan_form()
    Imageformset = modelformset_factory(images, fields=('image',), extra=3,min_num=2)
    Phoneform = modelform_factory(Phone, fields=('display','main_cam','add_cam','battery','memory','ram','color','network','biometric'))
    if request.method == 'POST':
        form = Elan_form(request.POST or None, request.FILES or None)
        imageform = Imageformset(request.POST or None,request.FILES or None)
        phoneformod = Phoneform(request.POST or None)

        if form.is_valid() and imageform.is_valid() and phoneformod.is_valid():
            post = form.save(commit=False)
            post.category = Category.objects.get(id = 1)
            post.user = request.user
            post.save()

            for i in imageform:
                try:
                    photo = images(product=post,image = i.cleaned_data['image'])
                    photo.save()
                except:
                    break

            phone = Phone(product=post,display = phoneformod.cleaned_data['display'],main_cam = phoneformod.cleaned_data['main_cam'], add_cam = phoneformod.cleaned_data['add_cam'],battery =phoneformod.cleaned_data['battery'], biometric = phoneformod.cleaned_data['biometric'],memory = phoneformod.cleaned_data['memory'], ram =  phoneformod.cleaned_data['ram'],network =  phoneformod.cleaned_data['network'],color =  phoneformod.cleaned_data['color'] )
            phone.save()

            return redirect(post.get_url)
        
        elif not imageform.is_valid():
            messages.error(request, 'Ən azı 2 şəkil yüklənməlidir!')
            messages.success(request, 'Şəkilləri tam yükləyin!')


    else:
        form = Elan_form()
        imageform = Imageformset(queryset=images.objects.none())
        phoneformod = Phoneform()


    contex = {
        'form':form,
        'image': imageform,
        'phone':phoneformod
    }

    return render(request, 'phoneadd.html',contex)

# post create Notebook

def post_create_note(request):
    form = Elan_form()
    Imagesformset = modelformset_factory(images, fields=('image',), extra=3, min_num=2)
    Noteform = modelform_factory(Notebook, fields=('memory','ram','speed','processor','color'))
    if request.method == 'POST':
        form = Elan_form(request.POST or None, request.FILES or None)
        imageform = Imagesformset(request.POST or None, request.FILES or None)
        noteformvar = Noteform(request.POST or None)

        if form.is_valid() and imageform.is_valid() and noteformvar.is_valid():
            post = form.save(commit=False)
            post.category = Category.objects.get(id=4)
            post.user = request.user
            post.save()

            for i in imageform:
                try:
                    photo = images(product=post, image= i.cleaned_data['image'])
                    photo.save()
                except:
                    break

            note = Notebook(product=post,memory=noteformvar.cleaned_data['memory'],ram=noteformvar.cleaned_data['ram'],speed=noteformvar.cleaned_data['speed'],processor=noteformvar.cleaned_data['processor'],color=noteformvar.cleaned_data['color'])
            note.save()

        elif not imageform.is_valid():
            messages.error(request, 'Ən azı 2 şəkil yüklənməlidir!')
            messages.success(request, 'Şəkilləri tam yükləyin!')

            return redirect(post.get_url)
    
    else:
        form = Elan_form()
        imageform = Imagesformset(queryset=images.objects.none())
        noteformvar = Noteform()

    contex = {
        'form': form,
        'image': imageform,
        'phone': noteformvar 
    }

    return render(request, 'phoneadd.html',contex)


# post update Phone

def post_update_phone(request, id):
    post = get_object_or_404(Product, id=id)

    if post.user != request.user:
        raise Http404

    prodphone = Phone.objects.get(product=post)

    Phoneform = modelform_factory(Phone, fields=('display','main_cam','add_cam','battery','memory','ram','color','network','biometric'))
    
    form = Elan_form(request.POST or None, request.FILES or None, instance=post)
        
    phoneformod = Phoneform(request.POST or None, instance=prodphone)

    if form.is_valid()  and phoneformod.is_valid():
            post = form.save(commit=False)
            post.category = Category.objects.get(id = 1)
            
            post.save()

            
            phone = Phone(product=post,display = phoneformod.cleaned_data['display'],main_cam = phoneformod.cleaned_data['main_cam'], add_cam = phoneformod.cleaned_data['add_cam'],battery =phoneformod.cleaned_data['battery'], biometric = phoneformod.cleaned_data['biometric'],memory = phoneformod.cleaned_data['memory'], ram =  phoneformod.cleaned_data['ram'],network =  phoneformod.cleaned_data['network'],color =  phoneformod.cleaned_data['color'] )
            phone.save()

            return redirect(post.get_url)
    
    contex = {
        'form':form,
        
        'phone':phoneformod
    }

    return render(request,'phoneadd.html',contex)
    
   
def post_delete(request, id):
    post = get_object_or_404(Product, id=id)

    if post.user != request.user:
        raise Http404
    
    post.delete()

    return redirect(homepage)

    


def homepage(request):
    category = Category.objects.exclude(id=1)
    cat1 = Category.objects.get(id=1)
    categories = Category.objects.all()
    product = Product.objects.all().order_by('-date')
    phonecount = Product.objects.filter(category__name='Telefonlar').count()

    special = specialshop.objects.all()

    contex = {
        'category':category,
        'cat1':cat1,
        'product':product,
        'categories':categories,
        'phonecount':phonecount,
        'special': special,
    }


    return render(request,'index.html',contex)


def cartpage(request):
    return render(request,'cart.html')


def checkpage(request):
    return render(request,'checkout.html')


def contactpage(request):
    return render(request,'contact.html')


def detailpage(request,id):

    product = Product.objects.get(id=id)

    name = product.name.split(' ')
    

    add_prod = Product.objects.filter(name__contains=name[0])

    
    


    contex = {
        'product': product,
        'add_prod':add_prod,

        
    }


    return render(request,'detail.html',contex)


def shoppage(request):
    return render(request,'shop.html')
