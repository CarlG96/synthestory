# Generated by Django 3.2.15 on 2022-09-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synthestoryapp', '0005_auto_20220908_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storyideas',
            options={'ordering': ['-creation_date']},
        ),
        migrations.AlterField(
            model_name='storyideas',
            name='slug',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]
