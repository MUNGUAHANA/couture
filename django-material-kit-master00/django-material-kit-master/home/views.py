from django.shortcuts import render
from home.models import*
from django.http import HttpResponse
from theme_material_kit.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib.auth.decorators import permission_required, login_required
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages


from home.forms import *

from django.contrib.auth import views as auth_views
# Create your views here.

# Authentication
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/sign-up.html', context)

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/sign-in.html'
  form_class = LoginForm
  
  
class UserLoginViewDressMaker(auth_views.LoginView):
    template_name = 'pages/sign_inDressmaker.html'
    form_class = LoginForm
       
if UserLoginView:
    success_url = '/'  
if UserLoginViewDressMaker:
    success_url = 'homeDM'
    
def blog_post_add(request):   
    if request.method == "POST":        
        form =contenuForm(request.POST, request.FILES)        
        if form.is_valid(): 
            form.save()           
            return redirect('homeDM')  # r e d i r e c t s t o b l o g _ p o s t . g e t _ a b s o l u t e _ u r l ( )
    else:        
        form = contenuForm()
    return render(request, 'pages/newcontent.html', { 'form': form })

def blog_post_addMod(request):   
    if request.method == "POST":        
        form =modeleForm(request.POST, request.FILES)        
        if form.is_valid():  
            form.save()          
            return redirect('homeDM')  # r e d i r e c t s t o b l o g _ p o s t . g e t _ a b s o l u t e _ u r l ( )
    else:        
        form = modeleForm()
    return render(request, 'pages/newmodel.html', { 'form': form })


def homeDM(request):
    # Page from the theme 
    return render(request, 'pages/homeDM.html')  

def hOmePage(request):
    # Page from the theme 
    return render(request, 'pages/homePage.html')
    
def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

def index1(request):
    # Page from the theme 
    return render(request, 'pages/index1.html')

def models(request):
    # Page from the theme
    mod = modele.objects.all()
    return render(request, 'pages/models.html', {'mod':mod})

def contact_us(request):
      return render(request, 'pages/contact-us.html')

def about_us(request):
  return render(request, 'pages/about-us.html')

def author(request):
    cont=contenu.objects.all()
    return render(request, 'pages/author.html', {'cont':cont})

# Sections
def presentation(request):
  return render(request, 'sections/presentation.html')
  
def page_header(request):
  return render(request, 'sections/page-sections/hero-sections.html')

def features(request):
  return render(request, 'sections/page-sections/features.html')

def navbars(request):
  return render(request, 'sections/navigation/navbars.html')

def nav_tabs(request):
  return render(request, 'sections/navigation/nav-tabs.html')

def pagination(request):
  return render(request, 'sections/navigation/pagination.html')

def forms(request):
  return render(request, 'sections/input-areas/forms.html')

def inputs(request):
  return render(request, 'sections/input-areas/inputs.html')

def avatars(request):
  return render(request, 'sections/elements/avatars.html')

def badges(request):
  return render(request, 'sections/elements/badges.html')

def breadcrumbs(request):
  return render(request, 'sections/elements/breadcrumbs.html')

def buttons(request):
  return render(request, 'sections/elements/buttons.html')

def dropdowns(request):
  return render(request, 'sections/elements/dropdowns.html')

def progress_bars(request):
  return render(request, 'sections/elements/progress-bars.html')

def toggles(request):
  return render(request, 'sections/elements/toggles.html')

def typography(request):
  return render(request, 'sections/elements/typography.html')

def alerts(request):
  return render(request, 'sections/attention-catchers/alerts.html')

def modals(request):
  return render(request, 'sections/attention-catchers/modals.html')

def tooltips(request):
  return render(request, 'sections/attention-catchers/tooltips-popovers.html')

