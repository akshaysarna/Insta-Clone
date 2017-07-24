# -*- coding: utf-8 -*-


from django.db import models
import uuid
# Create your models here.
class UserModel(models.Model):
    email = models.EmailField(blank=True, max_length=70)
    username =models.CharField(max_length=30 , unique=True, blank=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    password = models.CharField(max_length=40, blank=True)
    verified_mobile= models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now = True)

class SessionToken(models.Model):
    user = models.ForeignKey(UserModel)
    session_token = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid.uuid4()

class PostModel(models.Model):
    user =models.ForeignKey(UserModel)
    image= models.FileField(upload_to="user_images")
    image_url = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    has_liked=False

    @property
    def like_count(self):
        return len(LikeModel.objects.filter(post=self))

    @property
    def comments(self):
        return CommentModel.objects.filter(post=self).order_by('-created_on')

class LikeModel(models.Model):
    user = models.ForeignKey(UserModel)
    post = models.ForeignKey(PostModel)
    created_on= models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class CommentModel(models.Model):
	user = models.ForeignKey(UserModel)
	post = models.ForeignKey(PostModel)
	comment_text = models.CharField(max_length=555)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
