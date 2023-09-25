from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
# from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models



   
# class Article(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     another = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
#     author = models.CharField(max_length=50)
#     different_id = models.IntegerField(default=1)


#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         return reverse("article_detail", args=[str(self.id)])
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    another = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Article,related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.writer)+" " + str(self.id)
    
    def get_absolute_url(self):
        return reverse("article_list")
    