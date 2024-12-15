from django.contrib import admin
from .models import (
    Etudiant, CV, Experience, Inclure,
    Formation, Associer, Langue, Rajouter,
    Competence, Posseder, Projet, Participer
)

# Configuration pour Etudiant
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'tel')
    search_fields = ('nom', 'prenom', 'email')


# Configuration pour CV
@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('titre', 'etudiant')
    search_fields = ('titre',)
    list_filter = ('etudiant',)


# Configuration pour Experience
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('poste', 'entreprise', 'date_debut', 'date_fin')
    search_fields = ('poste', 'entreprise')
    list_filter = ('date_debut', 'date_fin')


# Configuration pour Inclure (CV - Experience)
@admin.register(Inclure)
class InclureAdmin(admin.ModelAdmin):
    list_display = ('cv', 'experience')
    search_fields = ('cv__titre', 'experience__poste')


# Configuration pour Formation
@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('diplome', 'etablissement', 'date_debut', 'date_fin')
    search_fields = ('diplome', 'etablissement')
    list_filter = ('date_debut', 'date_fin')


# Configuration pour Associer (CV - Formation)
@admin.register(Associer)
class AssocierAdmin(admin.ModelAdmin):
    list_display = ('cv', 'formation')
    search_fields = ('cv__titre', 'formation__diplome')


# Configuration pour Langue
@admin.register(Langue)
class LangueAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'niveau')
    search_fields = ('libelle',)
    list_filter = ('niveau',)


# Configuration pour Rajouter (CV - Langue)
@admin.register(Rajouter)
class RajouterAdmin(admin.ModelAdmin):
    list_display = ('cv', 'langue')
    search_fields = ('cv__titre', 'langue__libelle')


# Configuration pour Competence
@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'niveau')
    search_fields = ('libelle',)
    list_filter = ('niveau',)


#list_display : Définit les colonnes affichées dans la liste admin.
#search_fields : Permet de rechercher dans des champs spécifiques.
#list_filter : Ajoute des filtres sur des champs comme les dates ou les niveaux.





# Configuration pour Posseder (Etudiant - Competence)
@admin.register(Posseder)
class PossederAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'competence')
    search_fields = ('etudiant__nom', 'competence__libelle')


# Configuration pour Projet
@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'date_fin')
    search_fields = ('titre',)
    list_filter = ('date_debut', 'date_fin')


# Configuration pour Participer (Etudiant - Projet)
@admin.register(Participer)
class ParticiperAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'projet')
    search_fields = ('etudiant__nom', 'projet__titre')
