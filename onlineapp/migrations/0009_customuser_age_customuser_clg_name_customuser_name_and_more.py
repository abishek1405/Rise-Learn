# Generated by Django 5.0.7 on 2024-07-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0008_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='clg_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
