# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


# class Classification(models.Model):
#     class_id = models.AutoField(primary_key=True)
#     learn_classification = models.CharField(max_length=50)


class Words(models.Model):
    word_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=50)
    word_explanation_ch = models.CharField(max_length=400)
    word_explanation_en = models.CharField(max_length=400)
    example_sentence = models.CharField(max_length=400)
    word_classification = models.CharField(max_length=50)


class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_tel = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_info = models.TextField()
    learn_classification = models.CharField(max_length=50)
    learn_per_day = models.IntegerField(11)


class UserWordsComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(11)
    word_id = models.IntegerField(11)
    comments = models.TextField()
    if_open = models.IntegerField(1)  # true 1 ; false 0


class UserLearn(models.Model):
    learn_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(11)
    word_id = models.IntegerField(11)


