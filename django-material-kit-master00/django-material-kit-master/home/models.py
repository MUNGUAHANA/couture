from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Permission
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class ModeTopic(models.TextChoices):    
        TENDANCE = "Tendance"    
        CULTUREL = "Culturel"    
        HAUTECOUTURE = "Hautecouture"
class SpecTopic(models.TextChoices):    
        COUTUREHOMME = "CoutureHomme"    
        COUTUREFEMME = "CoutureFemme"    
        COUTUREMIXTE = "CoutureMixte"


class patron(models.Model):
        title = models.CharField(unique=True, max_length=100)
        nomode = models.CharField(max_length=30)
        topic = models.CharField(max_length=50, choices=ModeTopic.choices)
        image = models.ImageField(upload_to="blog_images", null=True, blank=True)
        explain = models.TextField(blank=True) 
        is_published = models.BooleanField(default=False) 
        pub_date = models.DateField(null=True, blank=True) 
        def __str__(self):        
                return self.title + ("*" if self.is_published else "")

        def get_absolute_url(self):        
                return' ' + str(self.id) + "/"


class MaisonCouture(models.Model):
        nom = models.CharField(max_length=100)
        adresse = models.CharField(max_length=200)
        photo_atel = models.ImageField(upload_to="blog_images", null=True, blank=True)
        telephone = models.CharField(max_length=15)
        specialisation = models.CharField(max_length=50, choices=SpecTopic.choices)
        email = models.EmailField()
        site_web = models.URLField()
        description = models.TextField()
        date_creation = models.DateField()
        def compte_visit(self):
              return self.visiteurs.count()

        def __str__(self):        
                return self.nom
        def get_absolute_url(self):
                return reverse('blog:maison-detail', kwargs={'maison_id': self.id})
            
##----------------------------------------------------------------------------------------------------------------------


class commande (models.Model):
        nom_du_client = models.CharField( max_length=50)
        nom_du_modele = models.CharField( max_length=50)
        vos_mesures = models.TextField(max_length=100)
        date_commande = models.DateField()

class client(models.Model):
        nom_complet = models.CharField(max_length=100)
        contact = models.CharField(max_length=100)
        adresse = models.CharField(max_length=100)
        username = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
    
class demande(models.Model):
        nom_couturier = models.CharField(max_length=100)
        nom_du_contenu = models.CharField(max_length=100)
        date= models.DateField()
        
class modele(models.Model):
        image_du_modele = models.ImageField(upload_to="blog_images", null=True, blank=True)
        nom_modele = models.CharField(max_length=100)
        prix = models.IntegerField()
        couturier = models.CharField(max_length=50)
        mesures_a_prendre = models.TextField(max_length=100)
        tissus_possible = models.TextField(max_length=100)
        quantite_necessaire_de_tissus=models.IntegerField()
        
        
        
        
class contenu(models.Model):
        titre_contenu = models.CharField(max_length=100)
        photo = models.ImageField(upload_to="blog_images", null=True, blank=True)
        comment_faire = models.FileField(upload_to="blog_videos", null=True, blank=True)
        par_le_couturier = models.CharField(max_length=50)
        description = models.TextField(max_length=100)
        #is_published = models.BooleanField(default=False) 
        tissu_adapte = models.TextField(max_length=100)
        
        
        
class couturier(models.Model):
    nom_complet = models.CharField(max_length=30)   
    nom_populaire = models.CharField(max_length=30)
    contact = models.IntegerField(default=0)
    email = models.CharField(max_length=30)
    #topic = models.CharField(max_length=50, choices=SpecTopic.choices)
    nom_atelier = models.CharField(max_length=30)
    adresse_atelier = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="blog_images", null=True, blank=True)
    password = models.CharField(max_length=128, default="password")
    

    def __str__(self):        
        return self.nom_complet
    @property
    def recherche_nom_complet(self):
        return self.nom_complet
    
class Comment(models.Model):    
    post = models.ForeignKey(patron, on_delete=models.CASCADE)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    Ajouter_commentaire = models.CharField(max_length=1000)    
    time = models.DateTimeField(auto_now_add=True)

class Visite(models.Model):
    nom = models.CharField(max_length=100)
    date_visite = models.DateField()

#-------------------------------------------------------------------------------------------------------------------


