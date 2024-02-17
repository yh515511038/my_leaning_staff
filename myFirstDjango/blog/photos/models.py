from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Adjust, SmartResize, ResizeToFit
from PIL import Image
import os

# Create your models here.
class BanBan(models.Model):
    image = ProcessedImageField(
        upload_to="banban",
        processors=[
            Adjust(contrast=1.2, sharpness=1.1),
            SmartResize(width=450, height=600)
        ],
        format='JPEG',
        options={'quality': 60},
        null=True,
    )
    # def save(self, *args, **kwargs):
    #     if self.image:
    #         # path_list = self.image.path.split('\\')
    #         # prefix_dir = '\\'.join(path_list[:-1])
    #         # file_name = path_list[-1]
    #         # img = Image.open(os.path.join(prefix_dir, 'banban', file_name))
    #         img = Image.open(self.image.path)
    #         width, height = img.size
    #         aspect_ratio = width / height

    #         if aspect_ratio > 1:
    #             self.image.processors[1].height = 600
    #             self.image.processors[1].width = None
    #         else:
    #             self.image.processors[1].height = None
    #             self.image.processors[1].width = 450
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Banban - {str(self.id)}"
    
    def get_absolute_url(self):
        return reverse("banban", kwargs={"pk": self.pk})
