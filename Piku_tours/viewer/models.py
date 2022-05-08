from django.db import models

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






