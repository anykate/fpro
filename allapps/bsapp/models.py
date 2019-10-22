from django.db import models


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        db_table = 'framework'

    def __str__(self):
        return self.name
