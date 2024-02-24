from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField





class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True)
    image = ImageField()
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.text[0:100]



def compress(image):
    im = Image.open(image)
    out_put_size = (300,300)
    im.thumbnail(out_put_size)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im = im.resize([500,500])
    #resize image
    im = im.convert("RGB")
    im = im.save(im_io,'JPEG', quality=50) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image

class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profiles')
    
    def save(self, *args, **kwargs):
      #image compression start
      if self.image:
         # call the compress function
         new_image = compress(self.image)
         # set self.image to new_image
         self.image = new_image
      #image compression end 
      super(Profile,self).save(*args, **kwargs)



