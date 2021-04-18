from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

class theme(models.Model):
    name = models.CharField(max_length=250)
    theme_slug = models.SlugField(max_length=255,default='')

    def __str__(self):
        return self.name

    def save(self, *args,**kwargs):
        self.theme_slug = slugify(self.name)
        super().save(*args,**kwargs)

class post(models.Model):
    theme = models.ForeignKey(theme,on_delete=models.CASCADE)
    post_views=models.IntegerField(default=0)
    name = models.CharField(max_length=250)
    post_slug = models.SlugField(max_length=255,default='')
    description = models.TextField()
    Img = models.ImageField(upload_to='photos')
    Img2 = models.ImageField(upload_to='photos',blank=True)
    Img3 = models.ImageField(upload_to='photos',blank=True)
    Img4 = models.ImageField(upload_to='photos',blank=True)
    Img5 = models.ImageField(upload_to='photos',blank=True)
    Img6 = models.ImageField(upload_to='photos',blank=True)
    Img7 = models.ImageField(upload_to='photos',blank=True)
    Img8 = models.ImageField(upload_to='photos',blank=True)
    Img9 = models.ImageField(upload_to='photos',blank=True)
    Img10 = models.ImageField(upload_to='photos',blank=True)
    video = models.FileField(upload_to='videos',validators=[FileExtensionValidator(allowed_extensions=['mp4'])],blank=True)
    file = models.FileField(upload_to='files',blank=True)
    audio = models.FileField(upload_to='audio',blank=True,validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    link = models.URLField(max_length=5000,blank=True)

    image_medium = ImageSpecField(source='Img',processors=[ResizeToFill(220,220)]
    ,format='JPEG',options={'quality': 60})

    def __str__(self):
        return self.name

    def save(self, *args,**kwargs):
        self.post_slug = slugify(self.name)+ "-" + str(self.theme.theme_slug)
        super().save(*args,**kwargs)

class comment (models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
