# Generated by Django 3.2.6 on 2021-08-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_deleted',
            field=models.CharField(default=0, max_length=1),
        ),
    ]
