# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import *
import simplejson as json
# Create your views here.


def index(request):
    return render(request, 'index.html')


def save_configs(request):  # POST 设置用户信息
    if request.method == 'POST':
        req = json.loads(request.body)
        try:
            UserInfo.objects.filter(user_id=req['userId']).update(learn_classification=req['type']
                                                                  , learn_per_day=req['count'])
        except :
            return HttpResponse(json.dumps({"info": "no"}))
        return HttpResponse(json.dumps({"info": "yes"}))
    else:
        return HttpResponse(json.dumps({"info": "no"}))


def load_configs(request, user_id):  # GET 获取用户配置信息
    user = UserInfo.objects.get(user_id=user_id)
    configs = {'type': user.learn_classification, 'count': user.learn_per_day}
    return HttpResponse(json.dumps(configs))


def load_words_through_configs(request, user_id):  # GET 获取单词
    if request.method == "GET":
        try:
            user_info = UserInfo.objects.get(user_id=user_id)
            learned_words = UserLearn.objects.filter(user_id=user_id).all()
            word_ids = []
            for learned_word in learned_words:
                word_ids.append(learned_word.word_id)
            res = Words.objects.filter(word_classification=user_info.learn_classification).exclude(word_id__in=word_ids).all()[0: user_info.learn_per_day]

            results = []
            for one in res:
                ele = {"wordId": one.word_id, "word": one.word, "chinese": one.word_explanation_ch, "english": one.word_explanation_en, "example": one.example_sentence}
                results.append(ele)
            return HttpResponse(json.dumps(results))
        except:
            return HttpResponse(json.dumps([{"info": "no"}]))
    else:
        return HttpResponse(json.dumps([{"info": "no"}]))


def see_open_notes(request, word_id):  # GET 查看共享笔记
    if request.method == "GET":
        try:
            results = []
            res = UserWordsComment.objects.filter(word_id=word_id).filter(if_open=1).all()
            for one in res:
                ele = {"comments": one.comments}
                results.append(ele)
            return HttpResponse(json.dumps(results))
        except:
            return HttpResponse(json.dumps([{"info": "no"}]))
    else:
        return HttpResponse(json.dumps([{"info": "no"}]))


def save_note(request):  # POST 存储自己笔记
    if request.method == "POST":
        try:
            req = json.loads(request.body)
            # 暂不考虑用户 设置用户id 为1
            instance = UserWordsComment(user_id=1, word_id=req['wordId'], comments=req['comments'], if_open=0)
            instance.save()
            return HttpResponse(json.dumps({"info": "yes"}))
        except:
            return HttpResponse(json.dumps({"info": "no"}))
    else:
        return HttpResponse(json.dumps({"info": "no"}))


def save_and_open_note(request):  # POST 存储并设置共享
    if request.method == "POST":
        try:
            req = json.loads(request.body)
            # 暂不考虑用户 设置用户id 为1
            instance = UserWordsComment(user_id=1, word_id=req['wordId'], comments=req['comments'], if_open=1)
            instance.save()
            return HttpResponse(json.dumps({"info": "yes"}))
        except:
            return HttpResponse(json.dumps({"info": "no"}))
    else:
        return HttpResponse(json.dumps({"info": "no"}))


def mark_learned_words(request):  # POST 按天标记学过的单词
    if request.method == "POST":
        try:
            req = json.loads(request.body)
            word_ids = req['wordIds']
            user_id = req['userId']
            for word_id in word_ids:
                instance = UserLearn(user_id=user_id, word_id=word_id)
                instance.save()
            return HttpResponse(json.dumps({"info": "yes"}))
        except:
            return HttpResponse(json.dumps({"info": "no"}))
    else:
        return HttpResponse(json.dumps({"info": "no"}))
