# Generated by Django 3.2.23 on 2023-12-21 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_imgs',
            field=models.ManyToManyField(blank=True, to='Gallery.Img_Files'),
        ),
    ]