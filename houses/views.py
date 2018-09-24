from django.http import HttpResponse 
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login 
from .forms import MyHouseEditForm, VipForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . models import Myhouses, paid, Paids, Vip
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.template import RequestContext
from paystack.signals import payment_verified
from django.dispatch import receiver
from paystack.signals import event_signal
import re


@login_required
def addlisting(request):    
    if request.method == 'POST': 
        house_form = MyHouseEditForm(request.POST, files=request.FILES, )
        if house_form.is_valid():    
            Houses = house_form.save(commit=False)
            Houses.author=request.user
            Houses.Payment_status = "Not Paid"
            Houses.save()
            id = Houses.pk
            messages.success(request, 'Listing Created Succesfully successfully')
            return redirect('detail', id)           
    else:        
        house_form = MyHouseEditForm()
    return render(request, 'houses/addlisting.html', {'house_form':house_form},  )


class UserListView(LoginRequiredMixin,generic.ListView):
    model = Myhouses
    template_name ='houses/ListingByUser.html'
    paginate_by = 9
    
    
    def get_queryset(self):
        return Myhouses.objects.filter(author=self.request.user)

class VipListView(LoginRequiredMixin,generic.ListView):
    model = Vip
    template_name ='houses/vipByUser.html'
    paginate_by = 9
    
    
    def get_queryset(self):
        return Vip.objects.filter(author=self.request.user)


class alllisting(LoginRequiredMixin,generic.ListView):
    model = Myhouses
    template_name ='houses/alllisting.html'
    paginate_by = 2




@login_required
def listbyuserdetails(request, id):
    house_list1 = Myhouses.objects.get(id = id)

    context = {
        'house_list1':house_list1
    }

    return render(request, 'houses/ListingByUserDetails.html', context)


@login_required
def vipbyuserdetails(request, id):
    house_list1 = Vip.objects.get(id = id)

    context = {
        'house_list1':house_list1
    }

    return render(request, 'houses/vip-details.html', context)

@login_required
def editlist2(request, pk):
    house_edit = get_object_or_404(Myhouses, pk = pk)
    if request.method == 'POST': 
        house_form = MyHouseEditForm(request.POST, files=request.FILES, instance=house_edit)
        if house_form.is_valid():    
            Houses = house_form.save(commit=False)
            Houses.save()
            messages.success(request, 'Listing Updated Succesfully')
            return redirect('editlist2', pk) 
        else:
            messages.success(request, 'Error Updating Listing')
            return redirect('editlist2', pk)         
    else:        
        house_form = MyHouseEditForm(instance=house_edit)
    return render(request, 'houses/editlist.html', {'house_form':house_form, 'house_edit': house_edit},  )

@login_required
def deletelist(request, pk):
    house_delete = get_object_or_404(Myhouses, pk = pk)
    if request.user == house_delete.author:
        house_delete.delete()
        messages.success(request, 'Listing Deleted Succesfully')
        return redirect('userlist')
    else:
        return HttpResponse('unauthorized ACTIVITY')

@login_required
def deletelist2(request, pk):
    house_delete = get_object_or_404(Vip, pk = pk)
    if request.user == house_delete.author:
        house_delete.delete()
        messages.success(request, 'Search Deleted Succesfully')
        return redirect('viplist')
    else:
        return HttpResponse('unauthorized ACTIVITY')



@login_required
def phone(request, id):
    house_list1 = Myhouses.objects.get(id = id)

    context = {
        'house_list1':house_list1
    }

    return render(request, 'houses/phone.html', context)

@login_required
def vipSearch(request):
    if request.method == 'POST': 
        vip_form = VipForm(request.POST )
        if vip_form.is_valid():    
            vip = vip_form.save(commit=False)
            vip.author=request.user
            vip.save()
            messages.success(request, 'Information saved successfully')
            return redirect('dashboard')           
    else:        
        vip_form = VipForm()
    return render(request, 'houses/vip.html', {'vip_form': vip_form})







@receiver(event_signal)
def on_event_received(sender, event, data, **kwargs):
    a = 'greatgodevent'
    b = 'jesusevent'
    c = int(4)
    d = data['metadata']['referrer']
    e = (re.findall('\d+', d ))
    id = int(e[0])
    g = 'Paid'
    editme = get_object_or_404(Myhouses, pk = id)
    editme.Payment_status = g
    editme.save()
    Paids.objects.create(myRef= event, amount=c, username=id, )
    return HttpResponse(status=200)

   