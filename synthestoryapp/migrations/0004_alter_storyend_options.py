# Generated by Django 3.2.15 on 2022-09-07 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('synthestoryapp', '0003_storyend_storymiddle_storystart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storyend',
            options={'ordering': ['creation_date']},
        ),
    ]