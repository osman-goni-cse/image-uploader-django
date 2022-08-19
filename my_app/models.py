from image_uploader.settings import TIME_ZONE
from django.db import models
from PIL import Image as Im

# Create your models here.

from .validators import validate_file_extension, validate_file_size, validate_image_dimension

class Image(models.Model):
  text = models.TextField(max_length=1000, default="What's up")
  photo = models.ImageField(upload_to="myimage", validators=[validate_file_size, validate_file_extension, validate_image_dimension])
  date = models.DateTimeField(null=True)
  event = models.DateTimeField(null=True)

  def save(self): # new
    super().save()
    img = Im.open(self.photo.path)
    print(img.height)
    # resize it
    if img.height > 300 or img.width > 300:
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.photo.path)
  