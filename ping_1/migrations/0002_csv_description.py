# Generated by Django 4.2.4 on 2024-02-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ping_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='Description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
