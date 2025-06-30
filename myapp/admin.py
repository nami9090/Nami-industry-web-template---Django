from django.contrib import admin
from .models import(
                    Feature, 
                    Produit, 
                    More_Culture,
                    StepModel, 
                    TestimonialModel, 
                    TeamModel, 
                    Icons, 
                    LocationModel, 
                    EmailModel, 
                    HourOfOperation,
                    AboutImageModel,
                    ContactModel,
                    SuggestModel, 
                    Galleries,
                    GalleryImages,
                    FeatureDetails)
# Register your models here.
admin.site.register(Feature)
admin.site.register(Produit)
admin.site.register(More_Culture)
admin.site.register(StepModel)
admin.site.register(TestimonialModel)
admin.site.register(TeamModel)
admin.site.register(Icons)
admin.site.register(LocationModel)
admin.site.register(EmailModel)
admin.site.register(HourOfOperation)
admin.site.register(AboutImageModel)
admin.site.register(ContactModel)
admin.site.register(SuggestModel)
admin.site.register(Galleries)
admin.site.register(GalleryImages)
admin.site.register(FeatureDetails)