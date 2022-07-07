from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class CategoryTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(CategoryTag, blank=True)
    image = models.ImageField(upload_to='',
                              validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])])
    image_thumb = ImageSpecField(source='image', processors=[ResizeToFit(183, 122)],
                                 format='JPEG', options={'quality': 60})

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = "Posts"

    def __str__(self):
        return f'id: {self.id}, title: {self.title}'

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
