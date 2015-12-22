from django.db.models import *
from django.contrib.auth.models import User
from django.contrib import admin

#from django.conf import settings

class Posts(Model):
    title = CharField(max_length = 40)
    body = TextField()
    category = CharField(max_length = 20)
    created = DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return self.title

#class UserProfile(Model):
#    avatar = ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
#    user   = OneToOneField(User, related_name="profile")


class Comments(Model):
    author = ForeignKey(User)
    title = CharField(max_length = 30)
    body = TextField()
    created = DateTimeField(auto_now_add = True)
    post = ForeignKey(Posts, related_name="comments",  blank=True, null=True)


    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return self.title

    #def __unicode__(self):
    #    return unicode(self.user)
