from django.db import models
# importing the basic user model we see in admin
from django.contrib.auth.models import User

# will store info

# Create your models here.


class UserProfileInfo(models.Model):
    # this is a model class to add in additional user info the default
    # user does not have
    # default has: username, email, password, first,lastname
    # here we are extending the class (e.g. profile picture)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    # if people post their porfolio projects on things they've been working on
    # not required to fill it out there will be no error
    portfolio_site = models.URLField(blank=True)

    # need to specify where to upload this to
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    # string name is our choice --> BUT NEED TO CREATE SUBDIRECTORY IN MEDIA FOLDER!!

    # to get something back if we print out the model
    def __str__(self):
        return self.user.username  # username is a default attribute
