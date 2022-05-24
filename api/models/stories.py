from django.db import models
from django.contrib.auth import get_user_model
import django.utils.timezone


# Create your models here.
class Story(models.Model):
  """Doc String"""
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=255)
  story = models.TextField()
  is_active = models.BooleanField(default=True)
  is_public = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The Story named '{self.title}' is {self.story} in color. It is {self.owner} that it is ripe."

  def as_dict(self):
    """Returns dictionary version of Stories models"""
    return {
        'id': self.id,
        'title': self.title,
        'story': self.story,
        'owner': self.owner
    }
