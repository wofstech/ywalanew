from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

  

class Myhouses(models.Model):
    
    Available = 'A'
    Not_Available = 'NA'
    Reserved = 'R'
    Availability = (
        (Available, 'Available'),
        (Not_Available, 'Not_Available'),
        (Reserved, 'Reserved')
    )


    private = 'Private'
    Shared = 'Shared'
    toilet = (
        (private, 'private'),
        (Shared, 'Shared'),
    )


    Yes = 'Yes'
    No = 'No'
    water = (
        (Yes, 'Yes'),
        (No, 'No'),
    )

    Yes = 'Yes'
    No = 'No'
    fence = (
        (Yes, 'Yes'),
        (No, 'No'),
    )

    Yes = 'Yes'
    No = 'No'
    park = (
        (Yes, 'Yes'),
        (No, 'No'),
    )



    Flat = 'Flat'
    Self_contained = 'Self Contain'
    Bungalow = 'Bungalow'
    Mini_flat = 'Mini Flat'
    Duplex = 'Duplex'
    Student_lodge = 'Student Lodge'
    Student_hostel = 'Student Hostel'
    Others = 'Others'
    Looking_for_roommate = 'Looking for roommate'
    Room = (
        (Flat, 'Flat'),
        (Self_contained, 'Self contained'),
        (Bungalow, 'Bungalow'),
        (Mini_flat, 'Mini flat'),
        (Student_lodge, 'Student lodge'),
        (Student_hostel, 'Student hostel'),
        (Others, 'Others'),
        (Looking_for_roommate, 'Looking for roommate'),
    )


    Abuja = 'Abuja'
    Abia = 'Abia'
    Adamawa = 'Adamawa'
    Akwa_ibom = 'Akwa Ibom'
    Anambra = 'Anambra'
    Bauchi = 'Bauchi'
    Bayelsa = 'Bayelsa'
    Benue = 'Benue'
    Borno = 'Borno'
    Cross_River = 'Cross River'
    Delta = 'Delta'
    Ebonyi = 'Ebonyi'
    Edo = 'Edo'
    Ekiti = 'Ekiti'
    Enugu = 'Enugu'
    Gombe = 'Gombe'
    Imo = 'Imo'
    Jigawa = 'Jigawa'
    Kaduna = 'Kaduna'
    Kano = 'Kano'
    Katsina = 'Katsina'
    Kebbi = 'Kebbi'
    Kogi = 'Kogi'
    Kwara = 'Kwara'
    Lagos = 'Lagos'
    Nasarawa = 'Nasarawa'
    Niger = 'Niger'
    Ogun = 'Ogun'
    Ondo = 'Ondo'
    Osun = 'Osun'
    Oyo = 'Oyo'
    Plateau = 'Plateau'
    Rivers = 'Rivers'
    Sokoto = 'Sokoto'
    Taraba = 'Taraba'
    Yobe = 'Yobe'
    Zamfara = 'Zamfara'
    
    States = (
        (Abuja, 'Abuja'),
        (Abia, 'Abia'),
        (Adamawa, 'Adamawa'),
        (Akwa_ibom, 'Akwa ibom'),
        (Anambra, 'Anambra'),
        (Bauchi, 'Bauchi'),
        (Bayelsa, 'Bayelsa'),
        (Benue, 'Benue'),
        (Borno, 'Borno'),
        (Cross_River, 'Cross River'),
        (Delta, 'Delta'),
        (Ebonyi, 'Ebonyi'),
        (Edo, 'Edo'),
        (Ekiti, 'Ekiti'),
        (Enugu, 'Enugu'),
        (Gombe, 'Gombe'),
        (Imo, 'Imo'),
        (Jigawa, 'Jigawa'),
        (Kaduna, 'Kaduna'),
        (Kano, 'Kano'),
        (Katsina, 'Katsina'),
        (Kebbi, 'Kebbi'),
        (Kogi, 'Kogi'),
        (Kwara,'Kwara'),
        (Lagos,'Lagos'),
        (Nasarawa, 'Nasarawa'),
        (Niger,  'Niger'),
        (Ogun, 'Ogun'),
        (Ondo, 'Ondo'),
        (Osun,  'Osun'),
        (Oyo, 'Oyo'),
        (Plateau, 'Plateau'),
        (Rivers, 'Rivers'),
        (Sokoto, 'Sokoto'),
        (Taraba, 'Taraba'),
        (Yobe, 'Yobe'),
        (Zamfara, 'Zamfara'),

    )

    time = models.DateTimeField(default = datetime.now, blank = True)
    name_of_accomodation = models.CharField(max_length=20)
    type_of_apartment = models.CharField(max_length=20, choices=Room, )
    Number_of_rooms = house_rent = models.IntegerField()
    house_rent = models.IntegerField()
    Landlord_number =models.CharField(max_length=200)
    availability = models.CharField(max_length=2, choices=Availability, default=Available,)
    State = models.CharField(max_length=20, choices=States, )
    City_or_town = models.CharField(max_length=200)
    Street = models.CharField(max_length=200)
    Size_of_room = models.CharField(max_length=200)
    Available_from = models.CharField(max_length=200)
    Toilet = models.CharField(max_length=20, choices=toilet,)
    Running_water = models.CharField(max_length=20, choices=water)
    Fenced = models.CharField(max_length=20, choices=fence)
    Parking_space = models.CharField(max_length=20, choices=park,)
    Account_name = models.CharField(max_length=200)
    Account_number = models.IntegerField()
    Payment_status = models.TextField(default='Not Paid')

    nearest_institution = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    house_image = models.ImageField()
    house_image2 = models.ImageField()
    house_image3 = models.ImageField()
    house_image4 = models.ImageField()
    house_image5 = models.ImageField()
    house_image6 = models.ImageField()
    house_image7 = models.ImageField(null=True, blank=True)
    house_image8 = models.ImageField( null=True, blank=True )
    house_image9 = models.ImageField( null=True, blank=True)
    house_image10 = models.ImageField( null=True, blank=True )
    house_image11 = models.ImageField( null=True, blank=True)
    house_image12 = models.ImageField( null=True, blank=True )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')

    def __str__(self):
        return self.name_of_accomodation

    def get_absolute_url(self):
        return reverse('search-detail', args=[str(self.id)])

    class Meta:
        ordering = ["-time"]


