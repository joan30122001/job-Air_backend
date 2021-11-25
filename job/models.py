from django.db import models
from user.models import User
from django.utils.translation import gettext as _

# Create your models here.

class Offer(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("titre de l'offre")),
    domain = models.CharField(max_length=255, verbose_name=_("domaine dans lequel l'offre cadre")),
    region = models.CharField(max_length=100, verbose_name=_("région dans laqu'elle l'offre est disponible")),
    description = models.TextField(verbose_name=_("description de l'offre")),
    condition = models.TextField(verbose_name=_("condition de l'offre")),
    begin_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name=_("date de début de l'offre")),
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name=_("date de fin de l'offre")),
    user = models.ForeignKey("user.User", verbose_name=_("utilisateur"), on_delete=models.CASCADE)



class UserOffer(models.Model):
    offer = models.ForeignKey("Offer", verbose_name=_("Offre"), on_delete=models.CASCADE),
    user = models.ForeignKey("user.User", verbose_name=_("utilisateur"), on_delete=models.CASCADE)



class Cv(models.Model):
    document = models.TextField(verbose_name=_("contenu du cv")),
    user = models.ForeignKey("user.User", verbose_name=_("utilisateur"), on_delete=models.CASCADE)
