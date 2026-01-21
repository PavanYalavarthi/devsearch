from django.db import models
# from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User

from uuid import uuid4
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    summary = models.TextField('Summary about user', default='New user on our platform!')
    location = models.TextField('Place of residence', default='Location is not specified.')
    about = models.TextField('About', default='Apparently, this user prefers to keep an air of mystery about them.')
    profile_image=models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/profile_pic.png')
    social_github=models.URLField(blank=True, null=True)
    social_linkedin=models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField('Skill name', max_length=20)
    description = models.TextField('Skill description')

    def __str__(self):
        return f'{self.profile} - {self.name} Skill'
