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
                    ArtSocietyModel,
                    LanguageCustomsModel,
                    FuliruGalleyModel,
                    ViraGalleyModel)
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
admin.site.register(ArtSocietyModel)
admin.site.register(LanguageCustomsModel)
admin.site.register(FuliruGalleyModel)
admin.site.register(ViraGalleyModel)