class Vip(models.Model):
    Flat = 'Flat'
    Self_contained = 'Self Contain'
    Bungalow = 'Bungalow'
    Mini_flat = 'Mini Flat'
    Duplex = 'Duplex'
    Student_lodge = 'Student Lodge'
    Student_hostel = 'Student Hostel'
    Others = 'Others'
    Looking_for_roommate = 'Looking for roommate'

    Room = (
        (Flat, 'Flat'),
        (Self_contained, 'Self contained'),
        (Bungalow, 'Bungalow'),
        (Mini_flat, 'Mini flat'),
        (Student_lodge, 'Student lodge'),
        (Student_hostel, 'Student hostel'),
        (Others, 'Others'),
        (Looking_for_roommate, 'Looking for roommate'),
    )


    Abuja = 'Abuja'
    Abia = 'Abia'
    Adamawa = 'Adamawa'
    Akwa_ibom = 'Akwa Ibom'
    Anambra = 'Anambra'
    Bauchi = 'Bauchi'
    Bayelsa = 'Bayelsa'
    Benue = 'Benue'
    Borno = 'Borno'
    Cross_River = 'Cross River'
    Delta = 'Delta'
    Ebonyi = 'Ebonyi'
    Edo = 'Edo'
    Ekiti = 'Ekiti'
    Enugu = 'Enugu'
    Gombe = 'Gombe'
    Imo = 'Imo'
    Jigawa = 'Jigawa'
    Kaduna = 'Kaduna'
    Kano = 'Kano'
    Katsina = 'Katsina'
    Kebbi = 'Kebbi'
    Kogi = 'Kogi'
    Kwara = 'Kwara'
    Lagos = 'Lagos'
    Nasarawa = 'Nasarawa'
    Niger = 'Niger'
    Ogun = 'Ogun'
    Ondo = 'Ondo'
    Osun = 'Osun'
    Oyo = 'Oyo'
    Plateau = 'Plateau'
    Rivers = 'Rivers'
    Sokoto = 'Sokoto'
    Taraba = 'Taraba'
    Yobe = 'Yobe'
    Zamfara = 'Zamfara'
    
    States = (
        (Abuja, 'Abuja'),
        (Abia, 'Abia'),
        (Adamawa, 'Adamawa'),
        (Akwa_ibom, 'Akwa ibom'),
        (Anambra, 'Anambra'),
        (Bauchi, 'Bauchi'),
        (Bayelsa, 'Bayelsa'),
        (Benue, 'Benue'),
        (Borno, 'Borno'),
        (Cross_River, 'Cross River'),
        (Delta, 'Delta'),
        (Ebonyi, 'Ebonyi'),
        (Edo, 'Edo'),
        (Ekiti, 'Ekiti'),
        (Enugu, 'Enugu'),
        (Gombe, 'Gombe'),
        (Imo, 'Imo'),
        (Jigawa, 'Jigawa'),
        (Kaduna, 'Kaduna'),
        (Kano, 'Kano'),
        (Katsina, 'Katsina'),
        (Kebbi, 'Kebbi'),
        (Kogi, 'Kogi'),
        (Kwara,'Kwara'),
        (Lagos,'Lagos'),
        (Nasarawa, 'Nasarawa'),
        (Niger,  'Niger'),
        (Ogun, 'Ogun'),
        (Ondo, 'Ondo'),
        (Osun,  'Osun'),
        (Oyo, 'Oyo'),
        (Plateau, 'Plateau'),
        (Rivers, 'Rivers'),
        (Sokoto, 'Sokoto'),
        (Taraba, 'Taraba'),
        (Yobe, 'Yobe'),
        (Zamfara, 'Zamfara'),

    )

    type_of_apartment = models.CharField(max_length=20, choices=Room, )
    Number_of_rooms = models.IntegerField()
    State = models.CharField(max_length=20, choices=States, )
    City_or_town = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='authorVip')

class paid(models.Model):
    client = models.CharField(max_length=20, )
    amount = models.IntegerField()
    accomodation = models.CharField(max_length=200 )

class Paids(models.Model):
    amount = models.IntegerField()
    myRef = models.TextField()
    username = models.TextField()
    

