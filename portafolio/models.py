from django.db import models
from django.db.models import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    tittle = CharField(max_length=50)
    description = CharField(max_length=400)
    image = ImageField(upload_to='portafolio/images/')
    url = URLField(blank=True)

    def __str__(self) -> str:
        return self.tittle
