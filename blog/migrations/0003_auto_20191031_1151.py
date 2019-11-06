# Generated by Django 2.2.6 on 2019-10-31 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191031_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_annotation',
            field=models.CharField(default='About something', max_length=300, verbose_name='Название статьи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=100, verbose_name='Название статьи'),
        ),
    ]