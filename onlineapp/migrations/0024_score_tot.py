# Generated by Django 5.0.7 on 2024-08-03 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0023_rename_student_id_score_worng_ans'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='tot',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
