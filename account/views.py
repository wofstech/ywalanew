from django.http import HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, SubForm
from django.contrib.auth.decorators import login_required
from .models import Profile, News
from django.contrib import messages
from django.contrib.auth.models import User
from houses.models import Myhouses, Paids
from django.db.models import Q
from django.views import generic
from account.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from paystack.signals import payment_verified
from django.dispatch import receiver
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def user_login(request):    
    if request.method == 'POST':        
        form = LoginForm(request.POST)        
        if form.is_valid():            
            cd = form.cleaned_data            
            user = authenticate(username=cd['username'],                                
            password=cd['password'])            
            if user is not None:                
                if user.is_active:                    
                    login(request, user)                    
                    return HttpResponse('Authenticated '\
                'successfully')                
                else:                    
                        return HttpResponse('Disabled account')
            else:                
                        return HttpResponse('Invalid login')    
    else:        
        form = LoginForm()    
        return render(request, 'account/login.html', {'form': form}) 


@login_required 
def dashboard(request):
    profile = Profile.objects.all() 
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'profile': profile}) 

def register(request):    
    if request.method == 'POST':        
        user_form = UserRegistrationForm(request.POST)        
        if user_form.is_valid():            
            # Create a new user object but avoid saving it yet            
            new_user = user_form.save(commit=False)            
            # # Set the chosen password                             
            new_user.set_password(                
            user_form.cleaned_data['password'])            
            # Save the User object            
            new_user.save() 
            profile = Profile.objects.create(user=new_user)            
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            messages.error(request, "Error")
    else:        
         user_form = UserRegistrationForm()    
    return render(request, 'account/register.html', {'user_form': user_form}) 

@login_required 
def edit(request):    
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST) 
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():            
            user_form.save()            
            profile_form.save()
            messages.success(request, 'Profile updated successfully') 
        else:            
             messages.error(request, 'Error updating your profile') 
    
    else:        
        user_form = UserEditForm(instance=request.user)        
        profile_form = ProfileEditForm(instance=request.user.profile) 

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

def search(request):
    query = request.GET.get('q')
    results = Myhouses.objects.filter(Q(name_of_accomodation__icontains=query) | Q(type_of_apartment__icontains=query) | Q(City_or_town__icontains=query) | Q(State__icontains=query) | Q(nearest_institution__icontains=query))

    return render(request, 'account/searchme.html', {'results': results})

def search_detail(request, id):
    search_list = Myhouses.objects.get(id = id)
    related = Myhouses.objects.filter(State__icontains=search_list.State)[:3]
    context = {
        'search_list': search_list,
        'related': related
    }

    @receiver(payment_verified)
    def on_payment_verified(sender, ref,amount, username, **kwargs):
        search_list = Myhouses.objects.get(id = id)
        name = search_list.name_of_accomodation
        Paids.objects.create(myRef= ref, amount=amount, username=ref, )
    return render(request, 'houses/mysearch.html', context)


class search_detail2(LoginRequiredMixin, generic.DetailView):
    model = Myhouses
    template_name = 'houses/mysearch.html'
    context_object_name = 'search_list'
    

    def on_payment_verified(sender, ref,amount, username, **kwargs):
        search_list = Myhouses.objects.get(id = id)
        name = search_list.name_of_accomodation
        Paids.objects.create(myRef= ref, amount=amount, username=ref, )
    
    
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['Your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['gabrielabuka@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "account/contact.html", {'form': form})

def success(request):
    return render(request, 'account/success.html')


