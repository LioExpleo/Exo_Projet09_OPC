from django.db import models
# Create your models here.
# Création de la classe Band qui hérite du modèle models. Model qui est la classe de base du modèle django
# Ensuite, nous ajoutons un attribut de classe à notre classe name. À cet attribut, nous attribuons unCharField,
# qui est l'abréviation de Character Field. Il s'agira d'un champ qui stocke des données
# de type caractère/texte/chaîne, ' \'ce qui est le type de données approprié pour un nom.


class Band(models.Model):
    name = models.fields.CharField(max_length=100)

# Le modèle avec django est capable de stocker ses données dans une base de donnees
# nous avons créé notre base de données dans le chapitre sur la configuration.
# Mais cette base de données ne sait encore rien de notre modèle de bande.
# Et c'est là que les migrations entrent en jeu.


