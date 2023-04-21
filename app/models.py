from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Movie(models.Model):
    title = models.CharField(_("title"), max_length=255)
    genres = models.CharField(_("genres"), max_length=300)
    character_name_and_cast = models.CharField(_("character name and cast"), max_length=400)
    overview = models.CharField(_("overview"), max_length=500)
    release_date = models.DateField(_("release date"))
    tagline = models.CharField(_("tagline"), max_length=300)
    vote_average = models.FloatField(_("average vote"))
    vote_count = models.IntegerField(_("vote count"))


    def __str__(self):
        return self.title