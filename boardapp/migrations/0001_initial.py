# Generated by Django 3.1.5 on 2021-07-19 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='surveyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('IT/과학', 'IT/과학'), ('경영/창업', '경영/창업'), ('예술', '예술'), ('인문/사회', '인문/사회'), ('심리학', '심리학'), ('뷰티/미용', '뷰티/미용')], default='IT/과학', max_length=30, verbose_name='카테고리')),
                ('title', models.CharField(max_length=100, verbose_name='설문제목')),
                ('link', models.URLField(max_length=255, verbose_name='설문링크')),
                ('description', models.TextField(verbose_name='상세설명')),
                ('dueDate', models.DateField(verbose_name='마감기한')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('d_day', models.IntegerField(max_length=10, verbose_name='디데이')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='found_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '설문조사',
                'verbose_name_plural': '설문조사_리스트',
                'db_table': 'Survey_List',
                'ordering': ('-registered_date',),
            },
        ),
    ]