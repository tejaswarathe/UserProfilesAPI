from django.db import models
from stdimage.models import StdImageField


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    picture = StdImageField(blank=True, null=True,
                            upload_to = 'profilepictures/', 
                            variations={
                                        'detailthumbnail':(200,200, True),
                                        'listthumbnail':(100,100,True)
                                        })

    def __str__(self):
        return self.name