# Generated by Django 3.2.13 on 2022-10-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/image', verbose_name='영화 포스터'),
        ),
    ]
