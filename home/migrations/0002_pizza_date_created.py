# Generated by Django 5.2 on 2025-04-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='date_created',
            field=models.DateField(null=True),
        ),
    ]
