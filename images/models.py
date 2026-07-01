from django.db         import models
from django.conf       import settings
from django.utils.text import slugify

# Create your models here.
class Image(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'images_created', on_delete =  models.CASCADE)

    users_like  = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'images_liked', blank = True ) # 1 user can like many images and 1 image can be like by many users.

    title       = models.CharField(max_length = 250)
    slug        = models.SlugField(max_length = 200, blank = True)
    url         = models.URLField(max_length = 2000)
    image       = models.ImageField(upload_to = "images/%Y/%m/%d")
    description = models.TextField(blank = True)
    created     = models.DateTimeField(auto_now_add = True)

    class Meta:
        indexes  =  [
                        models.Index(fields= ['-created']),

                    ]
        ordering = ['created']

    #Overriding the save() function of Image class to automatically generate the slug based on the value of "text" field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


def __str__(self):

    return self.title


