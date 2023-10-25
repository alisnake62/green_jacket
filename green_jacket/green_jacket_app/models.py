
from django.db.models import F, Sum, Case, When

from django.db import models

class UserCustom(models.Model):
    name = models.CharField(max_length=50)
    dark_mode = models.BooleanField(default=False)

class BuildProcess(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=5000)
    score = models.IntegerField()

class Material(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=5000)
    score = models.IntegerField()

class Country(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=5000)
    score = models.IntegerField()

class Brand(models.Model):
    name    = models.CharField(max_length=50)
    image_url = models.CharField(max_length=5000)

    def get_score(self):
        score = 0
        score_count = 0
        for brand_model in self.brand_models.all():
            score += brand_model.get_score()
            score_count += 1
        return int(score / score_count)

class BrandModel(models.Model):
    date    = models.DateField()
    name    = models.CharField(max_length=50)
    type    = models.CharField(max_length=50)
    link    = models.CharField(max_length=500)
    material= models.ForeignKey(Material, related_name="brand_models", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name="brand_models", on_delete=models.CASCADE)
    build_process = models.ForeignKey(BuildProcess, related_name="brand_models", on_delete=models.CASCADE)
    brand   = models.ForeignKey(Brand, related_name="brand_models", on_delete=models.CASCADE)
    image_url = models.CharField(max_length=5000)
    tarif = models.FloatField()
    favorite = models.BooleanField(default=False)

    def get_score(self):

        return self.material.score + self.country.score + self.build_process.score

class Favorite(models.Model):
    user = models.ForeignKey(UserCustom, related_name="favorites", on_delete=models.CASCADE)
    brand_model = models.ForeignKey(BrandModel, related_name="favorites", on_delete=models.CASCADE)