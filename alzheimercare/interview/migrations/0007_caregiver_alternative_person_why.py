# Generated by Django 2.1.7 on 2019-05-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_auto_20190503_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='caregiver',
            name='alternative_person_why',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
