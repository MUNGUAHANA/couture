from django.contrib import admin

# Register your models here.
# import the models 
from .models import *
# register each model with the admin site

admin.site.register(Visite)
admin.site.register(Comment)
admin.site.register(patron)
admin.site.register(couturier)
admin.site.register(MaisonCouture)
#-------------------------------------------------------------
admin.site.register(client)
admin.site.register(commande)
admin.site.register(demande)
admin.site.register(contenu)
admin.site.register(modele)

