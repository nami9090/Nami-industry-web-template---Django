from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    icons = models.CharField(max_length=50)
    details = models.CharField(max_length=500)
    image_pic = models.ImageField(upload_to='images/')

class Produit(models.Model):
    nom = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

class More_Culture(models.Model):
    name = models.CharField(max_length=100)
    fonction = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image_pic = models.ImageField(upload_to='images/')

class StepModel(models.Model):
    step_number = models.CharField(max_length=50)
    step_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    step_icon = models.CharField(max_length=50)

class TestimonialModel(models.Model):
    name = models.CharField(max_length=50)
    fonction = models.CharField(max_length=50)
    first_paragraph = models.CharField(max_length=1000)
    second_paragraph = models.CharField(max_length=1000)
    image_pic = models.ImageField(upload_to='images/')

class TeamModel(models.Model):
    name = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    facebook_link = models.CharField(max_length=10000)
    twitter_link = models.CharField(max_length=10000)
    linkedin_link = models.CharField(max_length=10000)
    image_pic = models.ImageField(upload_to='images/')

class Icons(models.Model):
    name = models.CharField(max_length=10000)
    link = models.CharField(max_length=10000)

class SuggestModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000000)

class AddressModel(models.Model):
    location_address = models.CharField(max_length=1000)
    email_address = models.CharField(max_length=1000)
    hours_of_operations = models.CharField(max_length=1000)

class LocationModel(models.Model):
    location_name = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)

class EmailModel(models.Model):
    email_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=1000)

class HourOfOperation(models.Model):
    hours_name = models.CharField(max_length=100)
    days_works = models.CharField(max_length=1000)

class AboutImageModel(models.Model):
    placeholder = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

class ArtSocietyModel(models.Model):
    title = models.CharField(max_length=100)
    subtile = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

class LanguageCustomsModel(models.Model):
    title = models.CharField(max_length=100)
    subtile = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

class FuliruGalleyModel(models.Model):
    title = models.CharField(max_length=100)
    subtile = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

class ViraGalleyModel(models.Model):
    title = models.CharField(max_length=100)
    subtile = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
