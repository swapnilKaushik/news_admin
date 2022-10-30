from django.db import models
from django.core.validators import FileExtensionValidator


class Headline(models.Model):
    headline = models.CharField(max_length=150)
    content = models.TextField()
    categories = models.ManyToManyField('categories.Category', blank=True)
    place = models.CharField(max_length=60, null=True, blank=True)
    city = models.ForeignKey(
        'location.City', blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.headline


class HeadlineImage(models.Model):
    headline = models.ForeignKey(
        Headline, related_name='images_headline', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='headline_img')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.headline.headline


class HeadlineVideo(models.Model):
    headline = models.ForeignKey(
        Headline, related_name='videos_headline', on_delete=models.CASCADE)
    video = models.FileField(blank=True, upload_to='headline_vid',
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.headline.headline
