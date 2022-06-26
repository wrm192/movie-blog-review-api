from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=500, default="")
    created = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=2)
    review_text = models.CharField(max_length=5000, default="")
    created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.review_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Comment(models.Model):
#     review = models.ForeignKey(Review, on_delete=models.CASCADE, default=1)
#     pub_date = models.DateTimeField('date published')
#     upvotes = models.IntegerField(default=0)
#     comment_text = models.CharField(max_length=1000, default="")

#     def __str__(self):
#         return self.comment_text
