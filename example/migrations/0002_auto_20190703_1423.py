# Generated by Django 2.2.3 on 2019-07-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='object',
            index=models.Index(fields=['name', 'description'], name='example_obj_name_e06656_idx'),
        ),
    ]