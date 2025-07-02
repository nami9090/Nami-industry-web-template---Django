from django.db import models
from datetime import date

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    icons = models.CharField(max_length=50)
    details = models.CharField(max_length=10000000)
    iskingdom = models.BooleanField(default=True)
    image_pic = models.ImageField(upload_to='images/')
    

class FeatureDetails(models.Model):
    feature = models.ForeignKey(Feature, related_name='detail', on_delete=models.CASCADE)
    completeName = models.CharField(max_length=100)
    yearOfTaken = models.DateField()
    encore_vivant = models.BooleanField(default=False)
    yearOfDeath = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        if self.encore_vivant:
            annees = date.today().year - self.yearOfTaken.year
            return f"{self.completeName}, au pouvoir depuis {self.yearOfTaken.year} ({annees} ans de règne)"
        elif self.yearOfDeath:
            return f"{self.completeName} de {self.yearOfTaken.year} à {self.yearOfDeath.year} soit {self.yearOfDeath.year - self.yearOfTaken.year} ans de règne"
        else:
            return f"{self.completeName}, au pouvoir depuis {self.yearOfTaken.year}"
        
class FeatureBenefit(models.Model):
    feature = models.ForeignKey(Feature, related_name='benefit', on_delete=models.CASCADE)
    iconStr = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.title} benefit of {self.feature.name}"
    

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
    def __str__(self):
        return self.name

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


class Galleries(models.Model):
    title = models.CharField(max_length=100)
    subtile = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

class GalleryImages(models.Model):
    gallery = models.ForeignKey(Galleries, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=1000)
    def __str__(self):
        return f"Image de {self.gallery.title}"


class ContactModel(models.Model):
    first_name = models.CharField(max_length=100)
    email_address = models.EmailField(blank=False)
    subject = models.CharField(max_length=100)
    write_message = models.CharField(max_length=1000)

