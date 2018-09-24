from django import forms
from django.contrib.auth.models import User
from .models import Myhouses, Vip

class MyHouseEditForm(forms.ModelForm):    
    class Meta:        
        model = Myhouses   
        labels = {
            'Landlord_number': "Landlord or House Agent's Phone Number"
        }     
        fields = ('name_of_accomodation', 'type_of_apartment','Parking_space', 'Number_of_rooms','Fenced', 'Running_water', 'house_rent', 'Landlord_number','Toilet', 'availability', 'State','Available_from', 'City_or_town', 'Size_of_room', 'nearest_institution', 'description', 'Street', 'house_image', 'house_image2', 'house_image3', 'house_image4', 'house_image5', 'house_image6', 'house_image7', 'house_image8', 'house_image9', 'house_image10', 'house_image11', 'house_image12', 'Account_number', 'Account_name') 


class VipForm(forms.ModelForm):    
    class Meta:        
        model = Vip  
        fields = ('type_of_apartment', 'Number_of_rooms', 'State', 'City_or_town') 