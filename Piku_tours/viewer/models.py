from django.db import models
from django.contrib.auth.models import User

LANGUAGE_OPTIONS = [
    ('Unknown local', 'Unknown local'),
    ('Chinese', 'Chinese'),
    ('Latin', 'Latin'),
    ('Sanskrit', 'Sanskrit'),
    ('No talking!', 'No talking!'),
    ('Mostly just cursing', 'Mostly just cursing')
]

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Travel(models.Model):
    name = models.CharField(max_length=50)
    country = models.ManyToManyField(Country, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True, blank=True)
    duration_in_days = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    guide_language = models.CharField(max_length=20, null=True, blank=True, choices=LANGUAGE_OPTIONS)
    cover = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    alergic = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

STARS_OPTIONS = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]

class Rate(models.Model):
    num_stars = models.PositiveIntegerField(choices=STARS_OPTIONS)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    review = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.travel.name + ' - ' + self.profile.user.username



