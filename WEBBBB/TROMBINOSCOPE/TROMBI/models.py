from django.db import models


# Modèle pour l'étudiant
class Etudiant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=15)
    adresse = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    def __str__(self):
        return f"{self.nom} {self.prenom}"


# Modèle pour le CV
class CV(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='cvs')

    def __str__(self):
        return self.titre


# Modèle pour l'expérience
class Experience(models.Model):
    poste = models.CharField(max_length=255)
    entreprise = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.poste} à {self.entreprise}"


# Table d'association entre CV et expérience
class Inclure(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='experiences')
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='cvs')


# Modèle pour la formation
class Formation(models.Model):
    diplome = models.CharField(max_length=255)
    etablissement = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.diplome


# Table d'association entre CV et formation
class Associer(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='formations')
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name='cvs')


# Modèle pour la langue
class Langue(models.Model):
    libelle = models.CharField(max_length=255)
    niveau = models.CharField(max_length=255)

    def __str__(self):
        return self.libelle


# Table d'association entre CV et langue
class Rajouter(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='langues')
    langue = models.ForeignKey(Langue, on_delete=models.CASCADE, related_name='cvs')


# Modèle pour la compétence
class Competence(models.Model):
    libelle = models.CharField(max_length=255)
    niveau = models.CharField(max_length=255)

    def __str__(self):
        return self.libelle


# Table d'association entre étudiant et compétence
class Posseder(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='competences')
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE, related_name='etudiants')


# Modèle pour le projet
class Projet(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titre


# Table d'association entre étudiant et projet
class Participer(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='projets')
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='etudiants')


