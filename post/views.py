from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import Elan_form,LoginForm,RegisterForm
from django.forms import modelform_factory,modelformset_factory
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


def logoutpage(request):
    logout(request)
    return redirect(homepage)

def is_valid_query(query):
    return query != "" and query is not None

from django.db.models import Q

def searching(request):
    product = Product.objects.all()
    searchdata = request.GET.get('query')
    price_bet = request.GET.get('price_between')

    if is_valid_query(searchdata):
        product = product.filter(name__contains = searchdata)

    if is_valid_query(price_bet):
        if price_bet == 'allprice':
            product = product

        elif price_bet == 'max100':
            product = product.filter(price__lte = 100)

        elif price_bet == 'max200':
            product = product.filter(Q(price__gte=100) & Q(price__lte = 200))

        elif price_bet == 'max300':
            product = product.filter(Q(price__gte=200) & Q(price__lte = 300))

        elif price_bet == 'max400':
            product = product.filter(Q(price__gte=300) & Q(price__lte = 400))

        elif price_bet == 'max500':
            product = product.filter(Q(price__gte=400) & Q(price__lte = 500))


    contex = {
        'product':product,
        'search': searchdata
    }

    return render(request, 'shop.html', contex)

def register(request):
    if request.user.is_authenticated:
        return redirect(homepage)
    

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        new_user = authenticate(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
        login(request, new_user)
        return redirect(homepage)
    
    data = {
        'form':form
    }

    return render(request, 'logreg.html',data)




def loginpage(request):
    if request.user.is_authenticated:
        return redirect(homepage)
    

    form = LoginForm(request.POST or None)

    if form.is_valid():
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])

        if user:
            login(request, user)
            return redirect(homepage)
        
        else:
            messages.error(request, 'İstifadəçi adı və ya şifrə yanlışdır. ')

    contex = {
        'form': form
    }

    return render(request, 'logreg.html', contex)



def profile(request, username):
    userprofile = User.objects.get(username=username)

    contex = {
        'user': userprofile
    }

    return render(request, 'profile.html',contex)





# post create Telefon

def post_create_phone(request):
    if not request.user.is_authenticated:
        return redirect(homepage)
    

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
    if not request.user.is_authenticated:
        return redirect(homepage)
      

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
    Imageformset = modelformset_factory(images, fields=('image',), extra=3,min_num=0)  
    form = Elan_form(request.POST or None, request.FILES or None, instance=post)
    
    phoneformod = Phoneform(request.POST or None, instance=prodphone)

    imageformvar = Imageformset(request.POST or None,request.FILES or None, queryset=images.objects.none())

    if form.is_valid()  and phoneformod.is_valid():
        form.save()
        phoneformod.save()

        for image in post.images_set.all():
            image.image = request.FILES.get(f'image_{image.id}',image.image)
            image.save()

        if imageformvar.is_valid():
            
            for i in imageformvar:
                try:
                    photo = images(product=post,image = i.cleaned_data['image'])
                    photo.save()
                except:
                    break


        return redirect(post.get_url)
    
    contex = {
        'form':form,
        
        'phone':phoneformod,
        'post': post,
        'image': imageformvar
    }

    return render(request,'post_update.html',contex)
    
   
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
    product = Product.objects.all().order_by('-views')
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

from django.db.models import F 

def detailpage(request,id):

    product = Product.objects.get(id=id)

    name = product.name.split(' ')
    

    add_prod = Product.objects.filter(name__contains=name[0])

    Product.objects.filter(id=id).update(views= F('views')+1)
    
    


    contex = {
        'product': product,
        'add_prod':add_prod,

        
    }


    return render(request,'detail.html',contex)


def shoppage(request):
    return render(request,'shop.html')
