# Generated by Django 2.0.6 on 2018-06-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20180605_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='head_img',
            field=models.ImageField(default=1, upload_to='', verbose_name='文章标题图片'),
            preserve_default=False,
        ),
    ]