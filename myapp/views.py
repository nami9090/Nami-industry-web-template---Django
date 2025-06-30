from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import (
                    Feature, 
                    Produit, 
                    More_Culture, 
                    StepModel, 
                    TestimonialModel, 
                    TeamModel, 
                    LocationModel, 
                    EmailModel, 
                    HourOfOperation, 
                    AboutImageModel,
                    Galleries, GalleryImages)
from .forms import ProduitForm, SuggestForm


# Create your views here.
def index(request):
    success = False
    if request.method == 'POST':
       form = SuggestForm(request.POST)
       if form.is_valid():
           form.save()
           success = True
    else:
        form = SuggestForm()
        success = False

    features = Feature.objects.all()
    elements = More_Culture.objects.all()
    steps = StepModel.objects.all()
    testimonials = TestimonialModel.objects.all()
    teams = TeamModel.objects.all()
    locations = LocationModel.objects.all()
    emails = EmailModel.objects.all()
    works_hours = HourOfOperation.objects.all()
    aboutImages = AboutImageModel.objects.all()
    galleryInfos = Galleries.objects.all()
    galleryImage = GalleryImages.objects.all()

    context = {
        'success':success,
        'features':features, 
        'elements':elements, 
        'steps':steps, 
        'testimonials':testimonials,
        'teams': teams,
        'locations':locations,
        'emails':emails,
        'works_hours':works_hours,
        'aboutImages':aboutImages,

        'galleryInfos': galleryInfos,
        'galleryImage': galleryImage
    }
    return render(request, 'index.html',context)

def counter(request):
    # text = request.POST['text']
    # amount_of_word = len(text.split())
    posts = [1,2,3,4,5,'tim','tom','johm']
    return render(request, 'counter.html', {'posts':posts})

def portfolio(request, pk):
    galleryInfos = Galleries.objects.get(id=pk)
    galleryImage = galleryInfos.images.all()
    locations = LocationModel.objects.all()
    emails = EmailModel.objects.all()
    features = Feature.objects.all()
    context = {
        'galleryInfos': galleryInfos,
        'galleryImage': galleryImage,
        'locations':locations,
        'emails':emails,
        'features':features,
    }
    return render(request, 'portfolio-details.html', context)

def service(request, pk):
    feature = Feature.objects.get(id=pk)
    featureDetail = feature.detail.all()
    locations = LocationModel.objects.all()
    emails = EmailModel.objects.all()
    features = Feature.objects.all()
    elements = More_Culture.objects.all()
    context = {
        'feature':feature,
        'locations':locations,
        'emails':emails,
        'features':features,
        'element':elements,
        'emails':emails,
        'featureDetail':featureDetail
    }
    return render(request, 'service-details.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
        return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invali')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})

def ajouter_image(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produit')
    else:
        form = ProduitForm()
        return render(request, 'ajouter_produit.html', {'form': form})
    
def produit_viz(request):
    produits = Produit.objects.all()
    return render(request, 'produit.html',{'produits':produits})

def more_culture(request):
    elements = More_Culture.objects.all()
    return render(request,'index.html', {'elements':elements})

def starter_page(request):
    return render(request, 'starter-page.html')

from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)
