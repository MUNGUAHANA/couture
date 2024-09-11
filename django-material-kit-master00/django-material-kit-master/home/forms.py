from django import forms

from .models import *

class SearchForm(forms.Form):
    query = forms.CharField(label='Entrer le nom complet pour rechercher ', max_length=100)


class PatronForm(forms.ModelForm):
    class Meta:
        model = patron
        fields = [ 'title', 'nomode', 'image', 'explain', 'topic', 'is_published', 'pub_date', ]

class couturierForm(forms.ModelForm):
    class Meta:
        model = couturier
        fields = [ 'nom_complet', 'nom_populaire', 'contact', 'email', 'nom_atelier', 'adresse_atelier', 'photo', ]

class MaisonCoutureForm(forms.ModelForm):
    class Meta:
        model = MaisonCouture
        fields = ['nom' ,'adresse', 'photo_atel', 'telephone','specialisation','email','site_web','description','date_creation']

class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'Ajouter_commentaire' ]
#----------------------------------------------------------------------------------------------------------------------------------------



class modeleForm(forms.ModelForm):
    class Meta:
        model = modele
        fields = [ 'image_du_modele', 'nom_modele', 'prix', 'couturier', 'mesures_a_prendre', 'tissus_possible', 'quantite_necessaire_de_tissus']

class contenuForm(forms.ModelForm):
    class Meta:
        model = contenu
        fields = [ 'titre_contenu', 'photo', 'comment_faire', 'par_le_couturier', 'description', 'tissu_adapte']

class clientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ['nom_complet' ,'adresse', 'contact', 'username','password']

class commandeForm(forms.ModelForm):
    class Meta:
        model = commande
        fields = [ 'nom_du_client', 'nom_du_modele', 'vos_mesures','date_commande' ]
        
class demandeForm(forms.ModelForm):
    class Meta:
        model = demande
        fields = [ 'nom_couturier', 'nom_du_contenu', 'date' ]