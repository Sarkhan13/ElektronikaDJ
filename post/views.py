from django.shortcuts import render,redirect
from .models import *
from .forms import Elan_form
from django.forms import modelform_factory,modelformset_factory


def post_create_phone(request):
    form = Elan_form()
    Imageformset = modelformset_factory(images, fields=('image',), extra=4,min_num=1)
    Phoneform = modelform_factory(Phone, fields=('display','main_cam','add_cam','battery','memory','ram','color','network','biometric'))
    if request.method == 'POST':
        form = Elan_form(request.POST or None, request.FILES or None)
        imageform = Imageformset(request.POST or None,request.FILES or None)
        phoneformod = Phoneform(request.POST or None)

        if form.is_valid() and imageform.is_valid() and phoneformod.is_valid():
            post = form.save(commit=False)
            post.category = Category.objects.get(id = 1)
            post.save()

            for i in imageform:
                try:
                    photo = images(product=post,image = i.cleaned_data['image'])
                    photo.save()
                except:
                    break

            phone = Phone(product=post,display = phoneformod.cleaned_data['display'],main_cam = phoneformod.cleaned_data['main_cam'], add_cam = phoneformod.cleaned_data['add_cam'],battery =phoneformod.cleaned_data['battery'], biometric = phoneformod.cleaned_data['biometric'],memory = phoneformod.cleaned_data['memory'], ram =  phoneformod.cleaned_data['ram'],network =  phoneformod.cleaned_data['network'],color =  phoneformod.cleaned_data['color'] )
            phone.save()

            return redirect(homepage)

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
