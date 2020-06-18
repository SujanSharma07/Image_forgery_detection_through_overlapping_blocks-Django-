from django.db import models

class detectedimages(models.Model):
    id = models.AutoField(primary_key=True)
    sample_image = models.ImageField(upload_to='images', default="1.jpg",help_text="JPG or PNG")

    def __str__(self):
        return "image"+str(self.id)

# Create your models here.
