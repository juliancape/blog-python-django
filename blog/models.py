from django.db import models
from django.db.models import CharField, URLField, TextField, DateField
from django.db.models.fields.files import ImageField
import datetime

class Post(models.Model):
    tittle = CharField(max_length=50)
    description = TextField()
    image = ImageField(upload_to='blog/images/')
    date = DateField(default= datetime.date.today)
