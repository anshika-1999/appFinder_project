# Generated by Django 2.2.12 on 2020-04-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywordFinder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_keyword',
            name='url',
            field=models.TextField(default=''),
        ),
    ]
