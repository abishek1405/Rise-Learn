# Generated by Django 5.0 on 2024-05-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0002_customuser_class_name_customuser_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verifi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
