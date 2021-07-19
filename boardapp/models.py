from django import template
from accountapp.models import User
from django.db import models

import datetime

register = template.Library()


class surveyModel(models.Model):
    Category_choice = (('IT/과학', 'IT/과학'), ('경영/창업', '경영/창업'), ('예술', '예술'),
                       ('인문/사회', '인문/사회'), ('심리학', '심리학'), ('뷰티/미용', '뷰티/미용'))
    category = models.CharField(max_length=30, choices=Category_choice, verbose_name="카테고리", default='IT/과학') # default를 관심분야로 수정
    title = models.CharField(max_length=100, verbose_name="설문제목")
    link = models.URLField(max_length=255, verbose_name="설문링크")
    description = models.TextField(verbose_name="상세설명")
    dueDate = models.DateField(verbose_name="마감기한")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='found_author', null=True)
    registered_date = models.DateTimeField(verbose_name="등록시간", auto_now_add=True)
    d_day = models.IntegerField(verbose_name="디데이")

    class Meta:
        db_table = "Survey_List"
        verbose_name = "설문조사"
        verbose_name_plural = "설문조사_리스트"
        ordering = ('-registered_date',)

    def __str__(self):
        return self.title

    def d_day_Counter(self):
        today = datetime.date.today()
        self.d_day = self.dueDate - today
        self.save()
